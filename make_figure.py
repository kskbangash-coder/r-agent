# -*- coding: utf-8 -*-
"""Generate Figure 1: population share (2023 census) vs NFC horizontal share.
Usage: python3 make_figure.py  -> writes figure1.png
Sources: PBS 2023 digital census; 7th NFC Award (2009/2010) horizontal shares as applied in FY2024-25.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

provinces = ["Punjab", "Sindh", "Khyber\nPakhtunkhwa", "Balochistan"]
pop_share = [52.9, 23.1, 16.9, 6.2]      # 2023 digital census, share of 4 provinces + ICT
nfc_share = [51.74, 24.55, 14.62, 9.09]  # 7th NFC Award horizontal distribution

x = np.arange(len(provinces))
w = 0.38

fig, ax = plt.subplots(figsize=(7.4, 3.4), dpi=300)
b1 = ax.bar(x - w/2, pop_share, w, label="Population share, 2023 census (%)",
            color="#1f4e79", zorder=3)
b2 = ax.bar(x + w/2, nfc_share, w, label="NFC horizontal share, 7th Award (%)",
            color="#c0504d", zorder=3)

for bars in (b1, b2):
    for r in bars:
        ax.annotate(f"{r.get_height():.1f}", (r.get_x() + r.get_width()/2, r.get_height()),
                    ha="center", va="bottom", fontsize=7.5, xytext=(0, 1.5),
                    textcoords="offset points")

ax.set_xticks(x)
ax.set_xticklabels(provinces, fontsize=8.5)
ax.set_ylabel("Per cent of national total / pool", fontsize=8.5)
ax.set_ylim(0, 60)
ax.grid(axis="y", color="#d9d9d9", lw=0.6, zorder=0)
ax.set_axisbelow(True)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.tick_params(axis="y", labelsize=8)
ax.legend(fontsize=8, frameon=False, loc="upper right")
ax.set_title("Pakistan's federation: demographic weight vs. fiscal voice", fontsize=10.5,
             color="#1f4e79", pad=8)
fig.tight_layout()
fig.savefig("figure1.png", dpi=300)
print("figure1.png written")
