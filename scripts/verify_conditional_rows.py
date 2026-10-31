#!/usr/bin/env python3
"""Exact full-domain exponent certificate CONDITIONAL on an unproved count.

Bernstein coefficients are computed with Fraction arithmetic. No float, grid
sampling, or optimizer is used to certify the inequalities.
"""
import argparse
from fractions import Fraction as Q
import json
from math import comb
from pathlib import Path
import sympy as s

if not __debug__:
    raise RuntimeError("Verification requires assertions enabled; omit -O/PYTHONOPTIMIZE.")

ROOT = Path(__file__).resolve().parents[1]
delta, p = s.symbols("delta p")


def rat(x):
    return Q(int(s.numer(x)), int(s.denom(x)))


def bernstein_bounds(terms, degree, box):
    nx, ny = degree
    a, b, c, d = box
    power = [[Q(0) for _ in range(ny+1)] for _ in range(nx+1)]
    for (u, v), coefficient in terms.items():
        for i in range(u+1):
            for j in range(v+1):
                power[i][j] += (coefficient * comb(u, i) * a**(u-i) * (b-a)**i
                                * comb(v, j) * c**(v-j) * (d-c)**j)
    coefficients = [sum((power[u][v] * Q(comb(i, u), comb(nx, u))
                         * Q(comb(j, v), comb(ny, v))
                         for u in range(i+1) for v in range(j+1)), Q(0))
                    for i in range(nx+1) for j in range(ny+1)]
    return min(coefficients), max(coefficients), coefficients


def verify_representation(terms, degree, box, coefficients):
    """Exact unisolvent evaluation proves equality to the Bernstein expansion."""
    nx, ny = degree
    a, b, c, d = box
    for i in range(nx+1):
        t = Q(i, max(1, nx))
        for j in range(ny+1):
            w = Q(j, max(1, ny))
            x, y = a+(b-a)*t, c+(d-c)*w
            original = sum((v*x**u*y**k for (u, k), v in terms.items()), Q(0))
            reconstructed = sum((coefficients[u*(ny+1)+v]
                                 * comb(nx, u)*t**u*(1-t)**(nx-u)
                                 * comb(ny, v)*w**v*(1-w)**(ny-v)
                                 for u in range(nx+1) for v in range(ny+1)), Q(0))
            assert original == reconstructed, "Invalid Bernstein representation"


