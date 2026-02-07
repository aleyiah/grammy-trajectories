"""
Check Song of the Year page structure
"""

import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

USER_AGENT = os.getenv("WIKI_USER_AGENT", "GrammyBot/1.0 (Educational)")
HEADERS = {"User-Agent": USER_AGENT}

url = "https://en.wikipedia.org/wiki/Grammy_Award_for_Song_of_the_Year"

response = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(response.content, 'html.parser')

tables = soup.find_all('table', class_='wikitable')
print(f"Found {len(tables)} tables\n")

# Check first few tables
for idx in range(min(4, len(tables))):
    table = tables[idx]
    print(f"={'='*60}")
    print(f"TABLE {idx + 1}")
    print(f"={'='*60}")
    
    # Get headers
    header_row = table.find('tr')
    if header_row:
        headers = [th.get_text(strip=True) for th in header_row.find_all(['th', 'td'])]
        print(f"Headers: {headers}\n")
    
    # Check first 5 rows
    rows = table.find_all('tr')[1:6]
    for row_idx, row in enumerate(rows):
        print(f"Row {row_idx + 1}:")
        
        # Check for year cell with rowspan
        year_cell = row.find('th', attrs={'rowspan': True})
        if year_cell:
            print(f"  YEAR CELL (rowspan): {year_cell.get_text(strip=True)}")
        
        # Check all th cells
        all_th = row.find_all('th')
        if all_th:
            print(f"  All TH cells: {[th.get_text(strip=True)[:30] for th in all_th]}")
        
        # Check all td cells
        all_td = row.find_all('td')
        if all_td:
            print(f"  TD cells ({len(all_td)}): {[td.get_text(strip=True)[:40] for td in all_td]}")
        
        print()
    
    print()
