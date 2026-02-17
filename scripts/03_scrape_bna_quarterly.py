"""
Best New Artist Billboard Scraper - Quarterly Sampling
High-quality data for BNA curse analysis
"""

import billboard
import pandas as pd
import time
import os
from datetime import datetime

def scrape_bna_quarterly(grammy_csv_path='data/processed/grammy_data_clean.csv',
                         output_dir='data/raw/billboard_bna',
                         artists_per_session=66):
    """
    Scrape Billboard data for Best New Artist winners with quarterly sampling
    
    Args:
        grammy_csv_path: Path to Grammy data
        output_dir: Directory to save individual artist files
        artists_per_session: How many artists to process (66 = all BNA winners)
    """
    
    print("="*60)
    print("BEST NEW ARTIST BILLBOARD SCRAPER - QUARTERLY SAMPLING")
    print("="*60)
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Load Grammy data - ONLY Best New Artist winners
    grammy_df = pd.read_csv(grammy_csv_path)
    bna_winners = grammy_df[(grammy_df['category'] == 'Best New Artist') & 
                             (grammy_df['is_winner'] == True)]
    
    artists = bna_winners['artist'].unique()
    print(f"\nTotal BNA winners to process: {len(artists)}")
    
    # Check which artists already scraped
    existing_files = os.listdir(output_dir) if os.path.exists(output_dir) else []
    scraped_artists = [f.replace('.csv', '').replace('_', ' ').replace(' and ', ' & ') for f in existing_files if f.endswith('.csv')]
    
    remaining_artists = [a for a in artists if a not in scraped_artists]
    
    print(f"Already scraped: {len(scraped_artists)}")
    print(f"Remaining: {len(remaining_artists)}")
    print(f"\nThis session will process: {min(artists_per_session, len(remaining_artists))} artists")
    
    # Process artists
    for i, artist in enumerate(remaining_artists[:artists_per_session], 1):
        print(f"\n[{i}/{min(artists_per_session, len(remaining_artists))}] {artist}")
        
        # Get Grammy years for this artist
        grammy_years = bna_winners[(bna_winners['artist'] == artist) & 
                                    (bna_winners['is_winner'] == True)]['year'].tolist()
        
        print(f"  BNA win: {grammy_years}")
        
        # Determine years to check: 5 before first win, 10 after last win
        if not grammy_years:
            print(f"  ✗ No Grammy data found, skipping")
            continue
        
        min_grammy_year = min(grammy_years)
        max_grammy_year = max(grammy_years)
        
        start_year = max(1958, min_grammy_year - 5)  # Hot 100 started Aug 1958
        end_year = min(2026, max_grammy_year + 10)
        
        print(f"  Time window: {start_year}-{end_year} ({end_year - start_year + 1} year span)")
        
        # Generate quarterly dates (Jan 1, Apr 1, Jul 1, Oct 1)
        dates_to_check = []
        for year in range(start_year, end_year + 1):
            for month in ['01-01', '04-01', '07-01', '10-01']:
                dates_to_check.append(f"{year}-{month}")
        
        print(f"  Checking {len(dates_to_check)} dates (quarterly sampling)")
        
        # CHECK BOTH CHARTS for each artist
        all_artist_data = []
        
        for chart_name in ['hot-100', 'billboard-200']:
            print(f"  Scraping {chart_name}...")
            
            chart_data = []
            dates_processed = 0
            
            for date in dates_to_check:
                try:
                    chart = billboard.ChartData(chart_name, date=date)
                    
                    # Search for artist (flexible matching)
                    for entry in chart:
                        entry_artist_lower = entry.artist.lower()
                        artist_lower = artist.lower()
                        
                        # Match if artist name appears anywhere in chart artist
                        if artist_lower in entry_artist_lower or entry_artist_lower in artist_lower:
                            chart_data.append({
                                'artist': artist,
                                'chart_date': date,
                                'year': int(date[:4]),
                                'quarter': (int(date[5:7]) - 1) // 3 + 1,
                                'chart_name': chart_name,
                                'rank': entry.rank,
                                'title': entry.title,
                                'chart_artist': entry.artist,
                                'peak_position': entry.peakPos,
                                'weeks_on_chart': entry.weeks,
                                'grammy_years': str(grammy_years)
                            })
                    
                    time.sleep(0.5)  # Be respectful
                    
                except Exception as e:
                    # Chart might not exist for that date
                    pass
                
                # Progress update every 20 dates
                dates_processed += 1
                if dates_processed % 20 == 0:
                    percent = int((dates_processed / len(dates_to_check)) * 100)
                    print(f"    Progress: {dates_processed}/{len(dates_to_check)} dates ({percent}%)")
            
            if len(chart_data) > 0:
                print(f"    ✓ Found {len(chart_data)} entries on {chart_name}")
                all_artist_data.extend(chart_data)
            else:
                print(f"    - No entries on {chart_name}")
        
        # Save this artist's data (both charts combined)
        if len(all_artist_data) > 0:
            df = pd.DataFrame(all_artist_data)
            filename = artist.replace('/', '-').replace('&', 'and')[:50] + '.csv'
            filepath = os.path.join(output_dir, filename)
            df.to_csv(filepath, index=False)
            print(f"  ✓ Saved {len(all_artist_data)} total entries")
        else:
            # Save empty file to mark as processed
            pd.DataFrame().to_csv(os.path.join(output_dir, filename), index=False)
            print(f"  ✗ No chart data found (saved empty file to skip in future)")
    
    print("\n" + "="*60)
    print("SESSION COMPLETE")
    print(f"Processed: {min(artists_per_session, len(remaining_artists))} artists")
    print(f"Remaining: {max(0, len(remaining_artists) - artists_per_session)} artists")
    print("="*60)
    
    # Combine all scraped files
    combine_bna_files(output_dir)


def combine_bna_files(output_dir='data/raw/billboard_bna'):
    """Combine all BNA artist CSV files into one"""
    
    csv_files = [f for f in os.listdir(output_dir) if f.endswith('.csv')]
    
    if len(csv_files) == 0:
        print("No files to combine yet")
        return
    
    print(f"\nCombining {len(csv_files)} BNA artist files...")
    
    all_data = []
    for f in csv_files:
        df = pd.read_csv(os.path.join(output_dir, f))
        if len(df) > 0:  # Skip empty files
            all_data.append(df)
    
    if len(all_data) == 0:
        print("No data to combine")
        return
    
    combined = pd.concat(all_data, ignore_index=True)
    
    # Save combined file
    output_path = 'data/processed/billboard_bna_quarterly.csv'
    combined.to_csv(output_path, index=False)
    
    print(f"✓ Combined file saved: {output_path}")
    print(f"  Total entries: {len(combined)}")
    print(f"  Unique artists: {combined['artist'].nunique()}")
    print(f"  Artists with #1 hits: {len(combined[combined['rank'] == 1]['artist'].unique())}")
    print(f"  Date range: {combined['chart_date'].min()} to {combined['chart_date'].max()}")
    
    return combined


if __name__ == "__main__":
    # Scrape Best New Artist winners with QUARTERLY sampling
    # 66 total BNA winners, 10 artists per session
    # Estimated time per session: ~15 hours
    # Need 7 sessions total to complete all 66 artists
    
    scrape_bna_quarterly(
        grammy_csv_path='data/processed/grammy_data_clean.csv',
        output_dir='data/raw/billboard_bna',
        artists_per_session=10  # 10 artists per session
    )
