#!/usr/bin/env python3
"""Exact limits of a specified separate-mean cubic model; no analytic bound."""
import argparse
import json
from pathlib import Path
import sympy as s

if not __debug__:
    raise RuntimeError('Verification requires assertions enabled.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    q = s.Rational
    a, b, a2, M, Fc, Fs, theta = s.symbols('a b a2 M Fc Fs theta', real=True)
    # One Poisson transform, with all Z^(1-a2) second frequencies charged.
    low = (a2-a-1)/2-b+(1-a2)+(Fc+Fs)/2
    signal = theta-q(5, 6)+(a+a2)/6
    required = s.expand(low-signal+theta).subs(b, M-a).expand()
    lower = q(2, 3)-M/3+Fc/2
    mixed = (4*M-2*a)/3
    assert s.expand(required-lower-q(2, 3)*(1-a2)-(Fs-mixed)/2) == 0

    # Paper 77's curved envelope is above its tangent linear branch.
    line = 2*M/5+q(13, 15)
    radicand = 6-3*M
    positive = q(79, 30)-9*M/10
    assert positive.subs(M, q(29, 27)) == q(5, 3)
    assert s.factor(positive**2-radicand) == (27*M-29)**2/900
    assert s.expand(q(7, 2)-M/2-line-positive) == 0

    crossing, floor = q(13, 9), q(49, 54)
    assert line.subs(M, crossing) == crossing
    assert s.expand(lower.subs(Fc, line)-floor-2*(crossing-M)/15) == 0
    assert s.expand(lower.subs(Fc, M)-floor-(M-crossing)/6) == 0
    assert lower.subs(Fc, 2*(M+1)/3) == 1

    # Both active comparisons meet at this admissible limiting point.
    optimum = {M: crossing, a: crossing/2, a2: 1, Fc: crossing, Fs: crossing}
    assert s.simplify(required.subs(optimum)) == floor
    selected = {a: q(73, 100), b: q(73, 100), a2: q(99, 100),
                Fc: q(73, 50), Fs: q(73, 50)}
    selected_theta = s.simplify((low-signal+theta).subs(selected))
    assert selected_theta == q(11, 12)
    assert selected_theta-q(21, 25) == q(23, 300)

    # Universal tame cubic Gauss bound, including principal unit masks.
    gauss_cases = 0
    for norm in [7, 13, 19, 25, 31]:
        for modulus_valuation in range(1, 9):
            for frequency_valuation in range(modulus_valuation+2):
                bound_sq = norm**(modulus_valuation+min(modulus_valuation,
                                                       frequency_valuation))
                primitive_sq = (norm**(2*modulus_valuation-1)
                                if frequency_valuation == modulus_valuation-1 else 0)
                principal_sq = ((norm**modulus_valuation-norm**(modulus_valuation-1))**2
                                if frequency_valuation >= modulus_valuation else
                                norm**(2*modulus_valuation-2)
                                if frequency_valuation == modulus_valuation-1 else 0)
                assert primitive_sq <= bound_sq and principal_sq <= bound_sq
                gauss_cases += 2
    cube_power = q(7, 6)-(a+b)/6-2*a2/3
    cube_selected = s.simplify(cube_power.subs(selected))
    assert cube_selected == q(79, 300)
    assert q(8797, 30000)-cube_selected == q(299, 10000)

    # Literal phase matching with one common cubic row power is impossible.
    assert not any(k % 3 == 1 and k % 3 == 2 for k in range(3))
    receipt = {
        'status': 'exact separate-mean exponent model; no improved L-function bound',
        'imported_norm': 'Paper 77 v1 Theorem 2, conditional on its ZF',
        'unproved_grants': ['all target twists', 'all growing second-frequency twists',
                            'natural-row ordinary-Gauss comparator Fs',
                            'free completion/overlap reconstruction and profile separation'],
        'row_exponent': 'M=a+b',
        'second_frequency_count_exponent': '1-a2',
        'ordinary_mean_exponent': 'max(M,b,2*(M+b)/3)',
        'long_mean_exponent_for_1_to_2':
            'max(M,7/2-M/2-sqrt(6-3*M)) to 29/27; max(M,2*M/5+13/15) thereafter',
        'theta_required': str(required),
        'curved_above_linear_certificate': str(s.factor(positive**2-radicand)),
        'limiting_optimum': {'M': str(crossing), 'a': str(crossing/2),
                             'b': str(crossing/2), 'a2': '1'},
        'theta_infimum': str(floor),
        'signed_saving_to_087': str(floor-q(87, 100)),
        'signed_saving_to_084': str(floor-q(21, 25)),
        'selected_084_geometry_cauchy_threshold': str(selected_theta),
        'selected_084_geometry_signed_saving': str(q(23, 300)),
        'selected_084_geometry_saving_with_reserve': str(q(23, 300)+q(1, 10000)),
        'literal_centered_source_orientation_match': False,
        'physical_cube_ratio_sector': {
            'scope': 'written full-sector bound, all completions and overlaps; not Lean formalized',
            'gauss_prime_power_fixtures': gauss_cases,
            'general_power': str(cube_power),
            'selected_084_power': str(cube_selected),
            'margin_below_reserved_direct_target': str(q(299, 10000)),
            'noncube_complement_bound_proved': False,
        },
        'full_probe_direct_estimate_proved': False,
    }
    path = Path(__file__).resolve().parents[1]/'results/cubic-signed-budget.json'
    if args.write:
        path.write_text(json.dumps(receipt, indent=2)+'\n')
    else:
        assert json.loads(path.read_text()) == receipt
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
