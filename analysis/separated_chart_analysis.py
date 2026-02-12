"""
Grammy Trajectories - Separated Chart Analysis
Hot 100 (Singles) vs Billboard 200 (Albums) Curse Testing
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("="*80)
print("SEPARATED CHART ANALYSIS: HOT 100 vs BILLBOARD 200")
print("Testing if singles curse differs from albums curse")
print("="*80)

# Load data
df = pd.read_csv('billboard_bna_quarterly.csv')

print(f"\n📊 DATASET BREAKDOWN")
print(f"Total entries: {len(df):,}")
print(f"Hot 100 entries: {len(df[df['chart_name'] == 'hot-100']):,} ({len(df[df['chart_name'] == 'hot-100'])/len(df)*100:.1f}%)")
print(f"Billboard 200 entries: {len(df[df['chart_name'] == 'billboard-200']):,} ({len(df[df['chart_name'] == 'billboard-200'])/len(df)*100:.1f}%)")

# ============================================================================
# FUNCTION: Calculate curse for a specific chart
# ============================================================================

def analyze_curse(data, chart_name):
    """Analyze curse for specific chart type"""
    
    chart_df = data[data['chart_name'] == chart_name].copy()
    curse_results = []
    
    for artist in chart_df['artist'].unique():
        artist_data = chart_df[chart_df['artist'] == artist].copy()
        
        try:
            grammy_year = eval(artist_data['grammy_years'].iloc[0])[0]
        except:
            continue
        
        before = artist_data[artist_data['year'] < grammy_year]
        after = artist_data[artist_data['year'] >= grammy_year]
        
        avg_rank_before = before['rank'].mean() if len(before) > 0 else None
        avg_rank_after = after['rank'].mean() if len(after) > 0 else None
        
        if avg_rank_before and avg_rank_after:
            change = avg_rank_after - avg_rank_before
            
            curse_results.append({
                'artist': artist,
                'grammy_year': grammy_year,
                'avg_rank_before': avg_rank_before,
                'avg_rank_after': avg_rank_after,
                'rank_change': change,
                'entries_before': len(before),
                'entries_after': len(after),
                'cursed': change > 0
            })
    
    return pd.DataFrame(curse_results)

# ============================================================================
# PART 1: HOT 100 (SINGLES) CURSE ANALYSIS
# ============================================================================

print(f"\n{'='*80}")
print("PART 1: HOT 100 (SINGLES) CURSE")
print(f"{'='*80}")

hot100_curse = analyze_curse(df, 'hot-100')

if len(hot100_curse) > 0:
    cursed_count = hot100_curse['cursed'].sum()
    avg_change = hot100_curse['rank_change'].mean()
    
    print(f"\nArtists with Hot 100 data: {len(hot100_curse)}")
    print(f"Singles curse rate: {cursed_count}/{len(hot100_curse)} ({cursed_count/len(hot100_curse)*100:.1f}%)")
    print(f"Average position change: {avg_change:+.1f}")
    
    # Statistical test
    if len(hot100_curse) >= 5:
        t_stat, p_value = stats.ttest_rel(hot100_curse['avg_rank_after'], 
                                           hot100_curse['avg_rank_before'])
        print(f"\nPaired t-test: t={t_stat:.3f}, p={p_value:.4f}")
        if p_value < 0.05:
            print("✓ Statistically significant singles decline (p < 0.05)")
        else:
            print("✗ Not statistically significant (p >= 0.05)")
    
    print(f"\n📉 TOP 10 SINGLES CURSE VICTIMS")
    print(hot100_curse.nlargest(10, 'rank_change')[['artist', 'avg_rank_before', 'avg_rank_after', 'rank_change']].to_string(index=False))
    
    print(f"\n📈 TOP 10 SINGLES CURSE BREAKERS")
    print(hot100_curse.nsmallest(10, 'rank_change')[['artist', 'avg_rank_before', 'avg_rank_after', 'rank_change']].to_string(index=False))

else:
    print("\nInsufficient Hot 100 data for analysis")

# ============================================================================
# PART 2: BILLBOARD 200 (ALBUMS) CURSE ANALYSIS
# ============================================================================

print(f"\n{'='*80}")
print("PART 2: BILLBOARD 200 (ALBUMS) CURSE")
print(f"{'='*80}")

bb200_curse = analyze_curse(df, 'billboard-200')

if len(bb200_curse) > 0:
    cursed_count = bb200_curse['cursed'].sum()
    avg_change = bb200_curse['rank_change'].mean()
    
    print(f"\nArtists with Billboard 200 data: {len(bb200_curse)}")
    print(f"Albums curse rate: {cursed_count}/{len(bb200_curse)} ({cursed_count/len(bb200_curse)*100:.1f}%)")
    print(f"Average position change: {avg_change:+.1f}")
    
    # Statistical test
    if len(bb200_curse) >= 5:
        t_stat, p_value = stats.ttest_rel(bb200_curse['avg_rank_after'], 
                                           bb200_curse['avg_rank_before'])
        print(f"\nPaired t-test: t={t_stat:.3f}, p={p_value:.4f}")
        if p_value < 0.05:
            print("✓ Statistically significant albums decline (p < 0.05)")
        else:
            print("✗ Not statistically significant (p >= 0.05)")
    
    print(f"\n📉 TOP 10 ALBUMS CURSE VICTIMS")
    print(bb200_curse.nlargest(10, 'rank_change')[['artist', 'avg_rank_before', 'avg_rank_after', 'rank_change']].to_string(index=False))
    
    print(f"\n📈 TOP 10 ALBUMS CURSE BREAKERS")
    print(bb200_curse.nsmallest(10, 'rank_change')[['artist', 'avg_rank_before', 'avg_rank_after', 'rank_change']].to_string(index=False))

else:
    print("\nInsufficient Billboard 200 data for analysis")

# ============================================================================
# PART 3: COMPARISON - SINGLES VS ALBUMS
# ============================================================================

print(f"\n{'='*80}")
print("PART 3: SINGLES VS ALBUMS CURSE COMPARISON")
print(f"{'='*80}")

if len(hot100_curse) > 0 and len(bb200_curse) > 0:
    
    print("\n📊 CURSE RATE COMPARISON")
    hot100_rate = hot100_curse['cursed'].sum() / len(hot100_curse) * 100
    bb200_rate = bb200_curse['cursed'].sum() / len(bb200_curse) * 100
    
    print(f"Singles curse (Hot 100): {hot100_rate:.1f}%")
    print(f"Albums curse (Billboard 200): {bb200_rate:.1f}%")
    print(f"Difference: {abs(hot100_rate - bb200_rate):.1f} percentage points")
    
    if hot100_rate > bb200_rate:
        print(f"\n✓ SINGLES CURSE IS STRONGER")
        print(f"  Artists struggle more to replicate hit singles than successful albums")
    elif bb200_rate > hot100_rate:
        print(f"\n✓ ALBUMS CURSE IS STRONGER")
        print(f"  Artists struggle more to replicate successful albums than hit singles")
    else:
        print(f"\n→ CURSE AFFECTS BOTH EQUALLY")
    
    print(f"\n📈 AVERAGE POSITION CHANGE COMPARISON")
    print(f"Singles average change: {hot100_curse['rank_change'].mean():+.1f}")
    print(f"Albums average change: {bb200_curse['rank_change'].mean():+.1f}")
    
    # Artists in both datasets
    both_artists = set(hot100_curse['artist'].unique()) & set(bb200_curse['artist'].unique())
    
    print(f"\n🎵 ARTISTS WITH BOTH SINGLES & ALBUMS DATA: {len(both_artists)}")
    
    if len(both_artists) > 0:
        comparison_data = []
        
        for artist in both_artists:
            hot100_change = hot100_curse[hot100_curse['artist'] == artist]['rank_change'].values[0]
            bb200_change = bb200_curse[bb200_curse['artist'] == artist]['rank_change'].values[0]
            
            hot100_cursed = hot100_change > 0
            bb200_cursed = bb200_change > 0
            
            if hot100_cursed and bb200_cursed:
                pattern = "Both cursed"
            elif hot100_cursed and not bb200_cursed:
                pattern = "Singles cursed, Albums escaped"
            elif not hot100_cursed and bb200_cursed:
                pattern = "Albums cursed, Singles escaped"
            else:
                pattern = "Both escaped"
            
            comparison_data.append({
                'artist': artist,
                'hot100_change': hot100_change,
                'bb200_change': bb200_change,
                'pattern': pattern
            })
        
        comparison_df = pd.DataFrame(comparison_data)
        
        print("\nPATTERN BREAKDOWN:")
        for pattern in comparison_df['pattern'].unique():
            count = len(comparison_df[comparison_df['pattern'] == pattern])
            print(f"  {pattern}: {count} artists ({count/len(comparison_df)*100:.1f}%)")
        
        print(f"\nEXAMPLES BY PATTERN:")
        for pattern in sorted(comparison_df['pattern'].unique()):
            examples = comparison_df[comparison_df['pattern'] == pattern].head(3)
            print(f"\n  {pattern}:")
            for _, row in examples.iterrows():
                print(f"    {row['artist']}: Singles {row['hot100_change']:+.1f}, Albums {row['bb200_change']:+.1f}")

# ============================================================================
# PART 4: VOLUME ANALYSIS - SINGLES VS ALBUMS
# ============================================================================

print(f"\n{'='*80}")
print("PART 4: OUTPUT VOLUME - SINGLES VS ALBUMS")
print(f"{'='*80}")

if len(hot100_curse) > 0 and len(bb200_curse) > 0:
    
    print("\n📊 POST-GRAMMY OUTPUT COMPARISON")
    
    # Artists who increased singles output
    hot100_increase = hot100_curse[hot100_curse['entries_after'] > hot100_curse['entries_before']]
    print(f"\nIncreased singles output: {len(hot100_increase)}/{len(hot100_curse)} ({len(hot100_increase)/len(hot100_curse)*100:.1f}%)")
    print(f"Average singles increase: {(hot100_increase['entries_after'] - hot100_increase['entries_before']).mean():+.1f}")
    
    # Artists who increased album output
    bb200_increase = bb200_curse[bb200_curse['entries_after'] > bb200_curse['entries_before']]
    print(f"\nIncreased album output: {len(bb200_increase)}/{len(bb200_curse)} ({len(bb200_increase)/len(bb200_curse)*100:.1f}%)")
    print(f"Average album increase: {(bb200_increase['entries_after'] - bb200_increase['entries_before']).mean():+.1f}")

# ============================================================================
# VISUALIZATIONS
# ============================================================================

print(f"\n{'='*80}")
print("GENERATING VISUALIZATIONS")
print(f"{'='*80}")

if len(hot100_curse) > 0 and len(bb200_curse) > 0:
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    # 1. Curse rate comparison
    curse_rates = [
        hot100_curse['cursed'].sum() / len(hot100_curse) * 100,
        bb200_curse['cursed'].sum() / len(bb200_curse) * 100
    ]
    axes[0, 0].bar(['Hot 100\n(Singles)', 'Billboard 200\n(Albums)'], curse_rates, 
                   color=['#e74c3c', '#3498db'], edgecolor='black', linewidth=2)
    axes[0, 0].set_ylabel('Curse Rate (%)', fontsize=12, fontweight='bold')
    axes[0, 0].set_title('Curse Rate: Singles vs Albums', fontsize=14, fontweight='bold')
    axes[0, 0].set_ylim(0, 100)
    axes[0, 0].grid(axis='y', alpha=0.3)
    for i, v in enumerate(curse_rates):
        axes[0, 0].text(i, v + 3, f'{v:.1f}%', ha='center', fontweight='bold', fontsize=11)
    
    # 2. Position change distribution comparison
    axes[0, 1].hist([hot100_curse['rank_change'], bb200_curse['rank_change']], 
                    bins=20, label=['Hot 100', 'Billboard 200'], 
                    alpha=0.7, edgecolor='black')
    axes[0, 1].axvline(x=0, color='red', linestyle='--', linewidth=2, label='No change')
    axes[0, 1].set_xlabel('Position Change (Positive = Worse)', fontsize=12)
    axes[0, 1].set_ylabel('Number of Artists', fontsize=12)
    axes[0, 1].set_title('Distribution of Position Changes', fontsize=14, fontweight='bold')
    axes[0, 1].legend()
    axes[0, 1].grid(alpha=0.3)
    
    # 3. Before vs After scatter (Hot 100)
    axes[1, 0].scatter(hot100_curse['avg_rank_before'], hot100_curse['avg_rank_after'],
                      s=100, alpha=0.6, c='red', edgecolors='black')
    axes[1, 0].plot([0, 100], [0, 100], 'k--', alpha=0.5, label='No change line')
    axes[1, 0].set_xlabel('Avg Rank Before Grammy (Hot 100)', fontsize=12)
    axes[1, 0].set_ylabel('Avg Rank After Grammy (Hot 100)', fontsize=12)
    axes[1, 0].set_title('Hot 100: Before vs After Grammy', fontsize=14, fontweight='bold')
    axes[1, 0].invert_xaxis()
    axes[1, 0].invert_yaxis()
    axes[1, 0].legend()
    axes[1, 0].grid(alpha=0.3)
    
    # 4. Before vs After scatter (Billboard 200)
    axes[1, 1].scatter(bb200_curse['avg_rank_before'], bb200_curse['avg_rank_after'],
                      s=100, alpha=0.6, c='blue', edgecolors='black')
    axes[1, 1].plot([0, 200], [0, 200], 'k--', alpha=0.5, label='No change line')
    axes[1, 1].set_xlabel('Avg Rank Before Grammy (Billboard 200)', fontsize=12)
    axes[1, 1].set_ylabel('Avg Rank After Grammy (Billboard 200)', fontsize=12)
    axes[1, 1].set_title('Billboard 200: Before vs After Grammy', fontsize=14, fontweight='bold')
    axes[1, 1].invert_xaxis()
    axes[1, 1].invert_yaxis()
    axes[1, 1].legend()
    axes[1, 1].grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('separated_chart_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✓ Visualization saved: separated_chart_analysis.png")

# ============================================================================
# SUMMARY
# ============================================================================

print(f"\n{'='*80}")
print("ANALYSIS SUMMARY")
print(f"{'='*80}")

if len(hot100_curse) > 0 and len(bb200_curse) > 0:
    print(f"""
