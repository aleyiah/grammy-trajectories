"""
01_scrape_grammys.py - FIXED VERSION

Scrapes Grammy Award nominee and winner data from Wikipedia.
This version properly handles different table structures and detects winners.
"""

import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import re
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import configuration
from config import (
    GRAMMY_CATEGORIES,
    MVP_CATEGORIES,
    REQUEST_DELAY_SECONDS,
    GRAMMY_RAW_CSV,
)

# User-Agent for Wikipedia requests
USER_AGENT = os.getenv("WIKI_USER_AGENT", "GrammyTrajectoriesBot/1.0 (Educational)")
REQUEST_HEADERS = {"User-Agent": USER_AGENT}


def fetch_page(url):
    """Fetch Wikipedia page with proper headers."""
    print(f"  Fetching: {url}")
    try:
        response = requests.get(url, headers=REQUEST_HEADERS, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    except requests.RequestException as e:
        print(f"  ❌ Error: {e}")
        raise


def is_summary_table(headers):
    """Check if this is a summary table (not nominee/winner list)."""
    header_text = ' '.join(str(h).lower() for h in headers)
    summary_keywords = ['number of victories', 'number of nominations', 'most wins']
    return any(keyword in header_text for keyword in summary_keywords)


def find_artist_column(headers):
    """Find which column contains artist names."""
    print(f"      Detecting artist column from headers: {headers}")
    
    for idx, header in enumerate(headers):
        h_lower = str(header).lower()
        
        # Explicitly look for "artist(s)" or "artist/band" 
        if 'artist' in h_lower:
            # But NOT if it says "production" or "producer"
            if 'production' not in h_lower and 'producer' not in h_lower:
                print(f"      Found 'artist' in column {idx}: '{header}'")
                return idx
    
    # Fallback: for simple two-column tables (Year | Artist)
    if len(headers) == 2:
        return 1
    
    # If we have 3+ columns and didn't find explicit "Artist" header,
    # assume Year | Album | Artist structure
    if len(headers) >= 3:
        return 2
    
    # Last resort
    return 1


def parse_year(year_text):
    """Extract ceremony year from text, handling Wikipedia citations."""
    # Remove citation brackets FIRST
    year_text = re.sub(r'\[\d+\]', '', year_text)
    
    # Look for year in parentheses first (most reliable)
    paren_match = re.search(r'\((\d{4})\)', year_text)
    if paren_match:
        year = int(paren_match.group(1))
        if 1950 <= year <= 2030:
            return year
    
    # Find all 4-digit years
    all_years = re.findall(r'\b(19\d{2}|20\d{2})\b', year_text)
    valid_years = [int(y) for y in all_years if 1950 <= int(y) <= 2030]
    
    if valid_years:
        # Take the most recent year (likely ceremony year, not album title)
        return max(valid_years)
    
    return None


def clean_artist_name(text):
    """Clean artist name from Wikipedia formatting."""
    # Remove citation brackets
    text = re.sub(r'\[\d+\]', '', text)
    # Remove quotes
    text = text.replace('"', '').replace('"', '').replace('"', '')
    # Remove "for Album" or "by Artist" patterns
    text = re.sub(r'\s+for\s+.*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\s+by\s+.*', '', text, flags=re.IGNORECASE)
    return text.strip()


def is_winner(row, cells):
    """Detect if this row represents a Grammy winner."""
    # Check row and cell styling for background colors
    row_style = row.get('style', '')
    cell_styles = ' '.join(cell.get('style', '') for cell in cells)
    all_styles = (row_style + ' ' + cell_styles).lower()
    
    # Winner background colors
    if 'background' in all_styles:
        winner_colors = ['gold', 'yellow', 'ffd', 'ffc', 'f9f', 'lightgold', 'ffffbf']
        if any(color in all_styles for color in winner_colors):
            return True
    
    # Check for bold formatting (winners often bold)
    if row.find('b') or row.find('strong'):
        return True
    
    # Check for winner symbols or text
    for cell in cells:
        text = cell.get_text(strip=True)
        if any(sym in text for sym in ['✓', '★', '†', 'Winner', 'winner']):
            return True
    
    # Check CSS classes
    row_class = ' '.join(row.get('class', [])).lower()
    if 'winner' in row_class or 'selected' in row_class:
        return True
    
    return False


def extract_grammy_data(soup, category_name):
    """Extract Grammy data from Wikipedia page."""
    print(f"  Parsing {category_name}...")
    
    records = []
    tables = soup.find_all('table', class_='wikitable')
    
    if not tables:
        print(f"  ⚠️ No wikitable tables found")
        return records
    
    print(f"  Found {len(tables)} tables")
    
    for table_idx, table in enumerate(tables):
        # Get headers
        header_row = table.find('tr')
        if not header_row:
            continue
            
        headers = [th.get_text(strip=True) for th in header_row.find_all(['th', 'td'])]
        
        # Skip summary tables
        if is_summary_table(headers):
            print(f"    Table {table_idx + 1}: Skipping summary table")
            continue
        
        # Skip tables with too few columns
        if len(headers) < 2:
            continue
        
        print(f"    Table {table_idx + 1}: {headers[:3]}...")  # Show first 3 headers
        
        # Find artist column
        artist_col = find_artist_column(headers)
        print(f"      Artist in column {artist_col}")
        
        # Parse rows
        rows = table.find_all('tr')[1:]  # Skip header
        table_records = 0
        rows_processed = 0
        
        for row in rows:
            cells = row.find_all(['td', 'th'])
            
            if len(cells) < 2:
                continue
            
            rows_processed += 1
            
            # Debug: show first few rows
            if rows_processed <= 3 and table_idx in [1, 2]:  # Tables 2 and 3
                print(f"        DEBUG Row {rows_processed}:")
                print(f"          Number of cells: {len(cells)}")
                for i, cell in enumerate(cells[:4]):  # First 4 cells
                    print(f"          Cell {i}: {cell.get_text(strip=True)[:50]}")
            
            try:
                # Parse year
                year_text = cells[0].get_text(strip=True)
                year = parse_year(year_text)
                
                if not year or year < 1950 or year > 2030:
                    if rows_processed <= 3 and table_idx in [1, 2]:
                        print(f"          REJECTED: Invalid year from '{year_text}' -> {year}")
                    continue
                
                # Parse artist (using detected column)
                if artist_col >= len(cells):
                    if rows_processed <= 3 and table_idx in [1, 2]:
                        print(f"          REJECTED: Not enough cells ({len(cells)} < {artist_col})")
                    continue
                    
                artist_text = cells[artist_col].get_text(strip=True)
                artist = clean_artist_name(artist_text)
                
                if not artist or len(artist) < 2:
                    if rows_processed <= 3 and table_idx in [1, 2]:
                        print(f"          REJECTED: Artist too short: '{artist}'")
                    continue
                
                # Detect winner
                is_win = is_winner(row, cells)
                
                if rows_processed <= 3 and table_idx in [1, 2]:
                    print(f"          ACCEPTED: {year}, {artist}, winner={is_win}")
                
                records.append({
                    'year': year,
                    'category': category_name,
                    'artist': artist,
                    'is_winner': is_win,
                })
                table_records += 1
                
            except Exception as e:
                if rows_processed <= 3 and table_idx in [1, 2]:
                    print(f"          EXCEPTION: {e}")
                continue
        
        print(f"      Processed {rows_processed} rows, extracted {table_records} records")
    
    print(f"  ✓ Total: {len(records)} records")
    return records


def main():
    """Main scraping workflow."""
    print("=" * 60)
    print("GRAMMY DATA SCRAPER - FIXED VERSION")
    print("=" * 60)
    print()
    
    all_records = []
    
    categories_to_scrape = {
        name: url for name, url in GRAMMY_CATEGORIES.items() 
        if name in MVP_CATEGORIES
    }
    
    print(f"Scraping {len(categories_to_scrape)} categories:")
    for name in categories_to_scrape.keys():
        print(f"  - {name}")
    print()
    
    for category_name, url in categories_to_scrape.items():
        print(f"📥 {category_name}")
        
        try:
            soup = fetch_page(url)
            records = extract_grammy_data(soup, category_name)
            all_records.extend(records)
            
            print(f"  Waiting {REQUEST_DELAY_SECONDS}s...\n")
            time.sleep(REQUEST_DELAY_SECONDS)
            
        except Exception as e:
            print(f"  ❌ Failed: {e}\n")
            continue
    
    # Create DataFrame
    print("=" * 60)
    print(f"✓ Scraped {len(all_records)} total records")
    
    if not all_records:
        print("❌ No data scraped")
        return
    
    df = pd.DataFrame(all_records)
    
    # Summary
    print()
    print("DATA SUMMARY:")
    print(f"  Total records: {len(df)}")
    print(f"  Year range: {df['year'].min()} - {df['year'].max()}")
    print(f"  Winners: {df['is_winner'].sum()}")
    print(f"  Nominees: {(~df['is_winner']).sum()}")
    print()
    print("By category:")
    print(df.groupby('category').size())
    print()
    print("Winners by category:")
    print(df[df['is_winner']].groupby('category').size())
    
    # Save
    df.to_csv(GRAMMY_RAW_CSV, index=False)
    print()
    print(f"💾 Saved to: {GRAMMY_RAW_CSV}")
    print()
    
    # Sample
    print("Sample data:")
    print(df.head(10).to_string())
    print()
    print("=" * 60)
    print("✓ Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()