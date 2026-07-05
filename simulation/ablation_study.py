"""
IREP — Stage 0 ablation study.

Complement to synthetic_demo.py, addressing a fair methodological critique:
the full conventional-vs-IREP comparison changes several factors at once.
Here, each scenario toggles EXACTLY ONE mechanism, so the contribution of
each design element is visible in isolation.

Same caveat, always: SYNTHETIC data, biases injected by us, circular by
construction — a mechanism demonstration, never a validation (VALIDATION.md).

Run: python ablation_study.py   (numpy only, fixed seed 1906)
"""

import numpy as np

RNG_SEED = 1906
N, P_B, TOP = 20_000, 0.30, 0.10
BIAS_B, CRED_BONUS, TIME_HIT, NOISE = -0.55, 0.60, -0.80, 0.90

def population(rng):
    comp = rng.normal(0, 1, N)
    grp_b = rng.random(N) < P_B
    cred = rng.random(N) < 1 / (1 + np.exp(-(1.2 * comp - 0.5 - 1.0 * grp_b)))
    stress = rng.random(N) < 0.25
    return comp, grp_b, cred, stress

def select(score):
    return np.argsort(-score)[: int(N * TOP)]

def run(bias=False, cred_filter=False, time_pressure=False, k_samples=1):
    rng = np.random.default_rng(RNG_SEED)
    comp, grp_b, cred, stress = population(rng)
    score = comp + rng.normal(0, NOISE / np.sqrt(k_samples), N)
    if cred_filter:
        score = score + CRED_BONUS * cred
    if bias:
        score = score + BIAS_B * grp_b
    if time_pressure:
        score = score + TIME_HIT * stress * rng.random(N)
    idx = select(score)
    return comp[idx].mean(), grp_b[idx].mean(), stress[idx].mean(), cred[idx].mean()

SCENARIOS = [
    ("S0 baseline (no injected mechanism)",           dict()),
    ("S1 + evaluator category prior only",            dict(bias=True)),
    ("S2 + credential bonus only",                    dict(cred_filter=True)),
    ("S3 + time pressure only",                       dict(time_pressure=True)),
    ("S4 + multi-sample evidence only (k=4)",         dict(k_samples=4)),
    ("S5 conventional (S1+S2+S3, k=1)",               dict(bias=True, cred_filter=True, time_pressure=True)),
    ("S6 IREP (no injected mechanisms, k=4)",         dict(k_samples=4)),
]

print(f"{'scenario':<44} {'mean true comp':>14} {'group B':>9} {'stress-sens':>12} {'credentialed':>13}")
print("-" * 96)
for name, kw in SCENARIOS:
    c, b, st, cr = run(**kw)
    print(f"{name:<44} {c:>+14.3f} {b:>8.1%} {st:>11.1%} {cr:>12.1%}")
print("-" * 96)
print("Population baselines: group B 30.0% | stress-sensitive 25.0% | true competence identical across groups.")
print("Each S1-S4 isolates one mechanism against S0. Illustrative under stated assumptions; see VALIDATION.md.")
