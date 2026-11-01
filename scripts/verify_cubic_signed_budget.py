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
    allocations = {j: [[jm, jh] for jm in range(3) for jh in range(3)
                       if (jm-jh) % 3 == j] for j in [1, 2]}
    for j, pairs in allocations.items():
        assert len(pairs) == 3
        assert all(jm+2*jh >= j for jm, jh in pairs)
    small_core_cutoff = q(1, 25)
    small_core_power = cube_selected+q(2, 3)*small_core_cutoff
    assert small_core_power == q(29, 100)
    assert q(8797, 30000)-small_core_power == q(97, 30000)
    # Source/compensator cross phases change g^2*m/h to g*m/h.
    for ea, eb in [(1, 0), (0, 1)]:
        cross = 2*ea+eb
        assert (2*(ea-eb)+cross-(ea-eb)) % 3 == 0
    for old_core in range(3):
        new_core = (old_core+1) % 3
        assert new_core >= old_core-2
    lift_cases = 0
    for completion_valuation in range(6):
        for extracted_valuation in [0, 1]:
            assert 2+3*completion_valuation-extracted_valuation >= 1
            lift_cases += 1
    support_cases = 0
    for nv in range(6):
        for gv, fv in [(0, 0), (1, 0), (0, 1)]:
            dv = 2*gv+3*nv
            if dv == 0:
                continue
            for vv in range(1+(fv == 0)):
                assert dv-vv >= 2*nv+gv
                support_cases += 1
    extracted_core_lower = small_core_cutoff-2*q(1, 100)
    assert extracted_core_lower == q(1, 50)
    Gg, Ga, Gb, xa, xb, Ra, Rb, An, mg, ma = s.symbols(
        'Gg Ga Gb xa xb Ra Rb An mg ma', nonzero=True)
    # alpha(g)^(-1)=mu(g)*G(g)^(-3), and likewise for a.
    source_phase = ((Gg*Ga*xa**2)*(Gg*Gb*xb**2)**2
                    *mg*ma/(Gg**3*Ga**3*An**3))
    initial_row = Ra/Rb*xa**2/xb**2
    target_phase = mg*ma/Ga*Gb/An**3*Ra/Rb*xa/xb
    phase_quotient = s.cancel(source_phase*(Ga/Gb)*initial_row/target_phase)
    assert phase_quotient == xa**3*xb**3
    assert 1-q(3, 2)*q(1, 100) == q(197, 200)
    assert q(73, 100)-q(1, 100) == q(18, 25)
    assert 1-q(73, 100)-q(3, 2)*q(1, 100) == q(51, 200)
    ng, na, nb, nn = s.symbols('ng na nb nn', positive=True)
    denominator = s.sqrt(ng*na)*nn*(ng*na*nn**3)*(ng*nb)/s.sqrt(na*nb)
    assert s.simplify(denominator-ng**q(5, 2)*na*s.sqrt(nb)*nn**4) == 0
    # Re-expanding the lift: q_l times its k range H/q_l cancels exactly.
    source_C = 1/(ng*nn**3)  # Z factor is recorded separately.
    scalar = 1/(ng**q(5, 2)*nn**4*s.sqrt(source_C))
    assert s.simplify(scalar-ng**(-2)*nn**q(-5, 2)) == 0
    benchmarks = []
    for saving, cutoff in [(q(1, 20), q(2, 25)), (q(2, 25), q(1, 25))]:
        signed_power = q(37, 100)-saving
        small_power = q(79, 300)+2*cutoff/3
        direct = max(signed_power, small_power)
        benchmarks.append({'signed_saving': str(saving), 'small_core_cutoff': str(cutoff),
                           'small_core_power': str(small_power),
                           'full_direct_power': str(direct),
                           'extracted_conductor_lower_power': str(cutoff/2-q(1, 100))})
    assert q(8, 25)+q(41, 75) == q(13, 15)
    assert q(8, 25)-q(19, 60) == q(1, 300)
    assert q(8797, 30000)-q(29, 100) == q(97, 30000)
    full_outside_power = (a2-a)/2-b-q(1, 2)+(a+b)+(1-a2)
    assert s.expand(full_outside_power-(1+a-a2)/2) == 0
    assert full_outside_power.subs(selected) == q(37, 100)
    gram = s.Matrix([[1, 1], [1, 1]])
    assert gram.eigenvals() == {0: 1, 2: 1}
    assert gram[0, 0] == gram[1, 1] == gram[0, 1] == 1

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
            'local_nontrivial_core_allocations': {str(j): pairs for j, pairs in allocations.items()},
            'small_core_cutoff_power': str(small_core_cutoff),
            'small_core_sector_power': str(small_core_power),
            'small_core_margin_below_target': str(q(97, 30000)),
            'remaining_good_conductor_lower_power': str(small_core_cutoff/2),
            'extracted_row_class': 'g*m/h, g=gcd(c,s)',
            'overlap_phase_quotient_before_cubic_reduction': str(phase_quotient),
            'overlap_lift_valuation_fixtures': lift_cases,
            'completion_overlap_support_fixtures': support_cases,
            'completion_overlap_support': 'g*n^2 divides h',
            'extracted_inverse_column_lower_power': '197/200',
            'extracted_label_column_lower_power': '18/25',
            'extracted_column_ratio_lower_power': '51/200',
            'extracted_core_lower_power': str(extracted_core_lower),
            'extracted_good_conductor_lower_power': str(extracted_core_lower/2),
            'noncube_complement_bound_proved': False,
        },
        'full_probe_direct_estimate_proved': False,
        'full_signed_contract': {
            'source': 'research/cubic-signed-correlation-contract.md',
            'summable_scalar_exponents': ['g^(-2)', 'n^(-5/2)'],
            'outside_full_correlation_power': '37/100',
            'benchmarks': benchmarks,
            'conditional_zero_free_thresholds': ['13/15', '21/25'],
            'signed_contract_proved': False,
            'diagonal_norm_countermodel': [[1, 1], [1, 1]],
        },
    }
    path = Path(__file__).resolve().parents[1]/'results/cubic-signed-budget.json'
    if args.write:
        path.write_text(json.dumps(receipt, indent=2)+'\n')
    else:
        assert json.loads(path.read_text()) == receipt
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
