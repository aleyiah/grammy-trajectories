"""
diagnostic_aoty_v2.py - Find ALL tables on Album of the Year page
"""

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Grammy_Award_for_Album_of_the_Year"

print("Fetching Album of the Year page...")
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find ALL tables, not just wikitable
all_tables = soup.find_all('table')
print(f"\nFound {len(all_tables)} total tables on page\n")

for idx, table in enumerate(all_tables):
    print(f"=" * 60)
    print(f"TABLE {idx + 1}")
    print("=" * 60)
    
    # Check what class it has
    table_class = table.get('class', [])
    print(f"Table classes: {table_class}")
    
    # Get headers
    header_row = table.find('tr')
    if header_row:
        headers = [th.get_text(strip=True) for th in header_row.find_all(['th', 'td'])]
        print(f"Headers: {headers}")
    
    # Get first 3 data rows
    rows = table.find_all('tr')[1:4]  # Skip header, get first 3 rows
    
    if not rows:
        print("  (No data rows)")
        continue
        
    print(f"\nFirst 3 rows of data:")
    
    for row_idx, row in enumerate(rows):
        cells = row.find_all(['td', 'th'])
        print(f"\n  Row {row_idx + 1} ({len(cells)} cells):")
        for cell_idx, cell in enumerate(cells):
            text = cell.get_text(strip=True)[:80]  # Show more text
            print(f"    Cell {cell_idx}: {text}")
        
        # Check row styling
        row_style = row.get('style', '')
        if row_style:
            print(f"  Row style: {row_style}")
        
        # Check if row has bold tags
        if row.find('b') or row.find('strong'):
            print(f"  Row has BOLD text")
    
    print("\n")

print("\n" + "=" * 60)
print("Diagnostic complete!")
print("\nLook for tables with headers like: Year, Album, Artist")
