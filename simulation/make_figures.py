"""
IREP — figure generation. Run after synthetic_demo.py logic (same seed).
Figures follow the project's figure policy: assumptions stated on-figure,
synthetic data labeled as illustrative, population baseline shown,
colorblind-safe palette, full y-axes, fixed seed, script referenced.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow, FancyBboxPatch

# ---------- reproduce the simulation (identical to synthetic_demo.py) ----------
RNG = np.random.default_rng(seed=1906)
N = 20_000
P_GROUP_B = 0.30
competence = RNG.normal(0.0, 1.0, N)
group_b = RNG.random(N) < P_GROUP_B
cred_logit = 1.2 * competence - 0.5 - 1.0 * group_b
credential = RNG.random(N) < 1 / (1 + np.exp(-cred_logit))
stress_sensitive = RNG.random(N) < 0.25
conventional_score = (competence + RNG.normal(0, 0.90, N) + 0.60 * credential
                      - 0.55 * group_b - 0.80 * stress_sensitive * RNG.random(N))
irep_score = competence + RNG.normal(0, 0.90 / np.sqrt(4), N)
k = int(N * 0.10)
sel_conv = np.argsort(-conventional_score)[:k]
sel_irep = np.argsort(-irep_score)[:k]

# colorblind-safe (Okabe-Ito)
C_POP, C_CONV, C_IREP = "#999999", "#E69F00", "#0072B2"

# ---------- Figure 1: pipeline comparison ----------
groups = [np.arange(N), sel_conv, sel_irep]
labels = ["Population\n(baseline)", "Conventional\npipeline", "IREP\npipeline"]
colors = [C_POP, C_CONV, C_IREP]

metrics = {
    "Mean true competence\n(z-score)": [competence[g].mean() for g in groups],
    "Group B share\n(pop. = 30%)": [group_b[g].mean() * 100 for g in groups],
    "Stress-sensitive share\n(pop. = 25%)": [stress_sensitive[g].mean() * 100 for g in groups],
    "Credentialed share": [credential[g].mean() * 100 for g in groups],
}

fig, axes = plt.subplots(1, 4, figsize=(13, 4.2))
for ax, (title, vals) in zip(axes, metrics.items()):
    bars = ax.bar(labels, vals, color=colors, edgecolor="black", linewidth=0.6)
    ax.set_title(title, fontsize=10)
    ax.axhline(vals[0], color="black", linestyle=":", linewidth=1, alpha=0.6)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v,
                f"{v:.2f}" if abs(v) < 5 else f"{v:.0f}%",
                ha="center", va="bottom", fontsize=9)
    ax.tick_params(axis="x", labelsize=8)
    ax.spines[["top", "right"]].set_visible(False)
    if "share" in title.lower():
        ax.set_ylim(0, 100)

fig.suptitle("Two pipelines, same candidates: who gets selected (top 10% of N=20,000)",
             fontsize=12, y=1.02)
fig.text(0.5, -0.06,
         "Illustrative — SYNTHETIC data under stated assumptions (biases are injected; "
         "detecting them is circular — see VALIDATION.md Stage 0).\n"
         "True competence identically distributed across groups by construction. "
         "Seed 1906. Script: simulation/make_figures.py",
         ha="center", fontsize=8, style="italic")
fig.tight_layout()
fig.savefig("figures/reproducible/fig1_pipeline_comparison.png", dpi=200, bbox_inches="tight")

# ---------- Figure 2: protocol flow ----------
fig2, ax = plt.subplots(figsize=(12, 3.4))
ax.set_xlim(0, 12); ax.set_ylim(0, 3.4); ax.axis("off")

stages = [
    ("STAGE 1", "Category-blind,\ntrajectory-rich\nscreening",
     "no name, photo, age, sex,\nnationality, credential labels"),
    ("STAGE 2", "Untimed structured\nassessment",
     "bounded window,\nvalidated rubrics (P4)"),
    ("STAGE 3", "Decision\non evidence",
     "documented rationale,\nevaluators firewalled"),
    ("STAGE 4", "Post-decision\nmeasurement",
     "admin, legal,\nequity AUDIT only"),
]
for i, (tag, title, sub) in enumerate(stages):
    x = 0.3 + i * 3.0
    color = C_IREP if i < 3 else "#009E73"
    box = FancyBboxPatch((x, 0.8), 2.4, 1.9, boxstyle="round,pad=0.08",
                         facecolor=color, alpha=0.12, edgecolor=color, linewidth=1.6)
    ax.add_patch(box)
    ax.text(x + 1.2, 2.45, tag, ha="center", fontsize=9, fontweight="bold", color=color)
    ax.text(x + 1.2, 1.95, title, ha="center", fontsize=9.5, fontweight="bold")
    ax.text(x + 1.2, 1.25, sub, ha="center", fontsize=7.8, color="#333333")
    if i < 3:
        ax.add_patch(FancyArrow(x + 2.55, 1.75, 0.32, 0, width=0.02,
                                head_width=0.14, head_length=0.1, color="#333333"))

ax.annotate("category data enters HERE — and only here",
            xy=(10.5, 0.82), xytext=(5.6, 0.18),
            fontsize=8.5, style="italic", color="#009E73",
            arrowprops=dict(arrowstyle="->", color="#009E73", lw=1.2))
ax.text(6.0, 3.25, "IREP — the four stages: evaluation first, measurement after",
        ha="center", fontsize=12, fontweight="bold")
fig2.savefig("figures/reproducible/fig2_protocol_flow.png", dpi=200, bbox_inches="tight")
print("figures written")
