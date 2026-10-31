#!/usr/bin/env python3
"""Exact identities for the inherited exponent model; no L-function claim."""
import json
import sympy as s

if not __debug__:
    raise RuntimeError("Verification requires assertions enabled; omit -O/PYTHONOPTIMIZE.")

Q = s.Rational
delta, p, B, L, z, kappa = s.symbols("delta p B L z kappa", real=True)
c, h, a, d = s.symbols("c h a d", real=True)
V = Q(5, 6) - delta


def counts(B, L, capped=False, z=0):
    D = 3 - p if capped else 3 - p - 4 * p / L
    A = 2 if capped else 2 - 4 * p / L
    U = (1 - p) * (1 - 2 * p * (z if capped else B / L))
    J = V * D + delta * (1 - p) * A
    N = (1 - delta) * J + V * delta * U
    T = J + delta * U
    Z = 2 * p * (z if capped else B / L)
    MN = D * T - (A * T + (Z - p) * J)
    return D, J, N, MN


def equal(actual, expected, label):
    remainder = s.factor(actual - expected)
    if remainder != 0:
        raise AssertionError(f"{label}: {remainder}")


def main():
    D, Ju, Nu, _ = counts(B, L)
    Dc, Jc, Nc, MNc = counts(B, L, True, z)
    G = (B - L * z) * Dc * Jc / 2 - MNc
    equal((Nc * Ju - Nu * Jc) * Dc * L,
          4 * delta * p * V * (1 - p) * G, "cap dominance")
    equal(s.diff(Nu / Ju, B),
          -2 * p * V * delta * (1 - p) / (L * Ju), "B monotonicity")
    equal(s.diff(Nu / Ju, L).subs(B, 1),
          2 * delta * p * V**2 * (1 - p)**2 / (L**2 * Ju.subs(B, 1)**2),
          "Lambda monotonicity at B=1")

    # Include inherited faces with Lambda<2 but Lambda/B>=2.
    w = s.Symbol("w", positive=True)
    _, Jb, Nb, _ = counts(B, B*w)
    _, Jone, None_, _ = counts(s.Integer(1), w)
    equal(Nb*Jone-None_*Jb,
          4*V*delta*p*(1-p)*(1-2*p/w)*(V+delta*(1-p))*(1-B)/(B*w),
          "normalized-face dominance")

    _, J, N, _ = counts(s.Integer(1), s.Integer(2))
    oldD = 3 - p - 2 * p / (3 * kappa)
    oldC = 2 * (1 - p) * (1 - p / (3 * kappa))
    Jo = V * oldD + delta * oldC
    No = (1 - delta) * Jo + delta * oldC * V / 2
    equal(No * J - N * Jo,
          delta * p * V**2 * (3 * kappa - 1) * (1 - p)**2 / (3 * kappa),
          "old-count dominance")

    ell = 4 * c - Q(1, 3)
    y = h - 2 * ell
    # Optimistic affine physical capacity: ignoring clipping only helps.
    cap = (2 * y - d) / 2
    equal((2*y-(2-B)*d)/(2*B)-cap, (1-B)*(y-d)/B,
          "normalized physical-capacity dominance")
    E = (Q(1, 2) + (a - Q(1, 6)) * h - y / 2 - ell / 2
         + (Q(1, 4) - a) * d + delta / 2
         + delta * p * (ell - cap / 2) + Q(3, 4) * d * N / J)
    top = s.factor(E.subs(d, h))
    equal(s.diff(top, a), 0, "contour cancels at d=h")
    F = s.factor((J * (1 - c - top)).subs(p, Q(1, 2)))
    expected = (192*c*delta**2 - 96*c*delta - 180*c - 33*delta**2*h
                + 8*delta**2 + 61*delta*h - 42*delta - 20*h + 40) / 48
    equal(F, expected, "top numerator")

    root = s.sqrt(1081)
    ds = (61 - root) / 66
    cs = (75 + root) / 852
    hs = Q(32, 71) + Q(838, 76751) * root
    A = s.simplify(-s.diff(F, c).subs(delta, ds))
    equal(F.subs(delta, ds), A * (cs - c), "universal-h obstruction")
    equal(s.diff(F, delta).subs({delta: ds, c: cs, h: hs}), 0, "stationarity")
    equal(s.diff(F, h).subs(delta, ds), 0, "h cancellation at saddle")
    assert A > 0 and 0 < ds < Q(3, 4) and Q(1, 2) < 1 - cs < Q(7, 8)

    # An independent exact reduction in Q[t]/(t^2-1081), without radical simplification.
    t = s.Symbol("t")
    expr = 48 * (expected.subs(delta, (61-t)/66)
                 - ((Q(5179, 4356) + Q(89, 1089)*t)
                    * ((75+t)/852-c)))
    assert s.rem(s.Poly(s.expand(expr), t), s.Poly(t*t-1081, t)).is_zero
    # The rational isolating interval certifies the signs used in the proof.
    lo, hi = Q(32878, 1000), Q(32879, 1000)
    assert lo*lo < 1081 < hi*hi and 0 < lo < hi < 61

    plain = s.simplify(1 - (hs - 2*(4*cs-Q(1, 3))) / hs)
    assert s.simplify(plain - Q(1, 3)) > 0
    print(json.dumps({
        "status": "exact model identities passed; no improved L-function bound",
        "theta_contact": str(1-cs),
        "theta_decimal": str(s.N(1-cs, 32)),
        "delta_contact": str(ds),
        "delta_decimal": str(s.N(ds, 25)),
        "h_contact": str(hs),
        "plain_length_decimal": str(s.N(plain, 25)),
        "sixth_three_factor_length_decimal": str(s.N(3*plain, 25)),
        "identity_checks": 12,
        "source_face_scope": "0<B<=1, Lambda>1, Lambda>=2B; positive admitted denominators",
        "independent_polynomial_quotient_check": True,
        "upstream_lean_rebuilt": False,
    }, indent=2))


if __name__ == "__main__":
    main()
