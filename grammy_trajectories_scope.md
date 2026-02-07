# Grammy Career Trajectories — Project Scope

**Project Name:** Grammy Career Trajectories  
**Tagline:** "Does winning a Grammy predict long-term success?"  
**Timeline:** 3 weeks  
**Status:** Planning  
**Owner:** [Your Name]  
**Part of:** moonpath.dev portfolio

---

## Overview

### One-Line Description
A data analysis project examining the correlation between Grammy Award wins and modern streaming success across 60+ years of music industry history.

### Longer Description
The Grammy Awards are often criticized for being out of touch with popular taste and cultural relevance. But is there data to support this critique? This project cross-references decades of Grammy nominees and winners with current streaming metrics to answer a simple question: **Does winning a Grammy predict long-term career success, or is it just a moment in time?**

By analyzing Best New Artist outcomes, Album of the Year correlations, and identifying "Grammy Paradoxes" (artists who succeeded without awards vs. winners who faded), this project brings quantitative rigor to a debate usually dominated by opinion.

The result is a public-facing website with interactive visualizations, key findings, and transparent methodology — designed to showcase both technical skill (data pipeline engineering, API integration, statistical analysis) and analytical thinking (asking the right questions, interpreting patterns, acknowledging limitations).

### Problem Statement
The Grammy Awards have crowned "best" artists for over 60 years, but there's little systematic analysis of whether winners actually sustain careers better than nominees. Music critics and fans debate this constantly, but the conversation lacks data. This project fills that gap.

### Target Audience
- **Primary:** Hiring managers and recruiters evaluating my technical + analytical capabilities
- **Secondary:** Music fans, data enthusiasts, cultural critics interested in award show dynamics
- **Tertiary:** Future clients for moonpath concierge analytics services (proof-of-concept)

---

## Goals & Success Metrics

### Primary Goals
1. **Technical:** Build a robust multi-source data pipeline (web scraping + API integration)
2. **Analytical:** Identify statistically significant patterns in Grammy outcomes vs. streaming success
3. **Portfolio:** Create a polished, public-facing project that demonstrates both technical and storytelling skills

### Success Criteria
- Live website with at least 5 key findings supported by data
- Clean, well-documented GitHub repository with reproducible code
- LinkedIn post with 500+ views and positive engagement
- At least 3 insights I didn't expect when I started (evidence of genuine discovery)
- Portfolio-ready case study I can discuss in interviews

### Non-Goals (Scope Boundaries)
- ❌ Predictive modeling or machine learning (this is descriptive analysis, not forecasting)
- ❌ Social features or user-generated content (static research project, not a platform)
- ❌ Real-time data updates (a snapshot in time is sufficient)
- ❌ Comprehensive music industry analysis (focused on Grammys specifically)
- ❌ Subjective quality judgments (letting the data speak, not editorializing about "deserving" winners)

---

## Technical Scope

### Tech Stack

**Data Collection:**
- Python 3.10+
- `beautifulsoup4` — Web scraping Wikipedia Grammy tables
- `requests` — HTTP requests
- `spotipy` — Spotify API wrapper
- `python-dotenv` — Environment variable management

**Data Analysis:**
- `pandas` — Data manipulation and analysis
- `numpy` — Numerical computations
- Jupyter Notebook — Exploratory analysis

**Visualization:**
- `matplotlib` or `plotly` — Chart generation
- Consider `seaborn` for statistical visualizations

**Presentation:**
- Astro or 11ty — Static site generator (TBD based on learning curve)
- Or simple HTML/CSS/JS if SSGs feel like overkill
- Hosted on Netlify or GitHub Pages (free tier)

**Version Control:**
- Git + GitHub (public repository)

### Data Sources

| Source | What It Provides | Access Method | Constraints |
|--------|------------------|---------------|-------------|
| Wikipedia | Grammy nominees & winners (1959–2024) by category | Web scraping (BeautifulSoup) | Page structure changes could break scraper |
| Spotify API | Monthly listeners, follower counts | Official API (OAuth) | Rate limits, no total stream counts available |
| Wikipedia Pageviews API | Cultural relevance proxy | REST API | Optional — only if time permits |

### Architecture Overview

```
Data Pipeline:
1. Scrape Grammy data → Raw CSV
2. Fetch Spotify metrics → Raw JSON
3. Normalize artist names → Processed CSV
4. Merge datasets → Analysis-ready dataset
5. Run analyses → Insights + visualizations
6. Build static site → Public output
```

**File Structure:**
```
grammy-trajectories/
├── data/
│   ├── raw/              # Unprocessed scraped/API data
│   ├── processed/        # Cleaned, normalized data
│   └── final/            # Analysis-ready merged datasets
├── scripts/
│   ├── 01_scrape_grammys.py
│   ├── 02_fetch_spotify.py
│   ├── 03_normalize_data.py
│   └── config.py
├── notebooks/
│   └── exploratory_analysis.ipynb
├── site/                 # Static site files
├── .env                  # API keys (gitignored)
├── requirements.txt
└── README.md
```

### Key Technical Challenges

