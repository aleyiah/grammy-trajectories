"""
test_headers.py - Test Wikipedia request with proper headers
"""

import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://en.wikipedia.org/wiki/Grammy_Award_for_Album_of_the_Year"

# Set proper headers
headers = {
    "User-Agent": os.getenv("WIKI_USER_AGENT", "GrammyTrajectoriesBot/1.0 (Educational Project; contact@example.com)")
}

print(f"Using User-Agent: {headers['User-Agent']}\n")
print("Fetching Album of the Year page...")

try:
    response = requests.get(url, headers=headers, timeout=10)
    print(f"Status code: {response.status_code}")
    
    if response.status_code == 200:
        print("✅ SUCCESS! Wikipedia allowed the request\n")
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find tables
        all_tables = soup.find_all('table')
        wikitables = soup.find_all('table', class_='wikitable')
        
        print(f"Total tables found: {len(all_tables)}")
        print(f"Tables with 'wikitable' class: {len(wikitables)}")
        
        if wikitables:
            print("\nFirst 3 wikitable headers:")
            for idx in range(min(3, len(wikitables))):
                table = wikitables[idx]
                header_row = table.find('tr')
                if header_row:
                    headers = [th.get_text(strip=True) for th in header_row.find_all(['th', 'td'])]
                    print(f"  Table {idx+1}: {headers}")
        
    else:
        print(f"❌ Request blocked with status {response.status_code}")
        print(f"Response: {response.text[:200]}")
        
except Exception as e:
    print(f"ERROR: {e}")