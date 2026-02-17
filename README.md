# grammy best new artist career trajectories

**testing the "best new artist curse" with 68 years of billboard chart data**

---

## the question

is winning grammy's best new artist award actually a curse?

music industry folklore says yes. people point to fun. (broke up shortly after), macklemore & ryan lewis (disappeared after their viral moment), and various one-album wonders as proof. every awards season, the same debate resurfaces: is this award a career death sentence?

i wanted to know if this was actually true or just confirmation bias.

so i spent 350 hours collecting and analyzing data on 65 best new artist winners across 68 years (1958-2026) to find out.

## the finding

**the best new artist curse doesn't exist.**

at least not in the way people think. looking at peak chart performance - the best position artists achieved before versus after their grammy win - there's no statistical evidence of a curse.

### what the data shows:

- **67.9%** of winners hit top 10 on hot 100 **after** their grammy (up from 56.6% before)
- **61.0%** hit top 10 on billboard 200 **after** winning (up from 42.4% before)
- **2x more artists** achieved #1 albums after their grammy (8 vs 4)
- **53%** improved or maintained their peak singles performance
- **58%** improved or maintained their peak album performance

most winners maintain or improve their peak chart performance after winning. the curse is folklore, not fact.

## the success stories

### adele
won best new artist in 2009. her peak before the grammy? #41 on billboard 200. after? #1. her best albums - "21" and "25" - both hit #1 and came after her grammy win.

### the beatles
won in 1965 at the height of beatlemania. maintained #1 performance on both singles and albums after winning. zero curse effect.

### maroon 5
won in 2005. before their grammy: 3 charting singles with a peak of #6. after? 18 charting singles including two #1 hits ("moves like jagger" and "one more night").

