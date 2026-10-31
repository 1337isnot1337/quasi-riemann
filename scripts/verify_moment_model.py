#!/usr/bin/env python3
"""Check higher-moment accounting and a sharp black-box obstruction."""
import json
import sympy as s

if not __debug__:
    raise RuntimeError("Verification requires assertions enabled; omit -O/PYTHONOPTIMIZE.")


def main():
    m, R, q, C, T = s.symbols("m R q C T", positive=True)
    exponent = (1 - 1/m)*R + T/m - 2*q*C/m
    fourth = s.Rational(3, 4)*R + s.Rational(1, 4) - q*C/2
    inferred_T = m/4 + (1-m/4)*R + (2-m/2)*q*C
    assert s.factor(exponent.subs(T, inferred_T) - fourth) == 0
    assert s.factor(exponent.subs(m, 4) - (3*R+T)/4 + q*C/2) == 0

    # Literal arrays saturate the fourth-moment/cardinality Holder inequality.
    U, values, weights = 64, [2, 2, 2, 2], [1, 1, 1, 1]
    moment4 = sum(x**4*w**2 for x, w in zip(values, weights))
    moment6 = sum(x**6*w**2 for x, w in zip(values, weights))
    assert moment4 == U and moment6 == 4*U > U
    assert sum(values)**4 == len(values)**3 * moment4

    root = s.sqrt(1081)
    c = (75+root)/852
    h = s.Rational(32, 71) + s.Rational(838, 76751)*root
    ell = 4*c-s.Rational(1, 3)
    y = h-2*ell
    n = s.simplify(1-y/h)
    # A 2k-th moment written as a squared polynomial needs k ordinary copies.
    def ordinary_cost(order):
        return s.simplify(order*n/2)
    def capacity(order):
        return s.simplify((1-ordinary_cost(order))/2)
    assert ordinary_cost(4) < 1 < ordinary_cost(6)
    assert capacity(4) > 0 > capacity(6)
    print(json.dumps({
        "status": "accounting and black-box obstruction passed; analytic lift unproved",
        "weighted_holder_exponent": str(exponent),
        "sharp_inferred_moment_exponent": str(inferred_T),
        "inferred_moment_recovers_fourth_exactly": True,
        "finite_extremizer": {"U": U, "row_values": values,
                              "fourth_moment": moment4, "sixth_moment": moment6},
        "ordinary_support_cost_fourth": str(s.N(ordinary_cost(4), 24)),
        "ordinary_support_cost_sixth": str(s.N(ordinary_cost(6), 24)),
        "sixth_unit_budget_selected_capacity": str(s.N(capacity(6), 24)),
        "support_model_scope": "direct polynomial-product realization, not all analytic methods",
    }, indent=2))


if __name__ == "__main__":
    main()
