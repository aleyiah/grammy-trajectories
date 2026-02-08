"""
Incremental Billboard Scraper - Saves progress as it goes
Can be stopped and resumed without losing data
"""

import billboard
import pandas as pd
import time
import os
from datetime import datetime

def scrape_billboard_incremental(grammy_csv_path='data/processed/grammy_data_clean.csv',
                                  output_dir='data/raw/billboard',
                                  winners_only=True,
                                  artists_per_session=10,
                                  sample_frequency='yearly'):
    """
    Scrape Billboard data incrementally, saving after each artist
    
    Args:
        grammy_csv_path: Path to Grammy data
        output_dir: Directory to save individual artist files
        winners_only: Only scrape Grammy winners
        artists_per_session: How many artists to process (set low to avoid timeout)
        sample_frequency: 'yearly' recommended for speed
    """
    
    print("="*60)
    print("INCREMENTAL BILLBOARD SCRAPER")
    print("="*60)
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Load Grammy data
    grammy_df = pd.read_csv(grammy_csv_path)
    
    if winners_only:
        grammy_df = grammy_df[grammy_df['is_winner'] == True]
    
    artists = grammy_df['artist'].unique()
    print(f"\nTotal artists to process: {len(artists)}")
    
    # Check which artists already scraped
    existing_files = os.listdir(output_dir) if os.path.exists(output_dir) else []
    scraped_artists = [f.replace('.csv', '').replace('_', ' ') for f in existing_files if f.endswith('.csv')]
    
    remaining_artists = [a for a in artists if a not in scraped_artists]
    
    print(f"Already scraped: {len(scraped_artists)}")
    print(f"Remaining: {len(remaining_artists)}")
    print(f"\nThis session will process: {min(artists_per_session, len(remaining_artists))} artists")
    
    # Process artists
    for i, artist in enumerate(remaining_artists[:artists_per_session], 1):
        print(f"\n[{i}/{min(artists_per_session, len(remaining_artists))}] {artist}")
        
        # Get Grammy years for this artist
        grammy_years = grammy_df[(grammy_df['artist'] == artist) & 
                                 (grammy_df['is_winner'] == True)]['year'].tolist()
        
        print(f"  Grammy wins: {grammy_years}")
        
        # Determine years to check: 5 before first win, 10 after last win
        if not grammy_years:
            print(f"  ✗ No Grammy data found, skipping")
            continue
        
        min_grammy_year = min(grammy_years)
        max_grammy_year = max(grammy_years)
        
        start_year = max(1959, min_grammy_year - 5)  # 5 years before first win
        end_year = min(2026, max_grammy_year + 10)   # 10 years after last win
        
        # Sample strategically: yearly around wins, every 2 years for rest
        years_to_check = set()
        
        # Yearly samples around each Grammy win (±2 years)
        for grammy_year in grammy_years:
            for offset in range(-2, 3):  # 2 before, year of, 2 after
                year = grammy_year + offset
                if start_year <= year <= end_year:
                    years_to_check.add(year)
        
        # Every 2 years for the rest of the period (less dense but still comprehensive)
        for year in range(start_year, end_year + 1, 2):
            years_to_check.add(year)
        
        years_to_check = sorted(years_to_check)
        print(f"  Time window: {start_year}-{end_year} ({end_year - start_year + 1} year span)")
        print(f"  Sampling {len(years_to_check)} years")
        
        # CHECK BOTH CHARTS for each artist
        all_artist_data = []
        
        for chart_name in ['hot-100', 'billboard-200']:
            print(f"  Scraping {chart_name}...")
            
            chart_data = []
            
            for year in years_to_check:
                date = f"{year}-07-01"  # Mid-year sample
                
                try:
                    chart = billboard.ChartData(chart_name, date=date)
                    
                    # Search for artist
                    for entry in chart:
                        if artist.lower() in entry.artist.lower() or entry.artist.lower() in artist.lower():
                            chart_data.append({
                                'artist': artist,
                                'chart_date': date,
                                'year': year,
                                'chart_name': chart_name,
                                'rank': entry.rank,
                                'title': entry.title,
                                'chart_artist': entry.artist,
                                'peak_position': entry.peakPos,
                                'weeks_on_chart': entry.weeks,
                                'grammy_years': str(grammy_years)
                            })
                    
                    time.sleep(0.5)  # Be nice to Billboard
                    
                except Exception as e:
                    # Silently continue - chart might not exist for that year
                    continue
            
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
            print(f"  ✓ Saved {len(all_artist_data)} total entries to {filename}")
        else:
            print(f"  ✗ No chart data found on either chart")
    
    print("\n" + "="*60)
    print("SESSION COMPLETE")
    print(f"Processed: {min(artists_per_session, len(remaining_artists))} artists")
    print(f"Remaining: {max(0, len(remaining_artists) - artists_per_session)} artists")
    print("="*60)
    
    # Combine all scraped files
    combine_billboard_files(output_dir)


def combine_billboard_files(output_dir='data/raw/billboard'):
    """Combine all individual artist CSV files into one"""
    
    csv_files = [f for f in os.listdir(output_dir) if f.endswith('.csv')]
    
    if len(csv_files) == 0:
        print("No files to combine yet")
        return
    
    print(f"\nCombining {len(csv_files)} artist files...")
    
    all_data = []
    for f in csv_files:
        df = pd.read_csv(os.path.join(output_dir, f))
        all_data.append(df)
    
    combined = pd.concat(all_data, ignore_index=True)
    
    # Save combined file
    output_path = 'data/processed/billboard_grammy_combined.csv'
    combined.to_csv(output_path, index=False)
    
    print(f"✓ Combined file saved: {output_path}")
    print(f"  Total entries: {len(combined)}")
    print(f"  Unique artists: {combined['artist'].nunique()}")
    print(f"  Artists with #1 hits: {len(combined[combined['rank'] == 1]['artist'].unique())}")
    
    return combined


if __name__ == "__main__":
    # Run scraper - process 50 artists per session
    # Should take ~1.5-2 hours per session
    # Need ~4 sessions to complete all 201 winners
    
    scrape_billboard_incremental(
        grammy_csv_path='data/processed/grammy_data_clean.csv',
        output_dir='data/raw/billboard',
        winners_only=True,
        artists_per_session=50,  # Process 50 at a time
        sample_frequency='yearly'  # Fastest option
    )
