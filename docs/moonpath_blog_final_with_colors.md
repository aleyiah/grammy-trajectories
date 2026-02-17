# testing the best new artist curse: what 68 years of data actually shows

february 16, 2026  
aleyiah peña

---

since 2020, i've run an annual grammy predictions survey with my friends. this year, 30 people participated - we vote on who we think will win each major category, and i give a gift card to whoever gets the most right. it's become this tradition that shows who's in tune with the pulse of pop culture and who's just guessing based on vibes.

every year, the best new artist category sparks the same debate: is winning this award actually a good thing? the "best new artist curse" is music industry folklore - the idea that winning dooms your career. people point to fun. (broke up shortly after), macklemore & ryan lewis (disappeared after their viral moment), and various one-album wonders as proof.

i wanted to know: is this actually true, or just confirmation bias?

so i spent 350 hours collecting data on 65 best new artist winners across 68 years (1958-2026) to test it. this is my first real dive into music data analysis, and it became both a personal curiosity project and the inaugural post in what we're hoping becomes a series exploring music through data at moonpath.

---

## what i found

the best new artist curse doesn't exist.

at least not in the way people think. looking at peak chart performance - the best position artists achieved before versus after their grammy win - there's no statistical evidence of a curse.

**the data:**
- 67.9% of winners hit top 10 on hot 100 after their grammy <span style="color: #6BBF6B;">(up from 56.6% before)</span>
- 61.0% hit top 10 on billboard 200 after their grammy <span style="color: #6BBF6B;">(up from 42.4% before)</span>
- more winners hit #1 albums after grammy <span style="color: #6BBF6B;">(8 artists)</span> than before <span style="color: #D94F4F;">(4 artists)</span>
- no statistically significant decline in peak positions for singles (p=0.35) or albums (p=0.05)

most winners maintain or improve their peak chart performance after winning. the curse is folklore, not fact.

---

## the success stories

### adele

adele won best new artist in 2009 for her album "19."

**chart performance:**
- peak before grammy: <span style="color: #D94F4F;">#41</span> (billboard 200)
- peak after grammy: <span style="color: #6BBF6B;">#1</span> (billboard 200)

her best albums - "21" and "25" - both hit #1 and came after her grammy win.

### the beatles

the beatles won in 1965 at the height of beatlemania. they maintained #1 performance on both singles and albums after winning. zero curse effect.

### maroon 5

maroon 5 won in 2005. before their grammy, they had <span style="color: #D94F4F;">3 charting singles</span> with a peak of <span style="color: #D94F4F;">#6</span>. after? <span style="color: #6BBF6B;">18 charting singles</span> including two that hit <span style="color: #6BBF6B;">#1</span> ("moves like jagger" and "one more night").

### billie eilish

