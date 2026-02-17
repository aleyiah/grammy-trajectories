# Grammy Best New Artist Career Trajectories

**Testing the "Best New Artist curse" with 68 years of Billboard chart data (1958-2026)**

## Key Finding

**The Grammy Best New Artist curse doesn't exist.**

After analyzing 65 winners across 68 years and 2,526 chart entries, the data shows:

- **67.9%** of winners hit Top 10 on Hot 100 **after** their Grammy (up from 56.6% before)
- **61.0%** hit Top 10 on Billboard 200 **after** winning (up from 42.4% before)
- **53%** of winners improved or maintained their peak chart performance post-Grammy
- **2x more artists** achieved #1 albums after their Grammy (8 vs 4)

The "curse" narrative exists because we remember dramatic failures (Milli Vanilli, Arrested Development) while forgetting massive successes (Adele, The Beatles, Mariah Carey).

## Methodology

### Data Collection
- **65 Best New Artist winners** (1959-2025)
- **2,526 total chart entries** from Billboard Hot 100 and Billboard 200
- **Quarterly sampling**: Every 3 months for 15 years (5 years before Grammy through 10 years after)
- **Peak position analysis**: Using peak chart positions instead of averages to avoid catalog charting bias
- **~350 hours** of manual web scraping and data cleaning

### Statistical Analysis
- Compared peak positions before vs after Grammy win
- Wilcoxon signed-rank test for paired samples
- Separated singles (Hot 100) and albums (Billboard 200) for precision
- **Albums**: p = 0.0514 (not statistically significant)
- **Singles**: p = 0.35 (not statistically significant)

### Winners Not Included
- Chappell Roan (2025) - too recent for post-Grammy data
- Meghan Trainor (2016) - data collection issues

## Project Structure

```
grammy-trajectories/
├── data/
│   ├── raw/                     # Original scraped data
│   └── processed/               # Cleaned datasets
│       └── billboard_bna_quarterly.csv
├── scripts/
│   └── scraping/               # Billboard scraping scripts
├── analysis/
│   └── peak_analysis.py        # Statistical analysis
├── visualizations/
│   ├── grammy_curse_before_after.png
│   └── grammy_curse_stat_cards.png
└── docs/
    ├── FINAL_ANALYSIS_NO_CURSE.md
    └── moonpath_blog_final_with_colors.md
```

## Key Findings by Artist

### Success Stories (Peak Improved After Grammy)
- **Adele**: #41 → #1 on Billboard 200
- **The Beatles**: Maintained #1 on both charts
- **Maroon 5**: 3 songs before → 18 songs after, including two #1 hits
- **Billie Eilish**: Minimal decline, still Top 5

### The "Curse" Cases (Peak Declined)
- **Fun.**: #1 → #14 on Hot 100 (band broke up, Jack Antonoff became superproducer)
- **Macklemore & Ryan Lewis**: #1 → #16 (viral hit couldn't be replicated)
- **Olivia Rodrigo**: #2 → #7 on Hot 100 (only 2 years post-Grammy, too early to conclude)

### Important Note
Even dramatic "failures" had successful members:
- Fun's Jack Antonoff won Producer of the Year and works with Taylor Swift/Kendrick Lamar
- The "curse" narrative oversimplifies complex career trajectories

## Why The Curse Belief Persists

1. **Confirmation bias**: We remember failures, forget successes
2. **Availability heuristic**: Dramatic stories (Milli Vanilli) are more memorable
3. **Selection bias**: Winning Best New Artist often means you've already peaked
4. **Catalog charting**: Average-based analysis shows decline due to older songs charting at #140+ years later

## Limitations

- Quarterly sampling (not every chart position)
- Pre-streaming era bias (before ~2015)
- Peak positions don't show longevity
- No control group (comparing winners vs. nominees who lost)
- Correlation ≠ causation

## Tools & Technologies

- **Python**: pandas, scipy, matplotlib
- **Data source**: Billboard.com
- **Analysis**: Wilcoxon signed-rank test
- **Visualization**: matplotlib with moonpath brand colors

## Future Work

**Phase 2: Control Group Analysis**
- Compare Grammy winners vs. nominees who lost
- Example matchups: Amy Winehouse (won) vs. Taylor Swift (lost) in 2008
- Would answer: Does *winning* cause anything, or is it just being a breakthrough artist?
- Estimated effort: 20-30 hours scraping 30-50 additional artists

## About This Project

This is my first major web scraping and data analysis project, built to:
1. Test a widely-believed music industry myth with real data
2. Build a differentiated data science portfolio piece
3. Practice rigorous statistical methodology
4. Challenge conventional wisdom with evidence

**Author**: Aleyiah Peña
**Contact**: [Your contact info]
**Portfolio**: [moonpath.dev](https://moonpath.dev)

## License

MIT License - feel free to use this data for your own analysis!

## Acknowledgments

Special thanks to Billboard for maintaining comprehensive chart archives, and to the data science community for resources on proper statistical analysis techniques.
