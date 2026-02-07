"""
diagnostic_aoty.py - Inspect Album of the Year Wikipedia page structure
"""

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Grammy_Award_for_Album_of_the_Year"

print("Fetching Album of the Year page...")
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

tables = soup.find_all('table', class_='wikitable')
print(f"\nFound {len(tables)} wikitable tables\n")

for idx, table in enumerate(tables):
    print(f"=" * 60)
    print(f"TABLE {idx + 1}")
    print("=" * 60)
    
    # Get headers
    header_row = table.find('tr')
    if header_row:
        headers = [th.get_text(strip=True) for th in header_row.find_all(['th', 'td'])]
        print(f"Headers: {headers}")
    
    # Get first 3 data rows
    rows = table.find_all('tr')[1:4]  # Skip header, get first 3 rows
    print(f"\nFirst 3 rows of data:")
    
    for row_idx, row in enumerate(rows):
        cells = row.find_all(['td', 'th'])
        print(f"\n  Row {row_idx + 1}:")
        for cell_idx, cell in enumerate(cells):
            text = cell.get_text(strip=True)[:50]  # Truncate long text
            style = cell.get('style', '')
            print(f"    Cell {cell_idx}: {text}")
            if style:
                print(f"      Style: {style}")
        
        # Check row styling
        row_style = row.get('style', '')
        if row_style:
            print(f"  Row style: {row_style}")
    
    print("\n")

print("\n" + "=" * 60)
print("Diagnostic complete!")
