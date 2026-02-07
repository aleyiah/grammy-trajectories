"""
Check how Best New Artist winners are styled
"""

import requests
from bs4 import BeautifulSoup
import re
import os
from dotenv import load_dotenv

load_dotenv()

USER_AGENT = os.getenv("WIKI_USER_AGENT", "GrammyBot/1.0 (Educational)")
HEADERS = {"User-Agent": USER_AGENT}

url = "https://en.wikipedia.org/wiki/Grammy_Award_for_Best_New_Artist"

response = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(response.content, 'html.parser')

tables = soup.find_all('table', class_='wikitable')

print("Checking first table for 1960s winners styling...\n")
table = tables[0]

current_year = None
first_row_of_year = False

for row in table.find_all('tr')[:20]:  # First 20 rows
    # Check for year
    year_cell = row.find('th', attrs={'rowspan': True})
    if year_cell:
        year_text = year_cell.get_text(strip=True)
        year_text = re.sub(r'\[\d+\]', '', year_text)
        year_match = re.search(r'(19\d{2}|20\d{2})', year_text)
        if year_match:
            current_year = int(year_match.group(1))
            first_row_of_year = True
            print(f"\n{'='*60}")
            print(f"YEAR: {current_year}")
            print(f"{'='*60}")
    
    cells = row.find_all('td')
    if len(cells) >= 1 and current_year:
        artist = cells[0].get_text(strip=True)[:40]
        
        # Check ALL possible winner indicators
        row_style = row.get('style', '')
        row_class = row.get('class', [])
        cell_style = cells[0].get('style', '')
        
        # Check for bold/strong
        has_bold = bool(row.find('b') or row.find('strong'))
        
        print(f"\n{'FIRST ROW (WINNER?)' if first_row_of_year else 'Nominee'}:")
        print(f"  Artist: {artist}")
        print(f"  Row style: {row_style}")
        print(f"  Row class: {row_class}")
        print(f"  Cell style: {cell_style}")
        print(f"  Has bold: {has_bold}")
        
        first_row_of_year = False

print("\n\nLook for patterns in FIRST ROW styling vs nominees")