### billie eilish
showed small declines in peak position (singles: #3 → #6, albums: #3 → #4), but she's still producing top 5 albums and top 10 singles. "birds of a feather" hit #6 in 2024 and was still charting in early 2025.

## the "curse" cases

### fun.
singles peak went from #1 ("we are young") to #14 post-grammy. the band broke up - but jack antonoff, their guitarist, became one of the most dominant producers in music. he's won producer of the year multiple times and produced grammy-winning work for taylor swift, kendrick lamar, and countless others. the band failed, but its members didn't.

### macklemore & ryan lewis
had a massive cultural moment with "thrift shop" (#1 in 2013), won best new artist in 2014, then seemingly disappeared. their best post-grammy single only hit #16. they were a viral phenomenon - the kind of lightning-in-a-bottle moment that's nearly impossible to replicate.

natural career arcs. some artists peak early, some sustain, some reinvent. the grammy didn't determine which path they took.

## why the curse belief persists

we're wired to remember the dramatic failures - the scandal, the one-hit wonder, the band that broke up. the consistent successes fade into background noise, even when they outnumber the failures.

about 47% of winners on hot 100 had worse peak positions after their grammy. that means **53% maintained or improved**. more winners succeed than fail. the curse narrative focuses on the minority.

## methodology

### data collection
- **65 best new artist winners** (1960-2026)
- **2,526 billboard chart entries** from hot 100 and billboard 200
- **quarterly sampling**: 4 dates per year (jan, apr, jul, oct)
- **time window**: 5 years before grammy win → 10 years after
- **~350 hours** of web scraping and data cleaning

### why peak positions?
i wanted to know if winners could still release hit music - not whether they sustained constant visibility. a #1 album is a #1 album, whether it happens the year of the grammy or five years later.

using averages would be misleading. when an artist's old songs chart at #140+ years later (catalog charting), it drags down their average performance even though nothing changed about their actual success. peaks tell the real story.

### statistical analysis
- wilcoxon signed-rank test for paired samples
- compared peak positions before vs after grammy win
- separated singles (hot 100) and albums (billboard 200)
- **albums**: p = 0.0514 (not statistically significant)
- **singles**: p = 0.35 (not statistically significant)

no curse.

### missing artist
**samara joy** (2023 winner) is the only winner excluded from the dataset. she's never charted on hot 100 or billboard 200. she's a jazz artist - proof you can win best new artist through critical acclaim without mainstream commercial chart presence.

## what i learned (beyond the data)

### the technical journey
this was my first web scraping project. going from not knowing how to scrape to building a system that collected 2,526 data points across 65 artists was challenging. i learned python web scraping, error handling, data validation, and how to keep code running overnight without my laptop going to sleep.

### the exciting part
i woke up every morning excited to check the progress - watching the dataset grow from 10 artists to 41 to 65 felt like watching a hypothesis come to life.

### the surprising part
i genuinely expected to find evidence of a curse. the folklore is so debated that i assumed there had to be something to it. finding that winners actually hit top 10 **more** after their grammy was unexpected.

### the frustrating part
artist name formatting. "crosby, stills & nash" vs "crosby, stills and nash" caused duplicate files and hours of debugging. olivia rodrigo's file corrupted **three times** due to a bug in my script.

## project structure

```
grammy-trajectories/
├── data/
│   ├── raw/                     # scraped billboard data
│   └── processed/               
│       └── billboard_bna_quarterly.csv
├── scripts/
│   ├── 02_scrape_billboard.py
│   └── 03_scrape_bna_quarterly.py
├── analysis/
│   └── separated_chart_analysis.py
└── docs/
    ├── FINAL_ANALYSIS_NO_CURSE.md
    └── moonpath_blog_final_with_colors.md
```

## limitations

**quarterly sampling**: i sampled 4 dates per year rather than every week. this captures major hits but misses songs that charted briefly at lower positions.

**no spotify data**: the spotify api has been down during this project. streaming data would provide modern commercial success metrics, especially for post-2010 artists.

**pre-streaming era bias**: most of the dataset (55 of 65 artists) is from 1960-2010. chart dynamics changed significantly with streaming.

**no control group**: i only analyzed winners. comparing to best new artist nominees who lost would show whether winning causes anything or if breakthrough artists in general face similar trajectories. this is on my list for phase 2.

**peak positions don't show everything**: an artist who hits #1 once then disappears looks the same as an artist who hits #1 and sustains a long career. peaks measure ceiling, not consistency or longevity.

## what's next: phase 2

comparing grammy winners vs. nominees who lost would answer whether *winning* causes anything or if these are just natural career arcs.

example matchups:
- **amy winehouse** (won 2008) vs. **taylor swift** (nominated, lost)
- **macklemore & ryan lewis** (won 2014) vs. **kendrick lamar** (nominated, lost)

estimated effort: 20-30 hours to scrape 30-50 additional artists.

this would turn a good analysis into a definitive one.

## tools & tech

- **python**: pandas, scipy, matplotlib
- **data source**: billboard.com
- **statistical test**: wilcoxon signed-rank test
- **visualization**: matplotlib with custom styling

## why i built this

i've run an annual grammy predictions survey with friends since 2020. this year, 30 people participated. the best new artist category always sparks debate about the "curse."

i wanted to test music industry folklore with actual data. this became both a personal curiosity project and my first serious dive into music data analysis - building a differentiated portfolio piece that goes beyond typical kaggle datasets.

i'm passionate about exploring the stories hidden in music data. this is the first post in what i'm hoping becomes a series at [moonpath.dev](https://moonpath.dev), where we build human-centered music experiences.

## fun facts discovered

**olivia dean** (2026 best new artist winner) has the middle name lauryn - named after lauryn hill, who won best new artist in 1999. dean was born in 1998, the year hill's "the miseducation of lauryn hill" dominated. a full-circle grammy moment.

**best new artist** doesn't mean "debut artist." many winners had been releasing music for years before their "breakthrough" moment. bon iver won for his second album. chance the rapper had multiple mixtapes out. the grammy marks when an artist breaks through to mainstream awareness.

## contact

**aleyiah peña**  
hello@moonpath.dev  
[moonpath.dev](https://moonpath.dev) | [linkedin](https://linkedin.com/in/aleyiahpena)

*this analysis represents my personal research and is not professional music industry analysis. i'm an analyst who loves music data - not a music industry expert.*

## license

mit - use this data however you want for your own analysis.
