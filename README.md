# Data Is Plural: Newsletter Stats

Each weekly edition of [Data Is Plural](https://tinyletter.com/data-is-plural) features five useful/interesting datasets (or groups of related datasets). This repository contains [statistics for each published edition](data/messages.csv), derived from [TinyLetter's undocumented API](https://github.com/jsvine/tinystats).

## Subscribers

This [autogenerated](scripts/make-chart-subscribers.py) chart tracks the number of subscribers who received each edition:

![Data Is Plural subscribers over time](charts/subscribers.png)

#### Notes

- November 2015 spike coincided with announcements on [NICAR-L](https://www.ire.org/resource-center/listservs/subscribe-nicar-l/) and [Hacker News](https://news.ycombinator.com/item?id=10513012).

- March 2016 spike coincided with a [nice Poynter article about the newsletter](http://www.poynter.org/2016/meet-the-buzzfeed-editor-that-data-journalists-love/400553/).

## Open Rate

This [autogenerated](scripts/make-chart-open-rate.py) chart tracks each edition's "open rate" — the percentage of subscribers whom TinyLetter detected as having opened the newsletter:

![Data Is Plural "open rate" over time](charts/open-rate.png)

## Unique Opens

This [autogenerated](scripts/make-chart-unique-opens.py) chart tracks each edition's total "unique opens" — the number of subscribers whom TinyLetter detected as having opened the newsletter:

![Data Is Plural "unique opens" over time](charts/unique-opens.png)

## Explore the data

You can [explore the raw data here](data/messages.csv). It contains the following fields:

- `id`
- `stub`
- `subject`
- `sent_at`
- `sent_at_date`
- `send_count`
- `stats.total_opens`
- `stats.total_clicks`
- `stats.unique_opens`
- `stats.unique_clicks`
- `stats.open_rate`
- `stats.click_rate`
- `stats.soft_bounces`
- `stats.hard_bounces`
- `stats.spam_complaints`
- `stats.unsubs`

See anything interesting? Let me know! ([Contact information here](http://jsvine.com).)
