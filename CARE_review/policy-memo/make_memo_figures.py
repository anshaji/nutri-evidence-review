#!/usr/bin/env python3
"""Figure for the ScaleWorks policy memo. Values reproduce the memo arithmetic."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(OUT, exist_ok=True)

SURFACE, INK, INK_2, INK_MUTED = "#fcfcfb", "#0b0b0b", "#52514e", "#8a8a85"
BLUE, ORANGE, GRID = "#2a78d6", "#eb6834", "#e3e2dd"

plt.rcParams.update({
    "font.family": ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"],
    "font.size": 8.5, "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE, "axes.edgecolor": GRID, "axes.labelcolor": INK_2,
    "xtick.color": INK_2, "ytick.color": INK_2,
    "axes.spines.top": False, "axes.spines.right": False, "axes.spines.left": False,
})

fig, axes = plt.subplots(1, 2, figsize=(11.0, 3.9))

# --- Panel A: CMAM, same budget buys more children ---------------------
ax = axes[0]
rows = [("Standard protocol\n$1,041 per child recovered", 961, INK_MUTED),
        ("Combined protocol (ComPAS)\n$918 per child recovered", 1089, ORANGE)]
ys = range(len(rows))
for y, (lab, v, c) in zip(ys, rows):
    ax.barh(y, v, height=0.50, color=c, zorder=3, edgecolor=SURFACE, linewidth=1.2)
    delta = "" if y == 0 else f"   +{v/961-1:.0%}"
    ax.text(v + 20, y, f"{v:,}{delta}", va="center", ha="left",
            fontsize=9, color=INK, fontweight="bold")
ax.set_yticks(list(ys)); ax.set_yticklabels([r[0] for r in rows], fontsize=8, color=INK_2)
ax.invert_yaxis(); ax.tick_params(axis="y", length=0)
ax.set_xlim(0, 1480); ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
ax.xaxis.set_major_formatter(FuncFormatter(lambda v, p: f"{v:,.0f}"))
ax.set_xlabel("Children recovered per US$1 million", fontsize=8, color=INK_2, labelpad=6)
ax.set_title("Wasting treatment: same budget, more children recovered",
             loc="left", fontsize=9.6, color=INK, fontweight="bold", pad=8)
ax.text(0, -0.30, "Trial-measured costs, ComPAS (Kenya and South Sudan). Recovery 76.3% vs 73.5%.\n"
                  "Not indicated for MUAC <115 mm or oedema, where the standard protocol did better.",
        transform=ax.transAxes, ha="left", va="top", fontsize=7.0,
        color=INK_MUTED, style="italic")

# --- Panel B: MMS, higher unit cost buying a better birth --------------
ax = axes[1]
rows = [("South Asia\nlow birthweight 24.8%", 48, ORANGE),
        ("Sub-Saharan Africa\nlow birthweight 13.9%", 85, BLUE)]
ys = range(len(rows))
for y, (lab, v, c) in zip(ys, rows):
    ax.barh(y, v, height=0.45, color=c, zorder=3, edgecolor=SURFACE, linewidth=1.2)
    ax.text(v + 2, y, f"${v}", va="center", ha="left", fontsize=11,
            color=INK, fontweight="bold")
ax.set_yticks(list(ys)); ax.set_yticklabels([r[0] for r in rows], fontsize=8, color=INK_2)
ax.invert_yaxis(); ax.tick_params(axis="y", length=0)
ax.set_xlim(0, 112); ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
ax.xaxis.set_major_formatter(FuncFormatter(lambda v, p: f"${v:,.0f}"))
ax.set_xlabel("Cost per low-birthweight birth averted", fontsize=8, color=INK_2, labelpad=6)
ax.set_title("Antenatal MMS: better births, higher unit cost",
             loc="left", fontsize=9.6, color=INK, fontweight="bold", pad=8)
ax.text(0, -0.30, "MMS costs $1.42 more per pregnancy than iron-folic acid, so a fixed\n"
                  "budget covers 42% fewer women. Judge it per case averted, not per head.",
        transform=ax.transAxes, ha="left", va="top", fontsize=7.0,
        color=INK_MUTED, style="italic")

fig.suptitle("What a fixed budget buys — two different shapes of opportunity",
             x=0.010, y=0.975, ha="left", fontsize=11.5, color=INK, fontweight="bold")
fig.text(0.010, 0.885,
         "The two panels use different units and are not comparable to one another. "
         "Left panel is trial-measured. Right panel is our arithmetic from published unit costs and the pooled effect estimate.",
         fontsize=8, color=INK_2)
fig.subplots_adjust(left=0.150, right=0.990, top=0.715, bottom=0.290, wspace=0.62)
fig.savefig(os.path.join(OUT, "fig_fixed_budget.png"), dpi=220)
print("wrote figures/fig_fixed_budget.png")
