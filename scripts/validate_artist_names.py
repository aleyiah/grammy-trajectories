"""
Artist Name Validation Script
Checks for potential Billboard matching issues in BNA winner names
"""

import pandas as pd
import re

# Load Grammy data
grammy_df = pd.read_csv('data/processed/grammy_data_clean.csv')

# Filter to BNA winners only
bna_winners = grammy_df[(grammy_df['category'] == 'Best New Artist') & 
                         (grammy_df['is_winner'] == True)]

print("="*70)
print("ARTIST NAME VALIDATION - POTENTIAL BILLBOARD MATCHING ISSUES")
print("="*70)

print(f"\nTotal BNA winners: {len(bna_winners)}")

# Check for special characters
special_chars_patterns = {
    'Comma': r',',
    'Ampersand': r'&',
    'Slash': r'/',
    'Parentheses': r'\(|\)',
    'Brackets': r'\[|\]',
    'Period': r'\.',
    'Apostrophe': r"'",
    'Hyphen': r'-',
    'Featuring': r'featuring|feat\.|ft\.',
}

print("\n--- SPECIAL CHARACTERS DETECTED ---")
for char_type, pattern in special_chars_patterns.items():
    matches = bna_winners[bna_winners['artist'].str.contains(pattern, case=False, na=False)]
    if len(matches) > 0:
        print(f"\n{char_type} ({len(matches)} artists):")
        for artist in matches['artist'].unique():
            print(f"  - {artist}")

# Check for parenthetical notes (like "Revoked")
print("\n--- PARENTHETICAL NOTES ---")
parentheses_matches = bna_winners[bna_winners['artist'].str.contains(r'\(.*\)', na=False)]
if len(parentheses_matches) > 0:
    for artist in parentheses_matches['artist'].unique():
        print(f"  - {artist}")
else:
    print("  None found")

# Check for very long names (might be truncated in filename)
print("\n--- LONG NAMES (>30 chars) ---")
long_names = bna_winners[bna_winners['artist'].str.len() > 30]
if len(long_names) > 0:
    for artist, length in zip(long_names['artist'].unique(), 
                               long_names['artist'].str.len().unique()):
        print(f"  - {artist} ({length} chars)")
else:
    print("  None found")

# Check for duplicate artists (won multiple times)
print("\n--- DUPLICATE WINNERS ---")
duplicates = bna_winners['artist'].value_counts()
duplicates = duplicates[duplicates > 1]
if len(duplicates) > 0:
    print("Artists who won BNA multiple times (data error?):")
    for artist, count in duplicates.items():
        print(f"  - {artist}: {count} times")
        years = bna_winners[bna_winners['artist'] == artist]['year'].tolist()
        print(f"    Years: {years}")
else:
    print("  None found (expected)")

# Full list of all artists
print("\n" + "="*70)
print("COMPLETE LIST OF BNA WINNERS (alphabetical)")
print("="*70)
for i, artist in enumerate(sorted(bna_winners['artist'].unique()), 1):
    print(f"{i:2d}. {artist}")

print("\n" + "="*70)
print("RECOMMENDATIONS")
print("="*70)
print("""
1. Artists with commas/ampersands: Filename matching already handled
2. Artists with parentheses: May need manual cleanup
3. Long names: Will be truncated to 50 chars in filename
4. Featured artists: May not match if Billboard lists differently

NEXT STEPS:
- Review parenthetical notes (especially "Revoked")
- Test problem artists individually before full scrape
- Document any manual corrections in scraping_log.md
""")
