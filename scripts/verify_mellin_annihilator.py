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
    assert s.expand(multiplier.subs(w, 1-x)) == 0
    assert s.expand(multiplier.subs({w: 1, z: s.Rational(1, 6)})-x) == 0
    # Common dilation gives the sum of the three scale exponents plus a half.
    assert s.expand(s.diff(s.exp(sum(exponents)*t)*s.exp(t/2), t).subs(t, 0)
                    - multiplier) == 0
    # The inverse reciprocal's signal factor is x; its only zero is outside
    # the proposed strip Re(x)>869/1000.
    assert s.solve(multiplier.subs(w, 1), x) == [0]
    receipt = {
        'status': 'exact candidate-probe Mellin identities; no improved bound',
        'independent_physical_scales': ['X', 'Y', 'Z'],
        'scale_exponents': list(map(str, exponents)),
        'operator': 'X*dX + Y*dY + Z*dZ + 1/2',
        'multiplier': str(multiplier),
        'external_prime_slot_scales_held_fixed': True,
        'diagonal_value': '0',
        'principal_signal_value': 'x',
        'signal_zero_set': ['0'],
        'physical_probe_integration_checked': False,
        'low_estimate_checked': False,
        'coherent_row_sum_checked': False,
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
