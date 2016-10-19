#!/usrb/bin/env python
import seaborn as sb
import pandas as pd
import sys
from datetime import datetime

messages = pd.read_csv(sys.stdin)
messages["sent_at"] = messages["sent_at"].apply(datetime.fromtimestamp)
messages = messages.set_index(messages["sent_at"])
messages["open_rate"] = messages["stats.open_rate"].str.rstrip("%").astype(float)

COLOR = (97/255, 0, 138/255)

ax = messages["open_rate"].plot(
    kind="area",
    figsize=(12, 8),
    color=COLOR,
    alpha=0.5,
    ylim=(0, 100)
)

messages["open_rate"].plot(
    ax=ax,
    kind="line",
    marker="o",
    color=COLOR,
    alpha=0.5,
)

ax.figure.set_facecolor("#FFFFFF")
ax.set_title("Data Is Plural — Open Rate", fontsize=24)
ax.set_yticks(range(0, 110, 10))
ax.set_yticklabels([ "{0:.0f}%".format(y)
    for y in ax.get_yticks() ], fontsize=12)
ax.set_xlabel("")
sb.plt.savefig(sys.stdout, bbox_inches="tight")
