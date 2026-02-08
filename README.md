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

## ⚠️ Limitations & Considerations

1. **Quarterly sampling** captures ~75% of songs; may miss brief charting singles
2. **Billboard 200** only available from 1963; early artists have limited album data
3. **Era effects:** Streaming era (2010+) vs physical sales era (1960-2000s)
4. **Sample size:** 66 artists (robust but not exhaustive)

## 📈 Project Status

- ✅ Grammy data collected: 1,092 records
- 🔄 Billboard data: 11/66 artists complete
- ⏳ Spotify API: March 11, 2026

---

*Last updated: February 8, 2026*
