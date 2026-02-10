# Grammy Career Trajectories: Testing the Best New Artist Curse

**An empirical analysis of 66 Best New Artist Grammy winners from 1960-2026**

## 🎯 Research Question

Does winning the Grammy for Best New Artist help or hurt artists' commercial success? 

The "Best New Artist curse" is a long-discussed phenomenon in the music industry, where Grammy winners allegedly experience career declines after their win. This project tests this hypothesis with 60+ years of Billboard chart data.

## 📊 Methodology

### Data Sources

1. **Grammy Awards Data**
   - Source: Wikipedia (manually scraped)
   - Coverage: Best New Artist, Album of the Year, Record of the Year (1959-2026)
   - Total records: 1,092 (201 winners, 891 nominees)
   - Collection method: BeautifulSoup HTML parsing
   - Date collected: February 2026

2. **Billboard Chart Data**
   - Source: Billboard.com via billboard.py library (v6.3.0)
   - Charts: Hot 100 (singles) + Billboard 200 (albums)
   - Sampling: Quarterly (Jan 1, Apr 1, Jul 1, Oct 1)
   - Time window: 5 years before Grammy win → 10 years after
   - Coverage: 66 Best New Artist winners
   - Collection period: February 7-12, 2026

3. **Spotify Streaming Data** (Planned)
   - Source: Spotify Web API
   - Metrics: Monthly listeners, track popularity, career streams
   - Target date: March 11, 2026 (API access approval pending)

### Sampling Strategy

**Quarterly Sampling Rationale:**
- Testing on Bobby Darin (monthly vs quarterly) showed quarterly captures 74% of unique songs
- The 26% missed were predominantly low-charting (#34-#100) brief appearances
- All major hits (#1-#25) captured in quarterly sampling
- Time trade-off: Monthly = 300 hours, Quarterly = 100 hours (3x faster)
- **Decision:** Quarterly provides sufficient data for trajectory analysis

**Time Window Rationale:**
- **5 years before Grammy:** Captures rise to Grammy-winning status, establishes baseline
- **10 years after Grammy:** Long enough to observe sustained success or decline
- Alternative considered: 30 years after (rejected due to diminishing returns, data recency for modern artists)

## 🔍 Preliminary Findings (11/66 Artists)

**9 out of 11 artists showed average chart position DECLINE after Grammy win**

### Important Nuance:

**Chart position decline ≠ career failure**

- **The Beatles:** "Declined" 23 positions but had 4x more chart appearances post-Grammy
- **The Carpenters:** "Declined" 33 positions but sustained 10-year career with #1 hit post-Grammy
- **True curse victims:** Bobbie Gentry (-110 positions), José Feliciano (short post-Grammy career)

## 🔍 Midpoint Findings (30/66 Artists - Pre-Streaming Era)

**Dataset:** 1,181 Billboard chart entries for 30 Best New Artist winners (1960-2001)

### Key Discovery: The Curse is Real BUT Misunderstood

#### Statistical Evidence
- **75% of artists (21/28) showed chart position decline** after Grammy win
- **Average position change: +15.6** (lower rank number = better position)
- **p-value: 0.0041** ← Highly statistically significant (p < 0.01)
- **Interpretation:** This is NOT random chance - the decline is real

#### The Nuance: Volume vs Quality Paradox

**64% of declining artists INCREASED chart appearances:**

| Artist | Position Change | Entry Change | Interpretation |
|--------|----------------|--------------|----------------|
| The Beatles | -22.9 positions | +89 entries | More productive, lower avg |
| Mariah Carey | -26.1 positions | +84 entries | Career explosion post-Grammy |
| The Carpenters | -33.3 positions | +47 entries | Sustained long career |

**Translation:** Artists release MORE music post-Grammy (experimentation, album cycles), naturally hitting varied chart positions. The "decline" represents **normalization**, not failure.

#### True Curse Victims: Only 1

**Milli Vanilli** - The ONLY artist with:
- ✗ Worse positions (+24.9)
- ✗ Fewer entries (-1)  
- ✗ 0 years charting post-Grammy

Only **3.6% (1/28)** fit the "true curse" definition.

#### Commercial Success Post-Grammy

- **71% of #1 hits (22/31) came AFTER winning Grammy**
- 80% still charting 5 years post-Grammy
- 33% still charting 10 years post-Grammy
- Artists: The Beatles (13 different #1s), Mariah Carey (8), America (2)

### Conclusion

The "Best New Artist curse" exists statistically but is widely misinterpreted. Winners don't fail - they **normalize**. Pre-Grammy artists receive focused promotion for breakthrough hits. Post-Grammy, increased output and experimentation naturally vary chart performance. The Grammy appears to **help** more than hurt: most #1 hits and career peaks occurred post-win.

**Next:** Complete remaining 36 artists (2002-2026, streaming era) to test if curse intensifies in modern music industry.

---


## ⚠️ Limitations & Considerations

1. **Quarterly sampling** captures ~75% of songs; may miss brief charting singles
2. **Billboard 200** only available from 1963; early artists have limited album data
3. **Era effects:** Streaming era (2010+) vs physical sales era (1960-2000s)
4. **Sample size:** 66 artists (robust but not exhaustive)

## 📈 Project Status

- ✅ Grammy data collected: 1,092 records
- 🔄 Billboard data: 31/66 artists complete
- ⏳ Spotify API: March 11, 2026

---

*Last updated: February 10, 2026*
