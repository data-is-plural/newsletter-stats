#!/usrb/bin/env python
import sys
import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot
import seaborn as sb
sb.set()

ONE_WEEK = timedelta(days = 7)
messages = pd.read_csv("data/messages.csv")
messages["sent_at"] = messages["sent_at"].apply(datetime.fromtimestamp)
messages = messages.set_index(messages["sent_at"])
messages["open_rate"] = messages["stats.open_rate"].str.rstrip("%").astype(float)
messages["unique_opens"] = messages["stats.unique_opens"].astype(int)

CHART_SETTINGS = [
    {
        "var": "send_count",
        "title": "Subscribers",
        "color": "teal",
        "ylim": (0, None),
        "yticks": None,
        "yticks_fmt": "{0:,.0f}"
    },
    {
        "var": "open_rate",
        "title": "Open Rate",
        "color": (97/255, 0, 138/255),
        "ylim": (0, 100),
        "yticks": range(0, 110, 10),
        "yticks_fmt": "{0:.0f}%"
    },
    {
        "var": "unique_opens",
        "title": "Unique Opens",
        "color": "#D56100",
        "ylim": (0, None),
        "yticks": None,
        "yticks_fmt": "{0:,.0f}"
    }
]

def make_chart(settings):
    var = settings["var"]
    ax = messages[var].plot(
        kind = "area",
        figsize = (12, 8),
        color = settings["color"],
        alpha = 0.5,
    )

    messages[var].plot(
        ax = ax,
        kind = "line",
        marker = "o",
        color = settings["color"],
        alpha = 0.5,
    )

    ax.set_ylim(settings["ylim"])
    ax.set_xlim(
        min(messages.index) - ONE_WEEK,
        max(messages.index) + ONE_WEEK
    )

    ax.figure.set_facecolor("#FFFFFF")

    title = "Data Is Plural — {title}".format(**settings)
    ax.set_title(title, fontsize = 24)

    ax.set_xlabel("")

    if settings["yticks"] is not None:
        ax.set_yticks(settings["yticks"])

    ax.set_yticklabels([ settings["yticks_fmt"].format(y)
        for y in ax.get_yticks() ], fontsize = 12)

    slug = settings["title"].lower().replace(" ", "-")
    dest = "charts/{}.png".format(slug)
    
    pyplot.savefig(dest, bbox_inches = "tight")
    pyplot.close()

def main():
    for settings in CHART_SETTINGS:
        make_chart(settings)

if __name__ == "__main__":
    main()
