#!/usr/bin/env python3
"""Exact Mellin bookkeeping for a candidate coupled Euler derivative."""
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
    x, w, z, t = s.symbols('x w z t')
    exponents = [s.Rational(1, 2)-z, w-1, x+z-1]
    multiplier = x+w-1
    assert s.expand(sum(exponents)+s.Rational(1, 2)-multiplier) == 0
    assert s.expand(-1+(1-z)+w+(x+z-1)-multiplier) == 0
    assert s.expand(multiplier.subs(w, 1-x)) == 0
    assert s.expand(multiplier.subs({w: 1, z: s.Rational(1, 6)})-x) == 0
    # Common dilation gives the sum of the three scale exponents plus a half.
    assert s.expand(s.diff(s.exp(sum(exponents)*t)*s.exp(t/2), t).subs(t, 0)
                    - multiplier) == 0
    # The inverse reciprocal's signal factor is x; its only zero is outside
    # the proposed strip Re(x)>869/1000.
    assert s.solve(multiplier.subs(w, 1), x) == [0]
    # Covered angular mode for the separate shared-label cubic construction.
    k1, k2, ell = 2, -4, 1
    assert k1 % 2 == k2 % 2 == 0 and (k1-k2) % 6 == 0
    assert ell+k1+k2 == -1
    angular_orders = [-3*k1, -3*k2, -(k1+2*k2), -(2*k1+k2)]
    assert angular_orders == [-6, 12, 6, 0]
    forms = [s.Matrix([[3, 0]]), s.Matrix([[0, 3]]),
             s.Matrix([[1, 2]]), s.Matrix([[2, 1]])]
    for i in range(4):
        for j in range(i):
            assert s.Matrix.vstack(forms[i], forms[j]).det() != 0
    a1, a2, free = s.symbols('a1 a2 free')
    t2 = 1-2*free
    v = x-s.Rational(3, 2)+free+t2
    angular_scale = s.expand(v+a1*(s.Rational(1, 2)-free)
                             +a2*(s.Rational(1, 2)-t2))
    assert s.expand(angular_scale-(x-s.Rational(1, 2)+(a1-a2)/2
                                    +(2*a2-1-a1)*free)) == 0
    # A fixed-product second aspect difference of the cubic principal signal.
    u, vv, d, L, L2 = s.symbols('u vv d L L2')
    H0, H1, H2 = s.symbols('H0 H1 H2')
    denom = 9*u*vv*(u+2*vv)*(2*u+vv)
    analytic_jet = H0+H1*vv+H2*vv**2
    contrast_jet = d**2*(vv-u)**2
    residue = s.residue(s.residue(contrast_jet*analytic_jet/denom, u, 0), vv, 0)
    assert s.simplify(residue-d**2*H0/18) == 0
    q = (L-L2)**2
    second_difference = s.expand(q.subs(L2, L2-2*d)-2*q.subs(L2, L2-d)+q)
    assert second_difference == 2*d**2
    assert s.Rational(22, 75)-s.Rational(8797, 30000) == s.Rational(1, 10000)
    receipt = {
        'status': 'exact candidate-probe Mellin identities; no improved bound',
        'independent_physical_scales': ['X', 'Y', 'Z'],
        'scale_exponents': list(map(str, exponents)),
        'operator': 'X*dX + Y*dY + Z*dZ + 1/2',
        'physical_profile_terms': ['-W0*W1*G', '-r0*W0_prime*W1*G',
                                   '-r1*W0*W1_prime*G', 'W0*W1*log(y)*G/2'],
        'multiplier': str(multiplier),
        'external_prime_slot_scales_held_fixed': True,
        'diagonal_value': '0',
        'principal_signal_value': 'x',
        'signal_zero_set': ['0'],
        'physical_probe_integration_checked': False,
        'low_estimate_checked': False,
        'coherent_row_sum_checked': False,
        'angular_cubic_probe': {
            'scope': 'angular compatibility and Mellin algebra only; no global identity or estimate',
            'physical_orders': [k1, k2], 'source_order': ell,
            'label_compensator_order': -k1-k2,
            'partial_cubic_mode_after_conjugation': k1,
            'frequency_angular_orders': angular_orders,
            'remaining_ordinary_frequency_pole': '2*t1+t2=1',
            'coupled_scale_condition': 'X2^2=Z*X1',
            'candidate_scale_power_on_pole': 'Z^(x-1/2)*sqrt(X1/X2)',
            'full_frequency_sum_checked': False,
        },
        'cubic_aspect_contrast': {
            'scope': 'principal local residue and fixed-product finite-difference algebra',
            'probe_coefficients': [1, -2, 1],
            'scale_copies': ['(X1,X2)', '(kappa*X1,X2/kappa)',
                             '(kappa^2*X1,X2/kappa^2)'],
            'mellin_multiplier': '(kappa^(t2-t1)-1)^2',
            'local_iterated_residue': str(residue),
            'quadratic_signal_second_difference': str(second_difference),
            'signal_factor_relative_to_unscaled_top_log_coefficient': '2*log(kappa)^2',
            'conditional_theta_target': '21/25',
            'unproved_full_contrast_direct_target': '8797/30000',
            'source_to_centered_estimate_map_checked': False,
        },
        'new_exponent_saving_proved': False,
    }
    path = Path(__file__).resolve().parents[1]/'results/mellin-annihilator.json'
    if args.write:
        path.write_text(json.dumps(receipt, indent=2)+'\n')
    else:
        assert json.loads(path.read_text()) == receipt
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