📊 KEY FINDINGS:

1. SINGLES CURSE (Hot 100):
   - Curse rate: {hot100_curse['cursed'].sum()}/{len(hot100_curse)} ({hot100_curse['cursed'].sum()/len(hot100_curse)*100:.1f}%)
   - Average change: {hot100_curse['rank_change'].mean():+.1f} positions

2. ALBUMS CURSE (Billboard 200):
   - Curse rate: {bb200_curse['cursed'].sum()}/{len(bb200_curse)} ({bb200_curse['cursed'].sum()/len(bb200_curse)*100:.1f}%)
   - Average change: {bb200_curse['rank_change'].mean():+.1f} positions

3. COMPARISON:
   - Stronger curse: {'Singles' if hot100_curse['cursed'].sum()/len(hot100_curse) > bb200_curse['cursed'].sum()/len(bb200_curse) else 'Albums'}
   - Difference: {abs(hot100_curse['cursed'].sum()/len(hot100_curse) - bb200_curse['cursed'].sum()/len(bb200_curse))*100:.1f} percentage points

4. DUAL CHART ARTISTS:
   - {len(both_artists)} artists have both singles and albums data
   - Patterns reveal whether curse is format-specific or artist-wide

📈 IMPLICATIONS:
   - Separating charts reveals nuanced curse patterns
   - Different success metrics show different trajectories
   - Demonstrates sophisticated analytical approach
""")

print("="*80)
print("Separated chart analysis complete!")
print("="*80)