def certify(expression):
    poly = s.Poly(s.cancel(expression), delta, p)
    terms = {powers: rat(coefficient) for powers, coefficient in poly.terms()}
    degree = (int(poly.degree(delta)), int(poly.degree(p)))
    leaves = []

    def visit(box, depth):
        lower, upper, coefficients = bernstein_bounds(terms, degree, box)
        if lower > 0:
            verify_representation(terms, degree, box, coefficients)
            leaves.append({"box": [str(x) for x in box], "lower": str(lower)})
            return
        if upper <= 0 or depth >= 12:
            raise AssertionError(f"Cannot certify positive polynomial on {box}")
        a, b, c, d = box
        xmid, ymid = (a+b)/2, (c+d)/2
        for child in [(a, xmid, c, ymid), (xmid, b, c, ymid),
                      (a, xmid, ymid, d), (xmid, b, ymid, d)]:
            visit(child, depth+1)

    visit((Q(0), Q(3, 4), Q(0), Q(1, 2)), 0)
    assert sum(((Q(x["box"][1])-Q(x["box"][0]))
                * (Q(x["box"][3])-Q(x["box"][2])) for x in leaves), Q(0)) == Q(3, 8)
    return {"degree": list(degree), "leaves": leaves,
            "minimum_bernstein_lower": str(min(Q(x["lower"]) for x in leaves))}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write deterministic certificate")
    args = parser.parse_args()
    c, h = s.Rational(13, 100), s.Rational(391, 500)
    switch = s.Rational(7, 10)
    theta, ell = 1-c, 4*c-s.Rational(1, 3)
    y, x = h-2*ell, 1+ell-h
    kappa, reserve = 1-2*c, s.Rational(1, 10000)
    V = s.Rational(5, 6)-delta
    J = V*(3-3*p)+delta*(1-p)*(2-2*p)
    # UNPROVED CONTRACT: only 2/5 of the inherited correction to 1-delta remains.
    Nnew = (1-delta)*J+s.Rational(2, 5)*V*delta*(1-p)**2
    Do = 3-p-2*p/(3*kappa)
    Co = 2*(1-p)*(1-p/(3*kappa))
    Jo = V*Do+delta*Co
    No = (1-delta)*Jo+delta*Co*V/2

    def margin_numerator(d, capacity, denominator, numerator):
        base = (s.Rational(1, 2)+13*h/75-y/2-ell/2-9*d/100
                + delta/2+delta*p*(ell-capacity/2))
        return s.expand(denominator*(theta-reserve-base)-s.Rational(3, 4)*d*numerator)

    polys = {
        "ideal_count_denominator": J,
        "old_count_denominator": Jo,
        "old_zero": margin_numerator(0, 0, Jo, No),
        "old_join": margin_numerator(switch, (2*y-switch)/(6*kappa), Jo, No),
        # The old count is a conservative upper bound at the new interval's join.
        "new_join": margin_numerator(switch, s.Rational(3, 40)*switch, Jo, No),
        "new_top_CONDITIONAL": margin_numerator(h, (2*y-h)/2, J, Nnew),
    }
    assert (s.Rational(1, 6) < ell < s.Rational(1, 5)
            and ell < x < y < s.Rational(1, 2)
            and 2*x-y-ell > 0 and 1+3*ell-2*(x+y) < 0)
    floor_slack = ((50-234*c-25*h)/75
                   - s.Rational(67, 100)*s.Rational(1, 10**22))
    assert floor_slack > reserve
    assert (2*y-h)/2 < s.Rational(3, 40)*h
    assert s.Rational(3, 40)*switch < (2*y-switch)/2
    assert y < switch < min(h, 2*y) and s.Rational(2, 3) < switch
    # The modified count is below the ideal count, which is below the old count.
    assert s.factor(((1-delta)*J+V*delta*(1-p)**2)-Nnew
                    - s.Rational(3, 5)*V*delta*(1-p)**2) == 0
    Nhalf = (1-delta)*J+s.Rational(1, 2)*V*delta*(1-p)**2
    half_margin = margin_numerator(h, (2*y-h)/2, J, Nhalf)
    assert half_margin.subs({delta: s.Rational(11, 20), p: s.Rational(1, 2)}) < 0
    receipt = {
        "status": "CONDITIONAL exponent-model certificate; no improved L-function bound",
        "theta": str(theta), "h": str(h), "ell": str(ell),
        "x": str(x), "y": str(y), "reserve": str(reserve),
        "switch": str(switch),
        "unproved_count_contract": "R_new <= 1-delta + (2/5)*V*delta*(1-p)^2/J_ideal",
        "domain": "0<=delta<=3/4, 0<=p<=1/2; conductor intervals [0,7/10] and [7/10,h]",
        "geometry_checked": True,
        "floor_slack": str(floor_slack),
        "inherited_BoundsN_applicable": False,
        "analytic_reconstruction_checked": False,
        "certificates": {name: certify(poly) for name, poly in polys.items()},
    }
    path = ROOT / "results/conditional-087.json"
    if args.write:
        path.parent.mkdir(exist_ok=True)
        path.write_text(json.dumps(receipt, indent=2)+"\n")
    else:
        assert json.loads(path.read_text()) == receipt, "Stored certificate differs from replay"
    print(json.dumps({"status": receipt["status"], "theta": str(theta),
                      "reserve": str(reserve),
                      "certified_polynomials": len(polys),
                      "bernstein_leaves": sum(len(x["leaves"]) for x in receipt["certificates"].values()),
                      "unproved_count_contract": receipt["unproved_count_contract"]}, indent=2))


if __name__ == "__main__":
    main()
