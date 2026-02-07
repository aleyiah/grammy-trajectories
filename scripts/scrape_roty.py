"""
Record of the Year scraper
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

url = "https://en.wikipedia.org/wiki/Grammy_Award_for_Record_of_the_Year"

print("Fetching Record of the Year page...")
response = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(response.content, 'html.parser')

tables = soup.find_all('table', class_='wikitable')
print(f"Found {len(tables)} tables")

records = []
current_year = None

for table_idx, table in enumerate(tables):
    # Skip first table (summary)
    if table_idx == 0:
        continue
    
    print(f"\nProcessing table {table_idx + 1}...")
    
    for row in table.find_all('tr'):
        # Check if this row has a year header (th with rowspan)
        year_cell = row.find('th', attrs={'rowspan': True})
        if year_cell:
            year_text = year_cell.get_text(strip=True)
            year_text = re.sub(r'\[\d+\]', '', year_text)
            year_match = re.search(r'(19\d{2}|20\d{2})', year_text)
            if year_match:
                current_year = int(year_match.group(1))
                print(f"  Year: {current_year}")
        
        # Get data cells
        cells = row.find_all('td')
        if len(cells) >= 2 and current_year:
            # ROTY table structure: Record | Artist(s) | Production team
            record_title = cells[0].get_text(strip=True)
            artist = cells[1].get_text(strip=True)
            
            # Clean up
            record_title = re.sub(r'\[\d+\]', '', record_title)
            artist = re.sub(r'\[\d+\]', '', artist)
            
            # Check if winner
            is_winner = False
            row_style = row.get('style', '')
            cell_styles = ' '.join(c.get('style', '') for c in cells)
            all_styles = (row_style + ' ' + cell_styles).lower()
            
            winner_indicators = [
                'faeb86', 'ffffbf', 'gold', 'yellow', 'ffd', 'ffc', 
                'f9f', 'lightgold', 'background:#f', 'background: #f'
            ]
            
            if 'background' in all_styles:
                if any(indicator in all_styles for indicator in winner_indicators):
                    is_winner = True
            if row.find('b') or row.find('strong'):
                is_winner = True
            
            records.append({
                'year': current_year,
                'category': 'Record of the Year',
                'artist': artist,
                'record': record_title,
                'is_winner': is_winner
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
output_path = "/Users/aleyiahpena/Downloads/grammy-trajectories/data/raw/roty_scraped.csv"
df.to_csv(output_path, index=False)
print(f"\n💾 Saved to: {output_path}")
