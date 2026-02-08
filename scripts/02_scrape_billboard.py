"""
Billboard Chart Scraper for Grammy Artists
Fetches chart performance data for Grammy winners and nominees
"""

import billboard
import pandas as pd
import time
from datetime import datetime, timedelta
import os

def get_billboard_chart(chart_name='hot-100', date=None):
    """
    Fetch a Billboard chart for a specific date
    
    Args:
        chart_name: 'hot-100' or 'billboard-200'
        date: 'YYYY-MM-DD' format, or None for current
    
    Returns:
        ChartData object or None if error
    """
    try:
        chart = billboard.ChartData(chart_name, date=date)
        return chart
    except Exception as e:
        print(f"Error fetching {chart_name} for {date}: {e}")
        return None


def search_artist_in_chart(chart, artist_name):
    """
    Find all entries for an artist in a chart
    
    Returns:
        List of matching entries
    """
    if not chart:
        return []
    
    matches = []
    artist_lower = artist_name.lower()
    
    for entry in chart:
        entry_artist = entry.artist.lower()
        
        # Handle various artist name formats
        # "Artist A & Artist B" should match "Artist A" or "Artist B"
        if (artist_lower in entry_artist or 
            entry_artist in artist_lower or
            artist_lower.replace('&', 'and') in entry_artist.replace('&', 'and')):
            
            matches.append({
                'chart_date': chart.date,
                'chart_name': chart.name,
                'rank': entry.rank,
                'title': entry.title,
                'artist': entry.artist,
                'peak_position': entry.peakPos,
                'last_week': entry.lastPos,
                'weeks_on_chart': entry.weeks,
                'is_new': entry.isNew
            })
    
    return matches


def get_artist_chart_history(artist_name, chart_name='hot-100', 
                              start_year=1959, end_year=2026, 
                              sample_frequency='quarterly'):
    """
    Get chart history for an artist across years
    
    Args:
        artist_name: Name of artist to search
        chart_name: 'hot-100' or 'billboard-200'
        start_year: First year to check
        end_year: Last year to check
        sample_frequency: 'weekly', 'monthly', 'quarterly', or 'yearly'
    
    Returns:
        DataFrame of chart entries
    """
    print(f"Fetching {chart_name} data for: {artist_name}")
    
    all_entries = []
    
    # Determine sampling dates
    if sample_frequency == 'yearly':
        dates = [f"{year}-07-01" for year in range(start_year, end_year + 1)]
    elif sample_frequency == 'quarterly':
        dates = []
        for year in range(start_year, end_year + 1):
            for month in ['01', '04', '07', '10']:
                dates.append(f"{year}-{month}-01")
    elif sample_frequency == 'monthly':
        dates = []
        for year in range(start_year, end_year + 1):
            for month in range(1, 13):
                dates.append(f"{year}-{month:02d}-01")
    else:  # weekly
        print("Warning: Weekly sampling will be very slow. Consider quarterly instead.")
        dates = []
        current = datetime(start_year, 1, 1)
        end = datetime(end_year, 12, 31)
        while current <= end:
            dates.append(current.strftime('%Y-%m-%d'))
            current += timedelta(days=7)
    
    # Fetch charts
    for i, date in enumerate(dates):
        chart = get_billboard_chart(chart_name, date)
        
        if chart:
            matches = search_artist_in_chart(chart, artist_name)
            all_entries.extend(matches)
            
            # Progress indicator
            if (i + 1) % 10 == 0:
                print(f"  Processed {i + 1}/{len(dates)} dates...")
        
        # Be respectful to Billboard servers
        time.sleep(0.5)
    
    df = pd.DataFrame(all_entries)
    
    if len(df) > 0:
        print(f"  ✓ Found {len(df)} chart entries")
    else:
        print(f"  ✗ No chart entries found")
    
    return df


def scrape_grammy_artists_billboard(grammy_csv_path, output_dir='data/raw',
                                     winners_only=False, sample_frequency='quarterly'):
    """
    Scrape Billboard data for all Grammy artists
    
    Args:
        grammy_csv_path: Path to grammy_data_clean.csv
        output_dir: Where to save results
        winners_only: If True, only scrape winners
        sample_frequency: 'yearly', 'quarterly', or 'monthly'
    """
    print("="*60)
    print("BILLBOARD CHART SCRAPER FOR GRAMMY ARTISTS")
    print("="*60)
    
    # Load Grammy data
    grammy_df = pd.read_csv(grammy_csv_path)
    print(f"\nLoaded {len(grammy_df)} Grammy records")
    
    # Filter to winners if requested
    if winners_only:
        grammy_df = grammy_df[grammy_df['is_winner'] == True]
        print(f"Filtering to {len(grammy_df)} winners only")
    
    # Get unique artists
    artists = grammy_df['artist'].unique()
    print(f"Found {len(artists)} unique artists to process\n")
    
    # Process each artist
    all_billboard_data = []
    
    for i, artist in enumerate(artists, 1):
        print(f"\n[{i}/{len(artists)}] Processing: {artist}")
        
        # Determine which chart to use based on Grammy category
        artist_categories = grammy_df[grammy_df['artist'] == artist]['category'].unique()
        
        # Check Album of the Year -> Billboard 200
        if 'Album of the Year' in artist_categories:
            chart_name = 'billboard-200'
            print(f"  Using Billboard 200 (Album of the Year nominee)")
        else:
            chart_name = 'hot-100'
            print(f"  Using Hot 100")
        
        # Get chart history
        artist_data = get_artist_chart_history(
            artist, 
            chart_name=chart_name,
            sample_frequency=sample_frequency
        )
        
        # Add artist name and Grammy info
        if len(artist_data) > 0:
            artist_data['grammy_artist'] = artist
            
            # Add Grammy win years
            grammy_years = grammy_df[(grammy_df['artist'] == artist) & 
                                     (grammy_df['is_winner'] == True)]['year'].tolist()
            artist_data['grammy_win_years'] = [grammy_years] * len(artist_data)
            
            all_billboard_data.append(artist_data)
    
    # Combine all data
    if len(all_billboard_data) > 0:
        combined_df = pd.concat(all_billboard_data, ignore_index=True)
        
        # Save to CSV
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, 'billboard_grammy_artists.csv')
        combined_df.to_csv(output_path, index=False)
        
        print("\n" + "="*60)
        print(f"✓ Scraping complete!")
        print(f"  Total chart entries: {len(combined_df)}")
        print(f"  Artists with chart data: {combined_df['grammy_artist'].nunique()}")
        print(f"  Saved to: {output_path}")
        print("="*60)
        
        return combined_df
    else:
        print("\n✗ No Billboard data found for any artist")
        return pd.DataFrame()


if __name__ == "__main__":
    # Example usage
    
    # Scrape just Grammy winners, quarterly sampling (recommended)
    billboard_data = scrape_grammy_artists_billboard(
        grammy_csv_path='data/processed/grammy_data_clean.csv',
        output_dir='data/raw',
        winners_only=True,  # Start with winners only
        sample_frequency='quarterly'  # Balance between detail and speed
    )
    
    # Show sample results
    if len(billboard_data) > 0:
        print("\nSample Billboard data:")
        print(billboard_data.head(20))
        
        print("\nTop charting Grammy winners:")
        top_artists = billboard_data[billboard_data['rank'] == 1]['grammy_artist'].value_counts().head(10)
        print(top_artists)
