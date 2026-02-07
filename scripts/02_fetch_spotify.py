"""
02_fetch_spotify.py

Fetches artist streaming metrics from Spotify API.

WHAT THIS WILL DO:
- Read artist names from Grammy data
- Search for artists on Spotify
- Fetch metrics: monthly listeners, followers
- Save to JSON/CSV

TO BE IMPLEMENTED IN WEEK 1
"""

import json
import time
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from config import (
    SPOTIFY_CLIENT_ID,
    SPOTIFY_CLIENT_SECRET,
    SPOTIFY_REQUEST_DELAY,
    GRAMMY_PROCESSED_CSV,
    SPOTIFY_RAW_JSON,
)

def main():
    print("Spotify fetcher - Coming in Week 1")
    print("This script will:")
    print("  1. Load Grammy artist names")
    print("  2. Search Spotify for each artist")
    print("  3. Fetch streaming metrics")
    print("  4. Handle rate limiting")
    print("  5. Save results")

if __name__ == "__main__":
    main()
