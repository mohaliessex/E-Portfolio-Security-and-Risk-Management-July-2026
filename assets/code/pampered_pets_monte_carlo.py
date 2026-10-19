"""
Reproducibility script for the Unit 11 executive summary:
"Quantitative Risk Assessment of Digitalisation, the International Supply Chain
and Disaster Recovery at Pampered Pets".

Added to the e-portfolio after tutor feedback, which asked for simulation code so
that the results, particularly the correlated scenario, can be audited.

Method (Appendix A of the executive summary)
- Each risk's annual probability p_i is uncertain and described by a three-point
  estimate (min, most likely, max), modelled as a PERT distribution.
- Baseline (analytic aggregation): in each iteration, sample every p_i and compute
  P(at least one) = 1 - prod(1 - p_i). Report the mean and 5th/95th percentiles.
  "Two or more" is computed exactly from the sampled p_i (Poisson-binomial).
- Correlated sensitivity: event occurrence simulated as Bernoulli draws driven by
  correlated standard normals (Gaussian copula, rho = 0.3 between all pairs), with
  each event's threshold set from the sampled p_i.

The tutor noted that the correlated scenario uses a different procedure from the
baseline. To make the comparison like-for-like, this script also runs the
independent case with the same Bernoulli procedure (rho = 0), which should agree
with the analytic baseline. Any difference between rho = 0 and rho = 0.3 is then
attributable to correlation alone.

Run:  python pampered_pets_monte_carlo.py
"""
import numpy as np
from scipy.stats import norm

N = 100_000
SEED = 2026

QUALITY = {  # inherent min, most likely, max (%)
    "Q1 Transit temperature or humidity excursion": (10, 25, 45),
    "Q2 Warehouse stock-rotation or mis-pick error": (5, 15, 30),
    "Q3 Counterfeit or adulterated product": (2, 6, 15),
    "Q4 Undetected supplier recipe change": (3, 8, 20),
    "Q5 Deliberate tampering": (0.5, 1, 3),
    "Q6 Product or batch record error spread digitally": (5, 12, 25),
}
SUPPLY = {
    "S1 Logistics or customs delay over two weeks": (20, 35, 55),
    "S2 Cyber attack disrupting operations": (5, 12, 25),
    "S3 Personal data breach, including royal data": (4, 10, 22),
    "S4 Cloud or platform outage (before DR)": (5, 15, 30),
    "S5 Warehouse automation failure over 48 hours": (5, 12, 25),
    "S6 Import or regulatory stoppage": (5, 12, 25),
    "S7 Third-party software compromise": (3, 8, 18),
    "S8 Key supplier failure": (3, 8, 15),
    "S9 Fulfilment overload for four staff": (10, 20, 40),
}
RESIDUAL = {  # post-control estimates (Table A1)
    "Q1": (4, 10, 20), "Q2": (2, 5, 10), "Q3": (1, 3, 7), "Q4": (1, 3, 8),
    "Q5": (0.3, 0.6, 1.5), "Q6": (2, 5, 10),
    "S1": (15, 25, 40), "S2": (2, 5, 10), "S3": (2, 4, 9), "S4": (0.5, 1, 3),
    "S5": (2, 5, 10), "S6": (2, 5, 10), "S7": (2, 4, 9), "S8": (2, 5, 10),
    "S9": (5, 10, 20),
}


def pert(rng, a, m, b, size):
    """Sample a PERT(a, m, b) distribution, inputs in percent, output as probability."""
    alpha = 1 + 4 * (m - a) / (b - a)
    beta = 1 + 4 * (b - m) / (b - a)
    return (a + (b - a) * rng.beta(alpha, beta, size)) / 100


def sample_probs(rng, estimates):
    return np.column_stack([pert(rng, *est, N) for est in estimates])


def analytic(p):
    """P(>=1) and P(>=2) per iteration from sampled probabilities (independent events)."""
    none = np.prod(1 - p, axis=1)
    exactly_one = np.zeros(len(p))
    for i in range(p.shape[1]):
        others = np.prod(np.delete(1 - p, i, axis=1), axis=1)
        exactly_one += p[:, i] * others
    return 1 - none, 1 - none - exactly_one


def bernoulli(rng, p, rho):
    """Simulate event occurrence with a Gaussian copula (rho between all pairs)."""
    k = p.shape[1]
    cov = np.full((k, k), rho) + np.eye(k) * (1 - rho)
    z = rng.multivariate_normal(np.zeros(k), cov, size=len(p))
    events = z < norm.ppf(p)
    count = events.sum(axis=1)
    return (count >= 1).mean(), (count >= 2).mean()


def summarise(name, x):
    lo, hi = np.percentile(x, [5, 95])
    return f"{name}: mean {x.mean():.1%} (90% interval {lo:.0%}-{hi:.0%})"


def run(label, groups):
    rng = np.random.default_rng(SEED)
    print(f"\n=== {label} ===")
    for gname, est in groups.items():
        p = sample_probs(rng, list(est))
        at1, at2 = analytic(p)
        print(summarise(f"P(at least one {gname} event)", at1))
        print(f"P(two or more {gname} events): {at2.mean():.1%}")
        b0 = bernoulli(rng, p, 0.0)
        b3 = bernoulli(rng, p, 0.3)
        print(f"  Bernoulli check, rho = 0.0: >=1 {b0[0]:.1%}, >=2 {b0[1]:.1%}")
        print(f"  Correlated,      rho = 0.3: >=1 {b3[0]:.1%}, >=2 {b3[1]:.1%}")


def control_sensitivity():
    """Tutor feedback: test the assumed control reductions.
    Effectiveness e scales each residual estimate towards the inherent one:
    e = 1.0 is the residual case in the report, e = 0.5 means controls deliver
    half the assumed reduction, e = 0.0 means no reduction at all."""
    inherent = {k.split()[0]: v for k, v in {**QUALITY, **SUPPLY}.items()}
    print("\n=== Sensitivity of residual results to control effectiveness ===")
    for e in (1.0, 0.75, 0.5, 0.25, 0.0):
        rng = np.random.default_rng(SEED)
        row = []
        for ids in (("Q1", "Q2", "Q3", "Q4", "Q5", "Q6"),
                    ("S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9")):
            est = [tuple(i - e * (i - r) for i, r in zip(inherent[k], RESIDUAL[k])) for k in ids]
            at1, _ = analytic(sample_probs(rng, est))
            row.append(at1.mean())
        print(f"  effectiveness {e:.0%}: quality >=1 {row[0]:.1%}, supply >=1 {row[1]:.1%}")


if __name__ == "__main__":
    rng = np.random.default_rng(SEED)
    print("Individual risks (inherent): mean and 90% interval")
    for name, est in {**QUALITY, **SUPPLY}.items():
        print("  " + summarise(name, pert(rng, *est, N)))
    run("Inherent (before Section 4 controls)", {"quality": QUALITY.values(), "supply": SUPPLY.values()})
    run("Residual (after Section 4 controls)", {
        "quality": [RESIDUAL[k] for k in ("Q1", "Q2", "Q3", "Q4", "Q5", "Q6")],
        "supply": [RESIDUAL[k] for k in ("S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9")],
    })
    control_sensitivity()
