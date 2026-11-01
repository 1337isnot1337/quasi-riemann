#!/usr/bin/env python3
"""Exact local identities and decay certificates, not a global row estimate."""
import argparse
from itertools import product
import json
from pathlib import Path

import sympy as S

if not __debug__:
    raise RuntimeError("Verification requires assertions enabled.")

D, W, V, R, Q, T = S.symbols("D W V R Q T")
x, s, z = S.symbols("x s z")
X = (S.Rational(51, 100), S.Rational(7, 8))
SIGMA = (S.Rational(99, 100), S.Rational(101, 100))
Z = S.Rational(17, 50)


def equal(left, right):
    assert S.cancel(left - right) == 0


def lower_bound(expr, x_range=X, sigma_range=SIGMA, z_min=Z):
    """Affine function on a rectangle times a half-line; all-size proof."""
    poly = S.Poly(expr, x, s, z)
    assert poly.total_degree() <= 1
    assert S.diff(expr, z) >= 0
    return min(expr.subs({x: a, s: b, z: z_min})
               for a, b in product(x_range, sigma_range))


def decay_certificate(numerator, x_range, z_min, target):
    rows = []
    for term in S.Add.make_args(S.expand(numerator)):
        powers = term.as_powers_dict()
        ds, ws, ts, vs, rs, qs = [powers.get(a, 0)
                                for a in (D, W, T, V, R, Q)]
        assert all(n >= 0 for n in (ds, ws, ts, vs, rs))
        decay = S.expand((ds-ws+6*rs)*x + (ws+ts)*s + (6*vs+6*rs)*z-4*rs-qs)
        lo = lower_bound(decay, x_range=x_range, z_min=z_min)
        assert lo >= target
        rows.append({"term": str(term), "decay": str(decay), "minimum": str(lo)})
    return rows


