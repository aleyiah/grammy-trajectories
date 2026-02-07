"""
diagnostic_request.py - Check what we're actually getting from Wikipedia
"""

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Grammy_Award_for_Album_of_the_Year"

print("Fetching Album of the Year page...")
print(f"URL: {url}\n")

try:
    response = requests.get(url, timeout=10)
    print(f"Status code: {response.status_code}")
    print(f"Content length: {len(response.content)} bytes")
    print(f"Content type: {response.headers.get('content-type')}")
    
    # Check if we got HTML
    content_preview = response.text[:500]
    print(f"\nFirst 500 characters of response:")
    print("-" * 60)
    print(content_preview)
    print("-" * 60)
    
    # Try parsing
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Check for common Wikipedia elements
    print(f"\nFound <title> tag: {soup.title.string if soup.title else 'None'}")
    print(f"Found <table> tags: {len(soup.find_all('table'))}")
    print(f"Found <div> tags: {len(soup.find_all('div'))}")
    print(f"Found <p> tags: {len(soup.find_all('p'))}")
    
    # Check specifically for tables
    tables = soup.find_all('table')
    print(f"\nTable breakdown:")
    for idx, table in enumerate(tables[:5]):  # Show first 5
        classes = table.get('class', [])
        print(f"  Table {idx+1}: classes = {classes}")
    
except Exception as e:
    print(f"\nERROR: {e}")
    import traceback
    traceback.print_exc()