1. **Artist Name Normalization**
   - Problem: "Beyoncé" vs "Beyonce" vs "Beyoncé Knowles" vs "Beyoncé Knowles-Carter"
   - Solution: Fuzzy matching + manual QA for edge cases

2. **Spotify API Rate Limits**
   - Problem: Limited requests per minute
   - Solution: Implement rate limiting in code, cache results

3. **Wikipedia Table Inconsistency**
   - Problem: Grammy pages have different structures across decades
   - Solution: Write flexible scraper with fallback logic, validate manually

4. **Defining "Success"**
   - Problem: Streaming numbers favor recent artists; older Grammy winners may not be on Spotify
   - Solution: Acknowledge bias, focus on relative comparisons within eras

---

## Feature Breakdown

### Must-Haves (MVP)

**Core Analyses:**
- [ ] Best New Artist outcome analysis (winners vs. nominees, who stayed relevant?)
- [ ] Album of the Year streaming correlation (do AOTY winners have higher streams?)
- [ ] "Grammy Paradox" identification (0 wins + high streams vs. multiple wins + low streams)
- [ ] Basic visualizations for each finding (bar charts, scatterplots, trend lines)

**Technical Infrastructure:**
- [ ] Grammy data scraper (at minimum: Best New Artist, Album of the Year)
- [ ] Spotify API integration with rate limiting
- [ ] Artist name matching logic
- [ ] Merged, analysis-ready dataset

**Presentation:**
- [ ] Static website with findings
- [ ] Methodology section (transparent about data sources and limitations)
- [ ] GitHub repo with clean code + README
- [ ] LinkedIn post summarizing key insights

### Nice-to-Haves (If Time Permits)