def certificate():
    t = D * W
    p = (1 / (1 - V) + W / (1 - W)
         + ((R * (1 - 1 / Q) - (Q - 1) * t * V) / (1 - V)
            - D + W * R) / (1 - R))
    h = S.cancel(p * (1 - V) * (1 - W) / (1 - D))
    base = 1 - D + t
    e = (V * (D * (1 - W) * (1 + W - Q * W) - W)
         + R * (base - (1 - V) * W**2 + (W - 1) / Q))
    equal(h, base / (1 - D) + e / ((1 - R) * (1 - D)))
    equal(((1 - t) * h - 1) * (1 - R) * (1 - D),
          (1 - R) * t * (D - t) + (1 - t) * e)
    numerator = S.expand(S.cancel(((1 - t) * h - 1) * (1 - R) * (1 - D)))
    unramified = decay_certificate(numerator, X, Z, S.Rational(11, 10))
    assert len(unramified) == 20
    assert min(S.Rational(row["minimum"]) for row in unramified) == S.Rational(11, 10)

    # Valuation one has D=W=0, but T=eta*Q^(-x-w) remains nonzero.
    h1 = (1 + T - Q*T*V - R/Q) / (1 - R)
    source_h1 = 1 + (R*(1-1/Q)-(Q-1)*T*V+(1-V)*T)/(1-R)
    equal(h1, source_h1)
    n1 = -T**2 - Q*T*V + Q*T**2*V + R - R/Q + R*T/Q
    equal(((1 - T) * h1 - 1) * (1 - R), n1)
    valuation_one = decay_certificate(n1, X, Z, S.Rational(11, 10))

    # A second extraction reaches the neighborhood of the z=1/6 residue.
    # H = L(s,eta)/L(s+6z-1,eta) * K2 globally on the overlap.
    x2 = (S.Rational(4, 5), S.Rational(7, 8))
    z2 = S.Rational(33, 200)
    k2 = (1-t)*h/(1-Q*t*V)
    n2 = S.expand(S.cancel((k2-1)*(1-R)*(1-D)*(1-Q*t*V)))
    n2_rows = decay_certificate(n2, x2, z2, S.Rational(219, 200))
    assert len(n2_rows) == 22
    assert min(S.Rational(row["minimum"]) for row in n2_rows) == S.Rational(219, 200)
    k21 = (1-T)*h1/(1-Q*T*V)
    n21 = S.expand(S.cancel((k21-1)*(1-R)*(1-Q*T*V)))
    equal(n21, n1+Q*T*V*(1-R))
    n21_rows = decay_certificate(n21, x2, z2, S.Rational(219, 200))
    denominator_decay = lower_bound(s+6*z-1, x_range=x2, z_min=z2)
    assert denominator_decay == S.Rational(49, 50)

    # R is itself an Euler coordinate of a fixed angular Hecke character.
    # Extracting its full geometric factor removes the next local wall.
    k3 = (1-R)*k2
    n3 = S.expand(S.cancel((k3-1)*(1-D)*(1-Q*t*V)))
    n3_rows = decay_certificate(n3, X, z2, S.Rational(101, 100))
    assert len(n3_rows) == 18
    assert min(S.Rational(row["minimum"]) for row in n3_rows) == S.Rational(101, 100)
    k31 = (1-R)*k21
    n31 = S.expand(S.cancel((k31-1)*(1-Q*T*V)))
    equal(n31, -T**2+Q*T**2*V-R/Q+R*T/Q)
    n31_rows = decay_certificate(n31, X, z2, S.Rational(101, 100))

    # All terms in J_j for j>=2 decay, but (Q-1)*T can grow left of s=1.
    boundary = {"2": [3*x-S.Rational(3, 2)],
                "3": [2*x+s-2, 4*x-2],
                "4": [3*x+s-S.Rational(5, 2)], "5": [6*x-3]}
    ramified = {j: [str(lower_bound(v)) for v in values]
                for j, values in boundary.items()}
    assert ramified == {"2": ["3/100"], "3": ["1/100", "1/25"],
                        "4": ["1/50"], "5": ["3/50"]}
    ramified2 = {j: [str(lower_bound(v, x_range=x2, z_min=z2)) for v in values]
                 for j, values in boundary.items()}
    assert all(S.Rational(value) > 0 for values in ramified2.values() for value in values)
    # All-size norm cost: primes with valuation >=2 have rad <= N(u)^1/2.
    assert all(1 <= S.Rational(j, 2) for j in range(2, 6))

    equal(h.subs({R: 0, V: 0}), 1 + t / (1 - D))
    equal(((1-t)*h-1).subs({R: 0, V: 0}), t*(D-t)/(1-D))
    assert lower_bound(s) <= 1  # unregularized leading DW is not summable.
    # At a repeated prime and s<1 the term Q*T cannot be declared bounded.
    assert (1-s).subs(s, SIGMA[0]) > 0
    return {
        "status": "local Euler regularization and affine decay certificate",
        "region": {"Re(x)": list(map(str, X)), "Re(x+w)": list(map(str, SIGMA)),
                   "Re(z)_minimum": str(Z)},
        "extracted_factor": "L_eta^S(x+w)",
        "unramified_numerator": unramified,
        "valuation_one_numerator": valuation_one,
        "J_j_minimum_decay": ramified,
        "uniform_local_decay": "11/10",
        "second_extraction": {
            "extracted_ratio": "L_eta^S(x+w)/L_eta^S(x+w+6z-1)",
            "region": {"Re(x)": list(map(str, x2)), "Re(x+w)": list(map(str, SIGMA)),
                       "Re(z)_minimum": str(z2)},
            "unramified_numerator": n2_rows,
            "valuation_one_numerator": n21_rows,
            "uniform_local_decay": "219/200",
            "extra_denominator_decay": str(denominator_decay),
            "J_j_minimum_decay": ramified2,
        },
        "angular_extraction": {
            "additional_factor": "L^S(6x+6z-4, eta^6*alpha_bar^6)",
            "region": {"Re(x)": list(map(str, X)), "Re(x+w)": list(map(str, SIGMA)),
                       "Re(z)_minimum": str(z2)},
            "unramified_numerator": n3_rows,
            "valuation_one_numerator": n31_rows,
            "uniform_local_decay": "101/100",
            "extra_denominator_decay": str(denominator_decay),
            "J_j_minimum_decay": ramified,
        },
        "row_growth": "N(u)^(max(0,1-Re(x+w))/2+epsilon)",
        "negative_controls": ["unremoved DW term", "repeated-prime growth below the diagonal"],
        "new_zero_free_bound_proved": False,
        "global_signed_row_sum_bounded": False,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    receipt = certificate()
    path = Path(__file__).resolve().parents[1] / "results/euler-regularization.json"
    if args.write:
        path.write_text(json.dumps(receipt, indent=2) + "\n")
    else:
        assert json.loads(path.read_text()) == receipt
    print(json.dumps({k: receipt[k] for k in (
        "status", "uniform_local_decay", "row_growth", "new_zero_free_bound_proved")}, indent=2))


if __name__ == "__main__":
    main()
