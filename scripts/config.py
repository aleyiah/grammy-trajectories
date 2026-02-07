"""
Configuration file for Grammy Trajectories project.
Stores constants, file paths, and shared settings used across all scripts.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ============================================================================
# PROJECT PATHS
# ============================================================================

# Root directory of the project
PROJECT_ROOT = Path(__file__).parent.parent

# Data directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
FINAL_DATA_DIR = DATA_DIR / "final"

# Ensure directories exist
for directory in [RAW_DATA_DIR, PROCESSED_DATA_DIR, FINAL_DATA_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# ============================================================================
# API CREDENTIALS
# ============================================================================

# Spotify API credentials (from .env file)
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Wikipedia User Agent (optional but polite for web scraping)
WIKI_USER_AGENT = os.getenv("WIKI_USER_AGENT", "GrammyTrajectories/1.0")

# ============================================================================
# GRAMMY CATEGORIES TO SCRAPE
# ============================================================================

# Grammy categories we're analyzing
# Each category maps to its Wikipedia page URL
GRAMMY_CATEGORIES = {
    "Best New Artist": "https://en.wikipedia.org/wiki/Grammy_Award_for_Best_New_Artist",
    "Album of the Year": "https://en.wikipedia.org/wiki/Grammy_Award_for_Album_of_the_Year",
    "Record of the Year": "https://en.wikipedia.org/wiki/Grammy_Award_for_Record_of_the_Year",
    "Song of the Year": "https://en.wikipedia.org/wiki/Grammy_Award_for_Song_of_the_Year",
}

# Start with these two for MVP (can expand later)
MVP_CATEGORIES = [
    "Best New Artist",
    "Album of the Year",
]

# ============================================================================
# SCRAPING SETTINGS
# ============================================================================

# How long to wait between HTTP requests (be polite to Wikipedia)
REQUEST_DELAY_SECONDS = 1.0

# Headers for HTTP requests
REQUEST_HEADERS = {
    "User-Agent": WIKI_USER_AGENT,
}

# ============================================================================
# SPOTIFY API SETTINGS
# ============================================================================

# Rate limiting (Spotify allows ~180 requests per minute)
SPOTIFY_REQUESTS_PER_MINUTE = 150  # Conservative limit
SPOTIFY_REQUEST_DELAY = 60 / SPOTIFY_REQUESTS_PER_MINUTE  # ~0.4 seconds

# ============================================================================
# DATA PROCESSING SETTINGS
# ============================================================================

# Fuzzy matching threshold for artist name normalization
# Range: 0-100, where 100 is exact match
FUZZY_MATCH_THRESHOLD = 85

# Common artist name prefixes to normalize
# e.g., "The Beatles" vs "Beatles"
ARTIST_NAME_PREFIXES = ["The ", "the "]

# ============================================================================
# OUTPUT FILE NAMES
# ============================================================================

# Raw data files
GRAMMY_RAW_CSV = RAW_DATA_DIR / "grammy_data_raw.csv"
SPOTIFY_RAW_JSON = RAW_DATA_DIR / "spotify_data_raw.json"

# Processed data files
GRAMMY_PROCESSED_CSV = PROCESSED_DATA_DIR / "grammy_data_clean.csv"
SPOTIFY_PROCESSED_CSV = PROCESSED_DATA_DIR / "spotify_data_clean.csv"
ARTIST_MAPPING_CSV = PROCESSED_DATA_DIR / "artist_name_mapping.csv"

# Final merged dataset
FINAL_DATASET_CSV = FINAL_DATA_DIR / "grammy_spotify_merged.csv"

# ============================================================================
# VALIDATION
# ============================================================================

def validate_config():
    """
    Validates that all required configuration is present.
    Raises helpful error messages if something is missing.
    """
    errors = []
    
    # Check Spotify credentials
    if not SPOTIFY_CLIENT_ID:
        errors.append("SPOTIFY_CLIENT_ID not found in .env file")
    if not SPOTIFY_CLIENT_SECRET:
        errors.append("SPOTIFY_CLIENT_SECRET not found in .env file")
    
    if errors:
        error_msg = "\n".join([
            "Configuration errors:",
            *[f"  - {error}" for error in errors],
            "\nPlease check your .env file. See .env.example for template."
        ])
        raise ValueError(error_msg)
    
    return True

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_category_filename(category_name):
    """
    Convert category name to safe filename.
    E.g., "Best New Artist" -> "best_new_artist"
    """
    return category_name.lower().replace(" ", "_")

# Run validation when config is imported (but allow it to be skipped for testing)
if os.getenv("SKIP_CONFIG_VALIDATION") != "true":
    try:
        validate_config()
    except ValueError as e:
        print(f"⚠️  Configuration Warning: {e}")
        print("Some scripts may not work until this is resolved.\n")
