"""
Specialized Best New Artist scraper
Uses the same rowspan year logic as Album of the Year
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import os
from dotenv import load_dotenv

load_dotenv()

USER_AGENT = os.getenv("WIKI_USER_AGENT", "GrammyBot/1.0 (Educational)")
HEADERS = {"User-Agent": USER_AGENT}

url = "https://en.wikipedia.org/wiki/Grammy_Award_for_Best_New_Artist"

print("Fetching Best New Artist page...")
response = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(response.content, 'html.parser')

tables = soup.find_all('table', class_='wikitable')
print(f"Found {len(tables)} tables")

records = []
current_year = None

for table_idx, table in enumerate(tables):
    print(f"\nProcessing table {table_idx + 1}...")
    
    for row in table.find_all('tr'):
        # Check if this row has a year header (th with rowspan)
        year_cell = row.find('th', attrs={'rowspan': True})
        if year_cell:
            # Extract year from the header cell
            year_text = year_cell.get_text(strip=True)
            # Remove citation brackets
            year_text = re.sub(r'\[\d+\]', '', year_text)
            # Parse year
            year_match = re.search(r'(19\d{2}|20\d{2})', year_text)
            if year_match:
                current_year = int(year_match.group(1))
                print(f"  Year: {current_year}")
        
        # Get data cells (artist)
        cells = row.find_all('td')
        if len(cells) >= 1 and current_year:
            # BNA table structure: just Artist column
            artist = cells[0].get_text(strip=True)
            
            # Clean up
            artist = re.sub(r'\[\d+\]', '', artist)
            
            # Skip "No award" entries
            if 'no award' in artist.lower():
                continue
            
            # Check if winner (first row of year = winner, has yellow background)
            is_winner = False
            row_style = row.get('style', '')
            cell_styles = ' '.join(c.get('style', '') for c in cells)
            all_styles = (row_style + ' ' + cell_styles).lower()
            
            # Winner indicators - check for specific hex codes and color names
            # BNA uses #FAEB86, AOTY uses #FFFFBF, some use other variations
            winner_indicators = [
                'faeb86',  # BNA specific color
                'ffffbf',  # AOTY specific color
                'gold', 'yellow', 'ffd', 'ffc', 'f9f', 'lightgold',
                'background:#f', 'background: #f'  # Any hex starting with F (yellows/golds)
            ]
            
            if 'background' in all_styles:
                if any(indicator in all_styles for indicator in winner_indicators):
                    is_winner = True
            
            # Also check for bold (some years might use this)
            if row.find('b') or row.find('strong'):
                is_winner = True
            
            records.append({
                'year': current_year,
                'category': 'Best New Artist',
                'artist': artist,
                'is_winner': is_winner
            })

print(f"\n✓ Extracted {len(records)} total records")
print(f"  Winners: {sum(1 for r in records if r['is_winner'])}")
print(f"  Nominees: {sum(1 for r in records if not r['is_winner'])}")

# Create DataFrame
df = pd.DataFrame(records)

# Show year range
if len(df) > 0:
    print(f"  Year range: {df['year'].min()} - {df['year'].max()}")

print("\nSample:")
print(df.head(20))

# Check winner distribution by decade
print("\nWinners by decade:")
df['decade'] = (df['year'] // 10) * 10
print(df[df['is_winner']].groupby('decade').size())

# Save
output_path = "/Users/aleyiahpena/Downloads/grammy-trajectories/data/raw/bna_scraped.csv"
df.to_csv(output_path, index=False)
print(f"\n💾 Saved to: {output_path}")