billie showed small declines in peak position (singles: <span style="color: #6BBF6B;">#3</span> before → <span style="color: #D94F4F;">#6</span> after, albums: <span style="color: #6BBF6B;">#3</span> → <span style="color: #D94F4F;">#4</span>), but she's still producing top 5 albums and top 10 singles. "birds of a feather" hit #6 in 2024 and was still charting in early 2025.

whether looking at singles or albums, many winners either maintained or improved their peak performance after the grammy.

---

## why do people believe the curse?

### we remember the dramatic failures

fun broke up shortly after winning in 2013. their singles peak went from <span style="color: #6BBF6B;">#1</span> ("we are young") to <span style="color: #D94F4F;">#14</span> post-grammy. the band dissolved - but jack antonoff, their guitarist, went on to become one of the most dominant producers in music. he's won producer of the year multiple times and produced grammy-winning work for taylor swift, kendrick lamar, and countless others. the band failed, but its members didn't.

macklemore & ryan lewis had a massive cultural moment with "thrift shop" (<span style="color: #6BBF6B;">#1</span> in 2013), won best new artist in 2014, then seemingly disappeared. their best post-grammy single only hit <span style="color: #D94F4F;">#16</span>. they were a viral phenomenon - the kind of lightning-in-a-bottle moment that's nearly impossible to replicate.

natural career arcs. some artists peak early, some sustain, some reinvent. the grammy didn't determine which path they took.

### the psychology of it

we're wired to remember the dramatic failures - the scandal, the one-hit wonder, the band that broke up. the consistent successes fade into background noise, even when they outnumber the failures.

about 47% of winners on hot 100 and 42% on billboard 200 had worse peak positions after their grammy. that means 53% maintained or improved singles peaks, and 58% maintained or improved album peaks.

more winners succeed than fail. the curse narrative focuses on the minority.

---

## how i did this

**what i analyzed:**
- 65 best new artist winners (1960-2026)
- 2,526 billboard chart entries
- both hot 100 (singles) and billboard 200 (albums)
- peak chart positions before vs after grammy win
- quarterly sampling: 4 dates per year (jan, apr, jul, oct)
- time window: 5 years before win → 10 years after

**why peak positions?**  
i wanted to know if winners could still release hit music - not whether they sustained constant visibility. a #1 album is a #1 album, whether it happens the year of the grammy or five years later.

**missing artist:**  
samara joy (2023 winner) has never charted on hot 100 or billboard 200. she's a jazz artist - proof you can win best new artist through critical acclaim without mainstream commercial chart presence.

**fun fact i discovered:**  
olivia dean, the 2026 best new artist winner, has the middle name lauryn - named after lauryn hill, who won best new artist in 1999. dean was born in 1998, the year hill's "the miseducation of lauryn hill" dominated. a full-circle grammy moment.

**note on best new artist:**  
this award recognizes breakthrough moments, not debuts. many winners had been releasing music for years before their "breakthrough" moment. bon iver won for his second album. chance the rapper had multiple mixtapes out. the grammy marks when an artist breaks through to mainstream awareness, not when they start their career.

---

## what i learned (beyond the data)

### the technical journey

this was my first web scraping project. going from not knowing how to scrape to building a system that collected 2,526 data points across 65 artists over 68 years was challenging. i learned python web scraping, error handling, data validation, and how to keep code running overnight without my laptop going to sleep.

### the exciting part

i woke up every morning excited to check the progress - watching the dataset grow from 10 artists to 41 to 65 felt like watching a hypothesis come to life.

### the surprising part

i genuinely expected to find evidence of a curse. the folklore is so debated that i assumed there had to be something to it. finding that winners actually hit top 10 more after their grammy was unexpected.

### the frustrating part

artist name formatting. "crosby, stills & nash" vs "crosby, stills and nash" caused duplicate files and hours of debugging. olivia rodrigo's file corrupted three times due to a bug in my script.

### what i'd do differently

if i started over, i might focus on peak positions from the beginning instead of exploring multiple metrics. however, the exploration taught me why peaks matter more than averages for this question.

---

## limitations

**quarterly sampling:**  
i sampled 4 dates per year rather than every week. this captures major hits but misses songs that charted briefly at lower positions. testing showed this captures about 75% of chart appearances - all the hits are there, but some deep cuts are missing.

**no spotify data:**  
the spotify api has been down during this project. streaming data would provide modern commercial success metrics, especially for post-2010 artists. chart positions and streaming success don't always align.

**pre-streaming era bias:**  
most of the dataset (55 of 65 artists) is from 1960-2010. chart dynamics changed significantly with streaming - singles became more important, album sales declined. the patterns i found might not hold exactly the same way for artists who debuted in the streaming era.

**no control group:**  
i only analyzed winners. comparing to best new artist nominees who lost would show whether winning causes anything or if breakthrough artists in general face similar trajectories. this is on my list for a future analysis.

**peak positions don't show everything:**  
an artist who hits #1 once then disappears looks the same as an artist who hits #1 and sustains a long career. peak positions measure ceiling, not consistency or longevity.

---

## what this means

after analyzing 68 years of grammy winners and 2,526 billboard chart entries, i found no statistical evidence that winning best new artist hurts careers.

**what the data shows:**
- most winners maintain or improve peak chart performance
- more winners hit top 10 after their grammy
- success stories outnumber failures
- failures often have explanations unrelated to the grammy

**what people believe:**
- winning best new artist dooms your career
- the curse is real and documented
- winners fade into obscurity

the gap between belief and data is significant. the best new artist curse is folklore, not fact. we're wired to remember the dramatic failures - the scandal, the one-hit wonder, the band that broke up. the consistent successes fade into background noise, even when they outnumber the failures.

at least i can rest assured that my favorite artists aren't doomed by winning. chappell roan won in 2025 - turns out she'll probably be fine.

---

## what's next

this is the first post in what we're planning as a music data series at moonpath. we're interested in exploring the stories hidden in listening patterns, chart positions, and the way music marks time in our lives.

if you're curious about your own music data, check out [seasons of your life](https://seasons.moonpath.dev) - upload your spotify data and see which songs defined every era of your life. the first 100 users get free full access.

or share an anonymous music memory at [resonance](https://resonance.moonpath.dev) - our platform for the songs that meant something to you.

follow along on [instagram](https://www.instagram.com/moonpath.dev) for regular updates.

---

*questions? thoughts? disagree with my findings? reach out at hello@moonpath.dev or find me on [linkedin](https://linkedin.com/in/aleyiahpena)*

*this analysis represents my personal research and is not professional music industry analysis. i'm an analyst and program manager who loves music data - not a music industry expert.*
