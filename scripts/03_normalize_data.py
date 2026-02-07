"""
03_normalize_data.py

Normalizes artist names and merges Grammy + Spotify datasets.

WHAT THIS WILL DO:
- Match artist names across datasets using fuzzy matching
- Handle edge cases (name variations, collaborations)
- Merge into final analysis-ready dataset
- Flag unmatched artists for manual review

TO BE IMPLEMENTED IN WEEK 1
"""

import pandas as pd
from fuzzywuzzy import fuzz

from config import (
    GRAMMY_PROCESSED_CSV,
    SPOTIFY_PROCESSED_CSV,
    ARTIST_MAPPING_CSV,
    FINAL_DATASET_CSV,
    FUZZY_MATCH_THRESHOLD,
)

def main():
    print("Data normalization - Coming in Week 1")
    print("This script will:")
    print("  1. Load Grammy and Spotify datasets")
    print("  2. Fuzzy match artist names")
    print("  3. Manually review low-confidence matches")
    print("  4. Merge into final dataset")
    print("  5. Generate QA report")

if __name__ == "__main__":
    main()
