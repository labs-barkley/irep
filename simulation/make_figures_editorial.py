"""
IREP - editorial figures (IREP visual identity: cream paper, serif type,
Okabe-Ito palette). Same data as make_figures.py (seed 1906). These are the
public-facing versions; plain script versions live in figures/reproducible/.
Run from simulation/:  python make_figures_editorial.py
"""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

PAPER="#FAF7F1"; INK="#1B2A41"; MUTED="#6E675D"; LINE="#D8D0C2"
C_POP="#9C9C9C"; C_CONV="#E69F00"; C_IREP="#0072B2"; GREEN="#00785C"
plt.rcParams.update({"font.family":"serif","font.serif":["Georgia","DejaVu Serif"],
    "text.color":INK,"axes.edgecolor":INK,"axes.labelcolor":INK,
    "xtick.color":INK,"ytick.color":INK})

RNG=np.random.default_rng(seed=1906); N=20_000
comp=RNG.normal(0,1,N); grp_b=RNG.random(N)<0.30
cred=RNG.random(N)<1/(1+np.exp(-(1.2*comp-0.5-1.0*grp_b)))
stress=RNG.random(N)<0.25
conv=comp+RNG.normal(0,.9,N)+.6*cred-.55*grp_b-.8*stress*RNG.random(N)
irep=comp+RNG.normal(0,.9/2,N)
k=int(N*.10); sc=np.argsort(-conv)[:k]; si=np.argsort(-irep)[:k]
G=[np.arange(N),sc,si]; labels=["Population\n(baseline)","Conventional\npipeline","IREP\npipeline"]
colors=[C_POP,C_CONV,C_IREP]

# ================= FIGURE 1 =================
metrics=[("Mean true competence\n(z-score)",[comp[g].mean() for g in G],False),
         ("Group B share\n(pop. = 30%)",[grp_b[g].mean()*100 for g in G],True),
         ("Stress-sensitive share\n(pop. = 25%)",[stress[g].mean()*100 for g in G],True),
         ("Credentialed share",[cred[g].mean()*100 for g in G],True)]
fig,axes=plt.subplots(1,4,figsize=(15,5.6),facecolor=PAPER)
fig.subplots_adjust(top=.72,bottom=.24,left=.055,right=.985,wspace=.32)
for i,(ax,(title,vals,pct)) in enumerate(zip(axes,metrics)):
    ax.set_facecolor(PAPER)
    bars=ax.bar(labels,vals,color=colors,width=.62,zorder=3)
    ax.axhline(vals[0],color=INK,ls=(0,(2,3)),lw=1,alpha=.75,zorder=2)
    for b,v in zip(bars,vals):
        ax.text(b.get_x()+b.get_width()/2,v+(2.5 if pct else .04),
                (f"{v:.0f}%" if pct else (f"{v:.2f}" if abs(v)>=.005 else "-0.00")),
                ha="center",fontsize=12,fontweight="bold")
    ax.set_title(title,fontsize=13,pad=14)
    circ=Circle((-.13,1.13),.052,transform=ax.transAxes,fill=False,ec=INK,lw=1.1,clip_on=False)
    ax.add_patch(circ); ax.text(-.13,1.128,str(i+1),transform=ax.transAxes,ha="center",va="center",fontsize=10)
    ax.set_ylim(0,100) if pct else ax.set_ylim(-0.2,1.75)
    if pct:
        ax.set_yticks(range(0,101,20)); ax.set_yticklabels([f"{v}%" for v in range(0,101,20)],fontsize=9)
    else:
        ax.tick_params(axis="y",labelsize=9)
    ax.tick_params(axis="x",labelsize=9.5)
    for sp in ["top","right"]: ax.spines[sp].set_visible(False)
    for sp in ["left","bottom"]: ax.spines[sp].set_color(MUTED)
fig.text(.055,.90,"IREP",fontsize=13,fontweight="bold",color=C_IREP,family="monospace")
fig.text(.5,.885,"Two pipelines, same candidates:\nwho gets selected (top 10% of N=20,000)",
         fontsize=24,ha="center",va="center",fontweight="bold")
fig.text(.5,.105,"Illustrative - SYNTHETIC data under stated assumptions (biases are injected; detecting them is circular - see VALIDATION.md Stage 0).",
         ha="center",fontsize=10.5,style="italic",color=MUTED)
fig.text(.5,.065,"True competence identically distributed across groups by construction. Seed 1906. Script: simulation/make_figures.py",
         ha="center",fontsize=10.5,style="italic",color=MUTED)
fig.savefig("figures/fig1_pipeline_comparison.png",dpi=170,facecolor=PAPER)

# ================= FIGURE 2 =================
fig2,ax=plt.subplots(figsize=(15,5.2),facecolor=PAPER)
ax.set_facecolor(PAPER); ax.set_xlim(0,15); ax.set_ylim(0,5.2); ax.axis("off")
ax.text(7.5,4.75,"IREP - the four stages: evaluation first, audit after decision",
        fontsize=23,ha="center",fontweight="bold")
stages=[("STAGE 1",C_IREP,"Category-blind,\ntrajectory-rich\nscreening","no name, photo, age, sex,\nnationality, credential labels"),
        ("STAGE 2",C_IREP,"Untimed structured\nassessment","bounded window,\nvalidated rubrics (P4)"),
        ("STAGE 3",C_IREP,"Decision\non evidence","documented rationale,\nevaluators firewalled"),
        ("STAGE 4",GREEN,"Firewalled\nmeasurement","separate audit channel,\nequity AUDIT only")]
for i,(tag,c,title,sub) in enumerate(stages):
    x=.55+i*3.68
    box=FancyBboxPatch((x,1.15),3.05,2.9,boxstyle="round,pad=0.09",
        facecolor=("#E9F0F6" if c==C_IREP else "#E7F2ED"),edgecolor=LINE,linewidth=1.4)
    ax.add_patch(box)
    ax.text(x+1.525,3.68,tag,ha="center",fontsize=12,fontweight="bold",color=c,family="sans-serif")
    ax.text(x+1.525,2.95,title,ha="center",va="center",fontsize=15.5,fontweight="bold",linespacing=1.15)
    ax.plot([x+.45,x+2.6],[2.28,2.28],color=MUTED,lw=.8,ls=(0,(1,2)))
    ax.text(x+1.525,1.78,sub,ha="center",va="center",fontsize=10.5,color="#3F4A5A",family="sans-serif",linespacing=1.35)
    if i<3:
        ax.add_patch(FancyArrowPatch((x+3.18,2.6),(x+3.62,2.6),arrowstyle="-|>",mutation_scale=22,lw=2.2,color=INK))
ax.text(7.5,.62,"Evaluation first. Audit after decision.",ha="center",fontsize=13.5,
        fontweight="bold",color=GREEN,style="italic")
ax.text(7.5,.22,"Category data may be collected separately, but cannot be accessed, joined or analysed until the decision is final.",
        ha="center",fontsize=11,color=GREEN,style="italic")
fig2.savefig("figures/fig2_protocol_flow.png",dpi=170,facecolor=PAPER,bbox_inches="tight")
print("editorial figures written")
