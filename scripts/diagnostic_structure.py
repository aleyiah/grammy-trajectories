"""
Check how Album of the Year page is actually structured
"""

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Grammy_Award_for_Album_of_the_Year"
headers = {"User-Agent": "GrammyBot/1.0 (Educational)"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all section headers
print("SECTION HEADINGS with years:")
print("=" * 60)
for heading in soup.find_all(['h2', 'h3', 'h4']):
    text = heading.get_text(strip=True)
    # Look for headings with years
    if any(str(year) in text for year in range(1950, 2030)):
        print(f"{heading.name}: {text}")
        
        # Find the next table after this heading
        next_table = heading.find_next('table', class_='wikitable')
        if next_table:
            # Get table headers
            header_row = next_table.find('tr')
            if header_row:
                headers = [th.get_text(strip=True) for th in header_row.find_all(['th', 'td'])]
                print(f"  Next table headers: {headers}")
                
                # Get first row
                first_data_row = next_table.find_all('tr')[1] if len(next_table.find_all('tr')) > 1 else None
                if first_data_row:
                    cells = [td.get_text(strip=True)[:40] for td in first_data_row.find_all(['td', 'th'])]
                    print(f"  First row: {cells}")
        print()

print("\n" + "=" * 60)
print("This shows how years are organized on the page")
