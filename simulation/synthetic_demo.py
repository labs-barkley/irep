"""
IREP — Stage 0 synthetic demonstration.

WHAT THIS IS: a mechanism demonstration and analysis-pipeline dry run.
WHAT THIS IS NOT: a validation. The biases below are INJECTED BY US;
detecting them is circular by construction. See VALIDATION.md, Stage 0.

Setup (all assumptions explicit and adjustable):
  - Candidates have a true competence, identically distributed across
    two groups A and B (the simulation assumes NO true group difference;
    that assumption is the point).
  - Credentials are awarded as a function of competence AND group
    (unequal access), so the credential is a biased proxy.
  - The CONVENTIONAL pipeline scores candidates on a noisy competence
    signal + credential bonus + an evaluator prior against group B
    + time-pressure noise hitting stress-sensitive candidates.
  - The IREP pipeline scores candidates on the average of several
    untimed work-sample signals of true competence. No credential term,
    no group term, no time-pressure term.
Both pipelines select the same top fraction. We compare who they pick.

Run: python synthetic_demo.py   (numpy only, fixed seed)
"""

import numpy as np

RNG = np.random.default_rng(seed=1906)  # Sumner, Folkways

# ---------------- population ----------------
N = 20_000
P_GROUP_B = 0.30
competence = RNG.normal(0.0, 1.0, N)              # true, unobserved
group_b = RNG.random(N) < P_GROUP_B               # True = group B

# credential: depends on competence AND on group (unequal access)
CRED_ACCESS_GAP = 1.0                              # group B faces higher bar
cred_logit = 1.2 * competence - 0.5 - CRED_ACCESS_GAP * group_b
credential = RNG.random(N) < 1 / (1 + np.exp(-cred_logit))

# stress sensitivity: independent of competence by construction
stress_sensitive = RNG.random(N) < 0.25

# ---------------- conventional pipeline ----------------
EVALUATOR_PRIOR_B = -0.55        # category prior against group B
CREDENTIAL_BONUS = +0.60         # credential read as competence
TIME_PRESSURE_HIT = -0.80        # timed-test degradation if stress-sensitive
SIGNAL_NOISE = 0.90              # one rushed reading of one CV

conventional_score = (
    competence
    + RNG.normal(0, SIGNAL_NOISE, N)
    + CREDENTIAL_BONUS * credential
    + EVALUATOR_PRIOR_B * group_b
    + TIME_PRESSURE_HIT * stress_sensitive * RNG.random(N)
)

# ---------------- IREP pipeline ----------------
K_SAMPLES = 4                    # several untimed, structured work samples
irep_score = competence + RNG.normal(0, SIGNAL_NOISE / np.sqrt(K_SAMPLES), N)
# no credential term, no group term, no time-pressure term — by design

# ---------------- selection ----------------
TOP_FRAC = 0.10
k = int(N * TOP_FRAC)
sel_conv = np.argsort(-conventional_score)[:k]
sel_irep = np.argsort(-irep_score)[:k]
set_conv, set_irep = set(sel_conv), set(sel_irep)

def report(name, idx):
    return (f"{name:<14} mean true competence: {competence[idx].mean():+.3f} | "
            f"group B share: {group_b[idx].mean():5.1%} | "
            f"credentialed: {credential[idx].mean():5.1%} | "
            f"stress-sensitive: {stress_sensitive[idx].mean():5.1%}")

print("=" * 78)
print(f"Population: N={N:,} | group B: {P_GROUP_B:.0%} | "
      f"true competence identical across groups by construction")
print("=" * 78)
print(report("POPULATION", np.arange(N)))
print(report("CONVENTIONAL", sel_conv))
print(report("IREP", sel_irep))
print("-" * 78)
overlap = len(set_conv & set_irep) / k
print(f"Selection overlap between pipelines: {overlap:.1%}")

invisible = np.array(sorted(set_irep - set_conv))  # IREP yes, conventional no
print(f"\n'Invisible candidates' (selected by IREP, rejected by conventional): "
      f"{len(invisible):,}")
print(report("  INVISIBLE", invisible))
print(f"  -> of whom uncredentialed: {(~credential[invisible]).mean():.1%} | "
      f"group B: {group_b[invisible].mean():.1%} | "
      f"stress-sensitive: {stress_sensitive[invisible].mean():.1%}")

print("\nReminder: illustrative under stated assumptions. The biases are "
      "injected;\ndetecting them is circular. Real evidence: VALIDATION.md "
      "Stages 1-3.")