- [ ] Genre breakdown over time (has genre bias changed?)
- [ ] Decade-by-decade trend analysis (is the Grammy's predictive power shifting?)
- [ ] Record of the Year and Song of the Year analysis (expand beyond BNA and AOTY)
- [ ] Wikipedia pageview data integration (cultural relevance metric)
- [ ] Interactive charts (Plotly instead of static images)

### Future Roadmap (Post-Launch v2+)

- Expand to other award shows (Oscars, Emmys, Golden Globes)
- Automate annual data refresh (track new Grammy winners over time)
- "Check Your Taste" feature (users input favorite artists, see their Grammy history)
- Predictive modeling (can we forecast who will win based on historical patterns?)
- Cross-platform analysis (Apple Music, YouTube, TikTok metrics)

---

## Timeline & Phases

### Week 1: Data Collection & Pipeline
**Goal:** Clean, merged dataset ready for analysis

**Tasks:**
- Set up project repo, install dependencies, configure Spotify API
- Build Grammy scraper (Wikipedia → CSV)
- Build Spotify fetcher (API → JSON)
- Normalize artist names and merge datasets
- Validate data quality (spot-check for errors)

**Deliverable:** `final/grammy_spotify_merged.csv`

---

### Week 2: Analysis & Insights
**Goal:** Run analyses, generate visualizations, document findings

**Tasks:**
- Best New Artist outcome analysis
- Album of the Year correlation study
- Grammy Paradox identification
- Create charts and visualizations
- Document key findings in bullet points (for LinkedIn post)

**Deliverable:** Jupyter notebook with all analyses + visualizations

---

### Week 3: Presentation & Launch
**Goal:** Public-facing website, GitHub repo, LinkedIn post

**Tasks:**
- Choose static site framework and set up structure
- Design landing page with moonpath visual identity
- Build findings sections with embedded visualizations
- Write methodology section
- Deploy site to Netlify/GitHub Pages
- Polish GitHub README
- Draft and publish LinkedIn post
- Update moonpath.dev portfolio with project link

**Deliverable:** Live site URL + public announcement

---

### Milestones

| Milestone | Date | Status |
|-----------|------|--------|
| Project kickoff, repo setup | Week 1, Day 1 | Not started |
| Grammy data scraped | Week 1, Day 3 | Not started |
| Spotify data fetched | Week 1, Day 5 | Not started |
| Merged dataset complete | Week 1, Day 5 | Not started |
| Core analyses done | Week 2, Day 3 | Not started |
| Visualizations complete | Week 2, Day 5 | Not started |
| Site deployed | Week 3, Day 4 | Not started |
| Public launch | Week 3, Day 5 | Not started |

---

## Constraints & Risks

### Technical Constraints

**Spotify API Limitations:**
- No access to total lifetime stream counts (only monthly listeners)
- Rate limits could slow data collection
- Not all Grammy nominees are on Spotify (especially older artists)

**Data Quality:**
- Wikipedia tables are inconsistently formatted across decades
- Artist name matching will never be 100% accurate
- Some artists have changed names, collaborated, or disbanded

**Hosting:**
- Free tier hosting (Netlify/GitHub Pages) has bandwidth limits
- No backend server = all data processing happens in advance

### Time Constraints
- 3-week deadline is ambitious for a solo project
- May need to cut "nice-to-haves" to hit launch date
- Learning new tools (static site generators) could add time

### Known Risks

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Wikipedia changes page structure, scraper breaks | High | Medium | Build flexible scraper with fallback logic; validate manually |
| Spotify API rate limits slow data collection | Medium | High | Implement caching and rate limiting in code |
| Artist name matching produces too many errors | Medium | Medium | Start with manual QA on small dataset; refine logic iteratively |
| Static site framework learning curve eats time | Low | Medium | Fall back to simple HTML/CSS if needed |
| Findings aren't interesting enough | High | Low | Start with exploratory analysis to validate hypotheses early |

---

## Deliverables

### Public Outputs
1. **Live Website**
   - URL: TBD (likely `grammy-trajectories.moonpath.dev` or similar)
   - Content: Findings, visualizations, methodology
   - Branding: moonpath visual identity

2. **GitHub Repository**
   - URL: `github.com/[username]/grammy-trajectories`
   - Includes: Full code, documentation, datasets (if shareable)
   - README: Professional, portfolio-ready

3. **LinkedIn Post**
   - Summary of key findings
   - Link to site and repo
   - Target: 500+ views

### Portfolio Artifacts
- **Project write-up** for moonpath.dev (200–300 words)
- **Case study slide deck** (5–10 slides for interviews)
- **Resume bullet point** highlighting technical + analytical skills
- **Demo video** (optional, if helpful for interviews)

### Documentation
- Methodology notes (transparent about data sources, limitations)
- Code comments (every script heavily documented)
- Data dictionary (explaining all columns in final datasets)

---

## Design & Brand

### Visual Identity (moonpath)
**Colors:**
- Ash Grey (primary background)
- Silver (secondary/accents)
- Mauve Shadow (highlights)
- Vintage Grape (CTAs, emphasis)

**Typography:**
- Sans-serif, clean, readable
- Emphasis on data legibility over decorative fonts

**Aesthetic:**
- Minimal, scientific, calm
- Data-first (charts are the hero)
- Flat, geometric (no shadows or gradients)

### Tone & Voice
**Analytical but accessible:**
- No jargon without explanation
- Assume audience is smart but not specialists

**Skeptical but not cynical:**
- Acknowledge Grammy criticisms without dismissing the awards entirely
- Let data speak, don't editorialize

**Data-driven but human:**
- Use storytelling to make findings memorable
- Acknowledge limitations and biases openly

### UX Principles
- **Clarity over cleverness** (don't hide findings behind interactions)
- **Progressive disclosure** (start with high-level insights, allow deep dives)
- **Transparency** (methodology always accessible, never hidden)

---

## Ethical Considerations

### Data Privacy
- No personal data collected (all public sources)
- No tracking/analytics on site (or minimal, privacy-respecting analytics)

### Transparency
- Cite all data sources clearly
- Acknowledge limitations:
  - Spotify data favors recent artists
  - Artist name matching is imperfect
  - "Success" is narrowly defined (commercial metrics, not artistic impact)
- Don't overstate findings (correlation ≠ causation)

### Bias Awareness
**Systemic biases to acknowledge:**
- Grammys have historically underrepresented certain genres (hip-hop, electronic, non-English)
- Streaming platforms favor certain demographics and regions
- "Success" definition excludes non-commercial artistic impact

**Mitigation:**
- Call out these biases in methodology section
- Frame findings as "patterns in commercial success," not "artistic merit"
- Avoid making normative claims about who "deserved" to win

### Responsible AI Use
- No AI used for analysis (all statistical methods are transparent)
- If using LLMs for copywriting, disclose this
- No "AI-generated insights" that obscure human interpretation

---

## Maintenance & Longevity

### Post-Launch Plan
**Static snapshot approach:**
- This is a point-in-time analysis, not a living dashboard
- No ongoing maintenance required after launch
- Could refresh annually if I want to track new Grammy winners (but not required)

### Data Freshness
- Grammy data: Complete through 2024 awards
- Spotify data: Snapshot as of [scraping date]
- No automatic updates (would require backend server or scheduled scripts)

### Code Sustainability
- All code heavily commented for future me (or others)
- Modular design allows swapping data sources if needed
- Could hand off to another developer or revisit in 6+ months without confusion

### Archival Plan
- GitHub repo remains public indefinitely
- Site hosted on free tier (no ongoing costs)
- If I move on from moonpath, project can stand alone as portfolio piece

---

## Success Reflection (Post-Launch)

*To be filled in after Week 3:*

**What worked well:**
- 

**What was harder than expected:**
- 

**Key learnings:**
- 

**Would I do differently next time:**
- 

**Impact on portfolio/career:**
- 

---

## Appendix: Key Questions This Project Answers

1. Do Best New Artist Grammy winners sustain careers better than nominees?
2. Is there a correlation between Album of the Year wins and streaming success?
3. Which artists had massive streaming success without Grammy recognition?
4. Which Grammy winners have faded from cultural relevance?
5. Has the Grammy's predictive power changed over time (by decade)?
6. Are there genre patterns in Grammy outcomes vs. streaming success?

---

**Last Updated:** [Date]  
**Next Review:** End of Week 1 (validate scope based on progress)