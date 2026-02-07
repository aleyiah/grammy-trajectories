# Grammy Career Trajectories

**Does winning a Grammy predict long-term success?**

A data analysis project examining the correlation between Grammy Award wins and modern streaming success across 60+ years of music industry history.

![Project Status](https://img.shields.io/badge/status-in%20development-yellow)
![Python](https://img.shields.io/badge/python-3.10+-blue)

---

## 🎯 Overview

The Grammy Awards have crowned "best" artists for over six decades, but there's little systematic analysis of whether winners actually sustain careers better than nominees. This project brings quantitative rigor to that debate by cross-referencing Grammy data with current Spotify streaming metrics.

**Key Questions:**
- Do Best New Artist Grammy winners sustain careers better than nominees?
- Is there a correlation between Album of the Year wins and streaming success?
- Which artists achieved massive streaming success without Grammy recognition?
- Has the Grammy's predictive power changed over time?

---

## 📊 Data Sources

- **Grammy Awards Data**: Scraped from Wikipedia (1959–2024)
  - Categories: Best New Artist, Album of the Year, Record of the Year, Song of the Year
- **Spotify Metrics**: Monthly listeners and follower counts via Spotify API
- **Optional**: Wikipedia pageview data for cultural relevance proxy

---

## 🛠️ Tech Stack

**Data Collection:**
- Python 3.10+
- BeautifulSoup4 (web scraping)
- Spotipy (Spotify API wrapper)

**Analysis:**
- Pandas & NumPy (data manipulation)
- Jupyter Notebook (exploratory analysis)

**Visualization:**
- Matplotlib / Plotly
- Seaborn (statistical visualizations)

**Deployment:**
- Static site (Astro or 11ty)
- Hosted on Netlify or GitHub Pages

---

## 📁 Project Structure

```
grammy-trajectories/
├── data/
│   ├── raw/              # Scraped/API data (gitignored)
│   ├── processed/        # Cleaned, normalized data
│   └── final/            # Analysis-ready merged datasets
├── scripts/
│   ├── 01_scrape_grammys.py      # Grammy data scraper
│   ├── 02_fetch_spotify.py       # Spotify API integration
│   ├── 03_normalize_data.py      # Artist name matching
│   └── config.py                 # Shared configuration
├── notebooks/
│   └── exploratory_analysis.ipynb
├── site/                 # Static website files
├── .env.example          # Template for API keys
├── requirements.txt      # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- Spotify Developer account (free)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/[your-username]/grammy-trajectories.git
   cd grammy-trajectories
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API credentials:**
   - Copy `.env.example` to `.env`
   - Get Spotify API credentials from [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Add your `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET` to `.env`

### Running the Pipeline

**Step 1: Scrape Grammy Data**
```bash
python scripts/01_scrape_grammys.py
```

**Step 2: Fetch Spotify Metrics**
```bash
python scripts/02_fetch_spotify.py
```

**Step 3: Normalize and Merge Data**
```bash
python scripts/03_normalize_data.py
```

**Step 4: Run Analysis**
```bash
jupyter notebook notebooks/exploratory_analysis.ipynb
```

---

## 📈 Key Findings

*[To be updated as analysis progresses]*

---

## 🎨 Design Philosophy

This project is part of **moonpath.dev**, a creative-technical studio focused on data-driven storytelling.

**Design principles:**
- Data-first, not flashy
- Transparent about limitations
- Analytical but accessible

**Brand colors:**
- Ash Grey, Silver, Mauve Shadow, Vintage Grape

---

## 🔒 Privacy & Ethics

- All data sourced from public APIs and websites
- No personal user data collected
- Transparent methodology (all limitations documented)
- Bias awareness: Streaming metrics favor recent artists; Grammy history reflects systemic industry biases

---

## 📝 Methodology & Limitations

**Artist Name Matching:**
- Fuzzy string matching used to link Grammy nominees with Spotify artists
- Manual QA performed on edge cases
- Some mismatches inevitable (artists who changed names, collaborated, etc.)

**Streaming Data Constraints:**
- Spotify API provides monthly listeners (not total streams)
- Older Grammy winners may not be on Spotify (survivorship bias)
- Streaming success ≠ artistic merit (commercial metric only)

**Grammy Data:**
- Scraped from Wikipedia (subject to page structure changes)
- Validated against official Grammy sources where possible

---

## 🗓️ Timeline

- **Week 1**: Data collection & pipeline
- **Week 2**: Analysis & insights
- **Week 3**: Website design & deployment

---

## 🤝 Contributing

This is a solo portfolio project, but feedback is welcome! Feel free to:
- Open an issue for bugs or suggestions
- Reach out via [your contact method]

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- Grammy data sourced from Wikipedia
- Spotify metrics via Spotify Web API
- Built as part of the moonpath.dev portfolio

---

**Part of the moonpath.dev portfolio** — Creative-technical projects blending data, culture, and human insight.
