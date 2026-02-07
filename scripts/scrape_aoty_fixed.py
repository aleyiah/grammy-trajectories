"""
Specialized Album of the Year scraper
Handles the unique table structure where years are in row headers
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

url = "https://en.wikipedia.org/wiki/Grammy_Award_for_Album_of_the_Year"

print("Fetching Album of the Year page...")
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
            # Extract year from the header cell
            year_text = year_cell.get_text(strip=True)
            # Remove citation brackets
            year_text = re.sub(r'\[\d+\]', '', year_text)
            # Parse year
            year_match = re.search(r'(19\d{2}|20\d{2})', year_text)
            if year_match:
                current_year = int(year_match.group(1))
                print(f"  Year: {current_year}")
        
        # Get data cells (album and artist)
        cells = row.find_all('td')
        if len(cells) >= 2 and current_year:
            # Column structure: Album | Artist | Production team
            album = cells[0].get_text(strip=True)
            artist = cells[1].get_text(strip=True)
            
            # Clean up
            album = re.sub(r'\[\d+\]', '', album)
            artist = re.sub(r'\[\d+\]', '', artist)
            
            # Check if winner (first row of year = winner, has yellow background)
            is_winner = False
            row_style = row.get('style', '')
            cell_styles = ' '.join(c.get('style', '') for c in cells)
            all_styles = (row_style + ' ' + cell_styles).lower()
            
            # Winner indicators
            if any(color in all_styles for color in ['gold', 'yellow', 'ffd', 'ffc', 'ffffbf']):
                is_winner = True
            if row.find('b') or row.find('strong'):
                is_winner = True
            
            records.append({
                'year': current_year,
                'category': 'Album of the Year',
                'artist': artist,
                'album': album,
                'is_winner': is_winner
            })

print(f"\n✓ Extracted {len(records)} total records")
print(f"  Winners: {sum(1 for r in records if r['is_winner'])}")
print(f"  Nominees: {sum(1 for r in records if not r['is_winner'])}")

# Create DataFrame
df = pd.DataFrame(records)
print("\nSample:")
print(df.head(20))

# Save
output_path = "/Users/aleyiahpena/Downloads/grammy-trajectories/data/raw/aoty_scraped.csv"
df.to_csv(output_path, index=False)
print(f"\n💾 Saved to: {output_path}")
