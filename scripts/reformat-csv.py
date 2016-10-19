#!/usrb/bin/env python
import sys
import csv
import datetime

COL_ORDER = [
    "id",
    "stub",
    "subject",
    "sent_at",
    "sent_at_date",
    "send_count",
    "stats.total_opens",
    "stats.total_clicks",
    "stats.unique_opens",
    "stats.unique_clicks",
    "stats.open_rate",
    "stats.click_rate",
    "stats.soft_bounces",
    "stats.hard_bounces",
    "stats.spam_complaints",
    "stats.unsubs",
]

reader = csv.DictReader(sys.stdin)
writer = csv.DictWriter(sys.stdout, fieldnames=COL_ORDER, extrasaction="ignore")
writer.writeheader()
for row in reader:
    if str(row["public_message"]) != "True":
        continue
    dt = datetime.datetime.fromtimestamp(int(row["sent_at"]))
    row["sent_at_date"] = dt.strftime("%Y-%m-%d")
    writer.writerow(row)
