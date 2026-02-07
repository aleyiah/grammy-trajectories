"""
Song of the Year scraper
Uses the same rowspan year logic
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

url = "https://en.wikipedia.org/wiki/Grammy_Award_for_Song_of_the_Year"

print("Fetching Song of the Year page...")
response = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(response.content, 'html.parser')

tables = soup.find_all('table', class_='wikitable')
print(f"Found {len(tables)} tables")

records = []
current_year = None

for table_idx, table in enumerate(tables):
    print(f"\nProcessing table {table_idx + 1}...")
    
    for row in table.find_all('tr')[1:]:  # Skip header row
        # Get all cells - SOTY has year in TH, rest in TD
        year_cell = row.find('th')  # Year is in regular TH, not rowspan
        data_cells = row.find_all('td')
        
        if not year_cell or len(data_cells) < 3:
            continue
        
        # Parse year from TH cell
        year_text = year_cell.get_text(strip=True)
        year_text = re.sub(r'\[\d+\]', '', year_text)
        year_match = re.search(r'(19\d{2}|20\d{2})', year_text)
        
        if not year_match:
            continue
            
        current_year = int(year_match.group(1))
        
        # Data cells: Songwriter(s) | Work | Performing artist(s) | Nominees | Ref
        # Indices:    0              | 1    | 2                     | 3        | 4
        songwriter = data_cells[0].get_text(strip=True)
        song_title = data_cells[1].get_text(strip=True)
        performer = data_cells[2].get_text(strip=True)
        
        # Clean up
        songwriter = re.sub(r'\[\d+\]', '', songwriter)
        song_title = re.sub(r'\[\d+\]', '', song_title)
        song_title = song_title.replace('"', '').replace('"', '').replace('"', '')  # Remove quotes
        performer = re.sub(r'\[\d+\]', '', performer)
        
        # Check if winner (asterisk * in song title or background color)
        is_winner = False
        
        # Check for asterisk (winners marked with *)
        if '*' in data_cells[1].get_text():
            is_winner = True
        
        # Also check background color
        row_style = row.get('style', '')
        cell_styles = ' '.join(c.get('style', '') for c in data_cells)
        all_styles = (row_style + ' ' + cell_styles).lower()
        
        winner_indicators = [
            'faeb86', 'ffffbf', 'gold', 'yellow', 'ffd', 'ffc', 
            'f9f', 'lightgold', 'background:#f', 'background: #f'
        ]
        
        if 'background' in all_styles:
            if any(indicator in all_styles for indicator in winner_indicators):
                is_winner = True
        
        # Remove asterisk from song title
        song_title = song_title.replace('*', '').strip()
        
        # Add main entry
        records.append({
            'year': current_year,
            'category': 'Song of the Year',
            'songwriter': songwriter,
            'song': song_title,
            'performer': performer,
            'is_winner': is_winner
        })
        
        # Parse additional nominees from column 4 if it exists
        if len(data_cells) >= 4:
            nominees_cell = data_cells[3]
            nominee_text = nominees_cell.get_text(strip=True)
            
            # Clean citations
            nominee_text = re.sub(r'\[\d+\]', '', nominee_text)
            
            # Try to parse: "Songwriter for 'Song' performed by Artist"
            # Pattern: Name(s) for "Song Title" performed by Artist
            matches = re.finditer(r'([^"]+?)\s+for\s+["\']([^"\']+)["\'](?:\s+performed by\s+([^;•\n]+))?', nominee_text)
            
            for match in matches:
                nom_songwriter = match.group(1).strip()
                nom_song = match.group(2).strip()
                nom_performer = match.group(3).strip() if match.group(3) else ""
                
                # Skip if this looks like junk/incomplete data
                if len(nom_songwriter) < 3 or len(nom_song) < 3:
                    continue
                
                records.append({
                    'year': current_year,
                    'category': 'Song of the Year',
                    'songwriter': nom_songwriter,
                    'song': nom_song,
                    'performer': nom_performer,
                    'is_winner': False
                })

print(f"\n✓ Extracted {len(records)} total records")
print(f"  Winners: {sum(1 for r in records if r['is_winner'])}")
print(f"  Nominees: {sum(1 for r in records if not r['is_winner'])}")

df = pd.DataFrame(records)

if len(df) > 0:
    print(f"  Year range: {df['year'].min()} - {df['year'].max()}")

print("\nSample:")
print(df.head(20))

# Save
output_path = "/Users/aleyiahpena/Downloads/grammy-trajectories/data/raw/soty_scraped.csv"
df.to_csv(output_path, index=False)
print(f"\n💾 Saved to: {output_path}")