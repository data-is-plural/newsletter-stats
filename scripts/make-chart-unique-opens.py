#!/usrb/bin/env python
import seaborn as sb
import pandas as pd
import sys
from datetime import datetime

messages = pd.read_csv(sys.stdin)
messages["sent_at"] = messages["sent_at"].apply(datetime.fromtimestamp)
messages = messages.set_index(messages["sent_at"])
messages["unique_opens"] = messages["stats.unique_opens"].astype(int)

COLOR = "#D56100"

ax = messages["unique_opens"].plot(
    kind="area",
    figsize=(12, 8),
    color=COLOR,
    alpha=0.5,
)

messages["unique_opens"].plot(
    ax=ax,
    kind="line",
    marker="o",
    color=COLOR,
    alpha=0.5,
)

ax.figure.set_facecolor("#FFFFFF")
ax.set_title("Data Is Plural — Unique Opens", fontsize=24)
ax.set_yticklabels([ "{0:,.0f}".format(y) for y in ax.get_yticks() ], fontsize=12)
ax.set_xlabel("")
sb.plt.savefig(sys.stdout, bbox_inches="tight")
