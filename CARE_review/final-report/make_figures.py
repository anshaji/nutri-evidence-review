#!/usr/bin/env python3
"""Figures for the CARE evidence summary. Every value traces to the report text.

Run:  python3 make_figures.py    (writes figures/*.png next to this file)
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.ticker import FixedLocator, FuncFormatter

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(OUT, exist_ok=True)

# --- design tokens (validated palette, light surface) ---------------------
SURFACE   = "#fcfcfb"
INK       = "#0b0b0b"
INK_2     = "#52514e"
INK_MUTED = "#8a8a85"
BLUE      = "#2a78d6"   # slot 1 — significant
ORANGE    = "#eb6834"   # slot 2 — emphasis
GRID      = "#e3e2dd"

plt.rcParams.update({
    "font.family": ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"],
    "font.size": 8.5,
    "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
    "axes.edgecolor": GRID,
    "axes.labelcolor": INK_2,
    "xtick.color": INK_2,
    "ytick.color": INK_2,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.spines.left": False,
})


def _forest_panel(ax, rows, xlim, title, favour_note):
    """rows: list of (kind, ...) where kind is 'head' or 'row'.

    Row tuples keep their GRADE rating as a trailing field. It is no longer
    drawn — the certainty column was removed from the figure — but the ratings
    are verified against each source and the report text still cites them, so
    they stay here rather than being deleted.
    """
    ys, ylabels = [], []
    y = 0
    drawn = []
    for r in rows:
        if r[0] == "head":
            ys.append(y); ylabels.append(r[1]); drawn.append(("head", y))
            y -= 1
        else:
            _, label, est, lo, hi, cert = r
            ys.append(y); ylabels.append("   " + label)
            drawn.append(("row", y, est, lo, hi, cert))
            y -= 1

    for d in drawn:
        if d[0] != "row":
            continue
        _, yy, est, lo, hi, _cert = d
        sig = not (lo <= 1.0 <= hi)
        c = BLUE if sig else INK_MUTED
        ax.plot([lo, hi], [yy, yy], color=c, lw=2, solid_capstyle="round", zorder=3)
        ax.plot([est], [yy], "o", ms=6.5, color=c, mec=SURFACE, mew=1.6, zorder=4)
        ax.text(xlim[1] * 1.04, yy, f"{est:.2f}  ({lo:.2f}–{hi:.2f})",
                va="center", ha="left", fontsize=7.6, color=INK)

    ax.axvline(1.0, color=INK_MUTED, lw=1, ls=(0, (3, 3)), zorder=1)
    ax.set_xscale("log")
    ax.set_xlim(*xlim)
    ax.set_ylim(min(ys) - 0.7, 1.5)
    ax.text(xlim[1] * 1.04, 0.95, "Estimate (95% CI)", va="center", ha="left",
            fontsize=7.4, color=INK_2, clip_on=False)
    ticks = [t for t in (0.5, 0.7, 1.0, 1.5, 2.0, 2.5) if xlim[0] <= t <= xlim[1]]
    ax.xaxis.set_major_locator(FixedLocator(ticks))
    ax.xaxis.set_minor_locator(FixedLocator([]))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, p: f"{v:g}"))
    ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    ax.set_yticks(ys)
    ax.set_yticklabels(ylabels, fontsize=7.8)
    for lbl, r in zip(ax.get_yticklabels(), rows):
        if r[0] == "head":
            lbl.set_color(INK); lbl.set_fontweight("bold"); lbl.set_fontsize(7.9)
        else:
            lbl.set_color(INK_2)
    ax.tick_params(axis="y", length=0)
    ax.set_title(title, loc="left", fontsize=9, color=INK, fontweight="bold", pad=8)
    ax.text(0, 1.0, favour_note, transform=ax.transAxes, ha="left", va="bottom",
            fontsize=7.4, color=INK_2)


def fig1_forest():
    adverse = [
        ("head", "Wasting treatment — children with severe acute malnutrition"),
        ("row", "Relapse: standard vs alternative RUTF formulations", 0.84, 0.72, 0.98, "High"),
        ("head", "Facility newborn care — preterm or low-birth-weight infants"),
        ("row", "Kangaroo mother care vs conventional care: mortality", 0.68, 0.53, 0.86, "High"),
        ("row", "Immediate vs post-stabilisation KMC: 28-day mortality (1.0–1.8 kg)", 0.75, 0.64, 0.89, ""),
        ("row", "Early vs late KMC initiation: mortality", 0.77, 0.66, 0.91, "High"),
        ("row", "Kangaroo mother care: severe infection", 0.85, 0.79, 0.92, "Moderate"),
        ("head", "Community breastfeeding support — mothers, healthy term infants"),
        ("row", "Community intervention packages: neonatal mortality", 0.75, 0.67, 0.83, ""),
        ("row", "Stopping exclusive breastfeeding at 4–6 weeks", 0.83, 0.76, 0.90, "Moderate"),
        ("row", "Stopping exclusive breastfeeding at 6 months", 0.90, 0.88, 0.93, "Moderate"),
        ("head", "Antenatal MMS vs iron-folic acid — pregnant women"),
        ("row", "Low birthweight", 0.88, 0.85, 0.91, "High"),
        ("row", "Small-for-gestational-age", 0.92, 0.88, 0.97, "Moderate"),
        ("row", "Preterm birth", 0.95, 0.90, 1.01, "Moderate"),
        ("row", "Perinatal mortality", 1.00, 0.90, 1.11, "High"),
        ("row", "Neonatal mortality", 1.00, 0.89, 1.12, "High"),
        ("row", "Maternal mortality", 1.06, 0.72, 1.54, "not rated"),
    ]
    favourable = [
        ("head", "Wasting treatment — children with acute malnutrition"),
        ("row", "Recovery: RUTF vs alternative dietary approaches", 1.33, 1.16, 1.54, "Moderate"),
        ("row", "Recovery: standard vs alternative RUTF formulations", 1.03, 0.99, 1.08, "High"),
        ("head", "Community breastfeeding support"),
        ("row", "Community intervention packages: early initiation", 1.93, 1.55, 2.39, ""),
    ]

    fig, axes = plt.subplots(
        2, 1, figsize=(11.0, 8.0),
        gridspec_kw={"height_ratios": [len(adverse), len(favourable) + 0.4], "hspace": 0.22},
    )
    _forest_panel(axes[0], adverse, (0.45, 1.60),
                  "Adverse outcomes prevented",
                  "← risk ratio below 1 favours the intervention")
    _forest_panel(axes[1], favourable, (0.85, 2.6),
                  "Favourable outcomes achieved",
                  "risk ratio above 1 favours the intervention →")

    fig.suptitle("Effect estimates by intervention — results are specific to the population that was studied",
                 x=0.010, y=0.982, ha="left", fontsize=11.5, color=INK, fontweight="bold")
    fig.text(0.010, 0.950,
             "Blue = confidence interval excludes 1.00.  Grey = interval crosses 1.00, no effect demonstrated.",
             ha="left", fontsize=7.6, color=INK_2)
    fig.text(0.010, 0.014,
             "Interventions are measured on different outcomes in different populations and are not comparable to one another on this scale.",
             ha="left", fontsize=7.2, color=INK_MUTED, style="italic")
    fig.subplots_adjust(left=0.375, right=0.855, top=0.918, bottom=0.055)
    fig.savefig(os.path.join(OUT, "fig1_forest.png"), dpi=220)
    plt.close(fig)


def fig2_cost():
    items = [
        ("Antenatal MMS — Bangladesh", 21.26, BLUE),
        ("Wasting treatment, community — Bangladesh", 26.0, BLUE),
        ("Antenatal MMS — India", 31.62, BLUE),
        ("Antenatal MMS — Pakistan", 41.54, BLUE),
        ("Wasting treatment, community — Malawi", 42.0, BLUE),
        ("Wasting treatment, inpatient — Bangladesh", 1344.0, ORANGE),
    ]
    items = sorted(items, key=lambda x: -x[1])
    fig, ax = plt.subplots(figsize=(9.0, 3.6))
    ys = list(range(len(items)))
    for y, (label, val, c) in zip(ys, items):
        ax.plot([12, val], [y, y], color=GRID, lw=1.6, zorder=2, solid_capstyle="round")
        ax.plot([val], [y], "o", ms=11, color=c, mec=SURFACE, mew=1.8, zorder=4)
        ax.text(val * 1.22, y, f"${val:,.0f}", va="center", ha="left",
                fontsize=9.2, color=INK, fontweight="bold")
    ax.set_yticks(ys)
    ax.set_yticklabels([i[0] for i in items], fontsize=8.4, color=INK_2)
    ax.tick_params(axis="y", length=0)
    ax.set_xscale("log")
    ax.set_xlim(12, 4200)
    ax.set_ylim(-0.7, len(items) - 0.3)
    ax.xaxis.set_major_locator(FixedLocator([20, 50, 100, 500, 1000]))
    ax.xaxis.set_minor_locator(FixedLocator([]))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, p: f"${v:,.0f}"))
    ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    ax.set_xlabel("Cost per DALY averted — log scale", fontsize=8.4, color=INK_2, labelpad=7)
    fig.suptitle("What each intervention buys", x=0.010, y=0.975, ha="left",
                 fontsize=11.5, color=INK, fontweight="bold")
    fig.text(0.010, 0.878,
             "Community-based wasting treatment averts a DALY for roughly a fiftieth of the cost of inpatient care.",
             fontsize=8.2, color=INK_2)
    fig.text(0.010, 0.025,
             "MMS figures are modelled and assume high coverage and adherence, so real-world cost will be higher.  The Malawi estimate is a decision-model base case ($493 under worst-case assumptions).  "
             "Price years differ (2007–2016 USD).",
             fontsize=7.2, color=INK_MUTED, style="italic")
    fig.subplots_adjust(left=0.335, right=0.925, top=0.815, bottom=0.235)
    fig.savefig(os.path.join(OUT, "fig2_cost.png"), dpi=220)
    plt.close(fig)


def fig3_targeting():
    wasting = [
        ("India", 18.7), ("Yemen", 16.8), ("Sudan", 16.3), ("Nigeria", 11.6),
        ("Niger", 10.9), ("Bangladesh", 10.7), ("Burkina Faso", 9.3), ("Chad", 7.8),
        ("Pakistan", 7.1), ("Nepal", 7.0), ("Ethiopia", 6.8), ("Mali", 5.4),
        ("Kenya", 4.5),
    ]
    lbw = [
        ("South Asia", 24.8), ("Least Developed Countries", 15.4),
        ("Horn of Africa (IGAD)", 14.6), ("Eastern & Southern Africa", 14.4),
        ("Western Africa", 14.3), ("Sub-Saharan Africa", 13.9), ("Sahel", 13.8),
        ("Middle East & North Africa", 12.9), ("Latin America & Caribbean", 9.7),
        ("East Asia & Pacific", 8.5),
    ]
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.6))

    HIGHLIGHT = {"India", "Yemen", "Sudan", "Nigeria", "Niger", "Burkina Faso"}
    ax = axes[0]
    ys = range(len(wasting))
    for y, (c, v) in zip(ys, wasting):
        col = ORANGE if c in HIGHLIGHT else BLUE
        ax.barh(y, v, height=0.6, color=col, zorder=3, edgecolor=SURFACE, linewidth=1.2)
        ax.text(v + 0.35, y, f"{v:.1f}", va="center", ha="left", fontsize=7.8, color=INK)
    ax.axvline(5.9, color=INK_MUTED, lw=1, ls=(0, (3, 3)), zorder=4)
    ax.text(6.3, -0.75, "sub-Saharan Africa average 5.9", fontsize=7,
            color=INK_2, va="center", ha="left")
    ax.set_yticks(list(ys)); ax.set_yticklabels([c for c, _ in wasting], fontsize=8, color=INK_2)
    ax.tick_params(axis="y", length=0)
    ax.set_ylim(len(wasting) - 0.4, -1.1)
    ax.set_xlim(0, 23); ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    ax.set_xlabel("Wasting, % of children under 5", fontsize=8, color=INK_2, labelpad=6)
    ax.legend(handles=[Patch(facecolor=ORANGE, edgecolor="none",
                             label="India, and the highest-burden countries of\nthe Sahel, the Horn of Africa and Yemen"),
                       Patch(facecolor=BLUE, edgecolor="none",
                             label="Other countries shown")],
              loc="lower right", bbox_to_anchor=(1.02, 0.02), frameon=False,
              fontsize=7, labelspacing=0.8, handlelength=1.1, handleheight=1.1,
              borderpad=0, labelcolor=INK_2)
    ax.set_title("Wasting sits in two places — India, and the Sahel, Horn and Yemen",
                 loc="left", fontsize=9.6, color=INK, fontweight="bold", pad=8)

    ax = axes[1]
    ys = range(len(lbw))
    for y, (c, v) in zip(ys, lbw):
        col = ORANGE if c == "South Asia" else BLUE
        ax.barh(y, v, height=0.6, color=col, zorder=3, edgecolor=SURFACE, linewidth=1.2)
        ax.text(v + 0.35, y, f"{v:.1f}", va="center", ha="left", fontsize=7.8, color=INK)
    ax.set_yticks(list(ys)); ax.set_yticklabels([c for c, _ in lbw], fontsize=8, color=INK_2)
    ax.invert_yaxis(); ax.tick_params(axis="y", length=0)
    ax.set_xlim(0, 30); ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    ax.set_xlabel("Low birthweight, % of newborns", fontsize=8, color=INK_2, labelpad=6)
    ax.legend(handles=[Patch(facecolor=ORANGE, edgecolor="none", label="South Asia"),
                       Patch(facecolor=BLUE, edgecolor="none", label="Other regions")],
              loc="lower right", bbox_to_anchor=(1.02, 0.02), frameon=False,
              fontsize=7, labelspacing=0.5, handlelength=1.1, handleheight=1.1,
              borderpad=0, labelcolor=INK_2)
    ax.set_title("Low birthweight is concentrated in South Asia",
                 loc="left", fontsize=9.6, color=INK, fontweight="bold", pad=8)

    fig.suptitle("Where each intervention has the most to work with",
                 x=0.010, y=0.975, ha="left", fontsize=11.5, color=INK, fontweight="bold")
    fig.text(0.010, 0.912,
             "Left drives siting for wasting treatment; right drives siting for MMS and the facility newborn package.  "
             "Colour marks which concentration a country or region belongs to — it is not a prevalence threshold.",
             fontsize=8, color=INK_2)
    fig.text(0.012, 0.020,
             "Wasting: latest national survey estimate per country (WHO GHO / World Bank, 2014–2024); survey years and seasons differ.  Low birthweight: UNICEF-WHO modelled estimates, 2020.\n"
             "Chad and Mali are Sahel countries whose wasting has since fallen, so they appear in blue.  Sub-national variation exceeds all these differences.",
             fontsize=7, color=INK_MUTED, style="italic")
    fig.subplots_adjust(left=0.135, right=0.985, top=0.800, bottom=0.205, wspace=0.62)
    fig.savefig(os.path.join(OUT, "fig3_targeting.png"), dpi=220)
    plt.close(fig)


def fig4_cascade():
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.8))

    ax = axes[0]
    bars = [("Community\nmass screening", 8, ORANGE), ("Clinic-based systematic\nscreening", 98, BLUE)]
    for i, (lab, v, c) in enumerate(bars):
        ax.bar(i, v, width=0.5, color=c, zorder=3, edgecolor=SURFACE, linewidth=1.2)
        ax.text(i, v + 3, f"{v}%", ha="center", va="bottom", fontsize=13,
                color=INK, fontweight="bold")
    ax.set_xticks([0, 1]); ax.set_xticklabels([b[0] for b in bars], fontsize=8, color=INK_2)
    ax.set_ylim(0, 118); ax.set_yticks([0, 25, 50, 75, 100])
    ax.grid(axis="y", color=GRID, lw=0.8, zorder=0)
    ax.tick_params(axis="x", length=0)
    ax.set_ylabel("Detected cases enrolled in treatment (%)", fontsize=8, color=INK_2)
    ax.set_title("Finding children and treating them are two different problems",
                 loc="left", fontsize=9.6, color=INK, fontweight="bold", pad=8)
    ax.text(0.5, -0.28,
            "Burundi — enrolment into treatment, by case-detection approach.\n"
            "Odjidja et al. 2022 — one organisation, 18 collines, same six months.\n"
            "Community arm rests on ~37 detected cases: read the contrast, not the precision.",
            transform=ax.transAxes, ha="center", va="top", fontsize=7.0,
            color=INK_MUTED, style="italic")

    ax = axes[1]
    rel = [("Somalia", 22), ("Mali", 30), ("South Sudan", 63)]
    for i, (lab, v) in enumerate(rel):
        c = ORANGE if v >= 50 else BLUE
        ax.bar(i, v, width=0.5, color=c, zorder=3, edgecolor=SURFACE, linewidth=1.2)
        ax.text(i, v + 2, f"{v}%", ha="center", va="bottom", fontsize=13,
                color=INK, fontweight="bold")
    ax.set_xticks(range(len(rel))); ax.set_xticklabels([r[0] for r in rel], fontsize=8, color=INK_2)
    ax.set_ylim(0, 78); ax.set_yticks([0, 20, 40, 60])
    ax.grid(axis="y", color=GRID, lw=0.8, zorder=0)
    ax.tick_params(axis="x", length=0)
    ax.set_ylabel("Relapsed within 6 months (%)", fontsize=8, color=INK_2)
    ax.set_title("Recovery at discharge overstates durable effect",
                 loc="left", fontsize=9.6, color=INK, fontweight="bold", pad=8)
    ax.text(0.5, -0.28,
            "Children discharged as recovered from severe acute malnutrition;\n"
            "relapse is to acute malnutrition, moderate or severe.\n"
            "King et al. 2025 — not the Mali screening programme described in the text.",
            transform=ax.transAxes, ha="center", va="top", fontsize=7.0,
            color=INK_MUTED, style="italic")

    fig.suptitle("Where the treatment cascade leaks",
                 x=0.012, y=0.975, ha="left", fontsize=11.5, color=INK, fontweight="bold")
    fig.text(0.012, 0.885,
             "The two panels are separate studies measuring different things — not two views of one programme.",
             fontsize=8, color=INK_2)
    fig.subplots_adjust(left=0.085, right=0.985, top=0.720, bottom=0.260, wspace=0.30)
    fig.savefig(os.path.join(OUT, "fig4_cascade.png"), dpi=220)
    plt.close(fig)


if __name__ == "__main__":
    fig1_forest(); fig2_cost(); fig3_targeting(); fig4_cascade()
    for f in sorted(os.listdir(OUT)):
        print("wrote", os.path.join("figures", f))
