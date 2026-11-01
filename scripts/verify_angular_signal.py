#!/usr/bin/env python3
"""Exact angular Fourier/local algebra; no continued row-sum estimate."""
import argparse
from fractions import Fraction
import json
from pathlib import Path

import sympy as s

if not __debug__:
    raise RuntimeError('Verification requires assertions enabled.')


def equal(a, b):
    assert s.cancel(a-b) == 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    # Ordinary two-dimensional Fourier transform, then the self-dual pairing.
    xi, yi, a, b = s.symbols('xi yi a b', real=True)
    gaussian = s.exp(-s.pi*(xi**2+yi**2))
    for k in (2, -4):
        transformed = gaussian
        for _ in range(abs(k)):
            transformed = s.I/(2*s.pi)*(s.diff(transformed, xi)
                + s.sign(k)*s.I*s.diff(transformed, yi))
        transformed = 2/s.sqrt(3)*transformed.subs(
            {xi: 2*b/s.sqrt(3), yi: 2*a/s.sqrt(3)})
        angular = (a-s.I*b)**k if k > 0 else (a+s.I*b)**(-k)
        expected = (2/s.sqrt(3))**(abs(k)+1)*angular*s.exp(
            -4*s.pi*(a*a+b*b)/3)
        assert s.simplify(transformed-expected) == 0

    # Use omega as unit generator, with a second sign for each cube root.
    # d is the cubic character's value at omega, expressed as omega**d.
    omega = s.symbols('omega')
    for d in range(3):
        physical = sum(omega**((j*(d+2)) % 3) for j in range(6))**2
        dual = 12*sum(omega**((r*(1-d)) % 3) for r in range(3))
        assert s.rem(physical-dual, omega**2+omega+1, omega) == 0
    for r in range(3):
        # Both choices of sign are immaterial for the even angular orders.
        pairs = [(i, j) for i in range(6) for j in range(6)
                 if (i+j) % 3 == r]
        assert len(pairs) == 12
        assert all((-2*i+4*j-r) % 3 == 0 for i, j in pairs)

    Q, alpha, t1, t2, v, eta = s.symbols('Q alpha t1 t2 v eta')
    # A complete cube layer shifts BOTH frequency valuations by three.
    # Its new angular ratio is alpha**6 times the radial ratio.
    equal((alpha**-2*alpha**4)**3, alpha**6)
    equal(alpha**-3*alpha**6, alpha**3)

    # On 2*t1+t2=1 and Re(t1)=1/3 put q=1/Q and z=A**3/q.
    # Then |z|=1, B/A=z**-1, and A**2*B=q.
    q, z, D, R = s.symbols('q z D R')
    den = (1-q*z)*(1-q/z**2)
    f0 = (1+q+q/z)/den
    g0 = (1-q)**2*f0-q*(1-q)*(z**-1/(1-q/z**2)
                                           + z/(1-q*z))
    bg2 = (1-q)**2*(q+q/z+q/z**2)/den-q*(1-q)*(
        z**-1/(1-q/z**2)+1/(1-q*z))
    equal(g0, (1-q)/(1-q/z**2))
    equal(bg2, q/z**2*g0)
    numerator = f0+R*(g0-f0)+q-D*(1+bg2)
    correction = s.cancel((1-q/z)*(1-q)*den*numerator/
                          ((1-D)*(1+q)))
    equal(correction.subs(q, 0), 1)
    # Remaining linear terms carry D or R; all other defects have degree >=2.
    equal(s.diff(correction, q).subs(q, 0),
          (D-R)*(z+1)**2/(z*(1-D)))
    cleared = s.Poly(s.expand(s.cancel((correction-1)*(1-D)*(1+q))), q)
    assert cleared.nth(0) == 0
    equal(cleared.nth(1), (D-R)*(z+1)**2/z)

    # Q>=7, Re(x)>5/6 imply q<=1/7, |R|<=1/7 and |D|<1/5.
    assert 7**5 > 5**6
    qmax = Fraction(1, 7)
    lower_f = Fraction(49, 64)
    margin = (lower_f*(1-qmax*(2*qmax-qmax*qmax))
              -2*qmax*qmax-qmax-Fraction(1, 5)*(1+5*qmax))
    assert margin == Fraction(1647, 7840) and margin > 0

    x, a1, a2, free = s.symbols('x a1 a2 free')
    vv = x-s.Rational(1, 2)-free
    scale = s.expand(vv+a1*(s.Rational(1, 2)-free)
                     +a2*(s.Rational(-1, 2)+2*free))
    equal(scale, x-s.Rational(1, 2)+(a1-a2)/2
          +(2*a2-1-a1)*free)
    equal(scale.subs(a2, (1+a1)/2), x-s.Rational(3, 4)+a1/4)

    receipt = {
        'status': 'angular Fourier and local residue certificate; no improved bound',
        'physical_orders': [2, -4], 'source_order': 1,
        'label_compensator_order': 2,
        'fourier_gaussians_checked': 2, 'unit_character_checks': 3,
        'unit_row_multiplier': 'omega**r', 'unit_multiplicity': 12,
        'completion_ratio': 'eta(p)**3*alpha(p)**3*Q**(-1-3*v)',
        'completion_ratio_is_radial_ratio': False,
        'principal_local_numerator_lower_bound': str(margin),
        'local_nonzero_domain': 'Re(x)>5/6, Re(t1)=1/3, t2=1-2*t1, w=1',
        'local_correction_decay': 'O(q**2+abs(D)*q+abs(R)*q)',
        'scale_ratio_parameter': 'kappa=X2**2/(Z*X1)',
        'coupled_signal_exponent': 'x-3/4+a1/4',
        'written_initial_global_identity': True,
        'written_mellin_family_separation_argument': True,
        'contour_shift_and_row_error_proved': False,
        'direct_probe_bound_proved': False,
    }
    path = Path(__file__).resolve().parents[1]/'results/angular-signal.json'
    if args.write:
        path.write_text(json.dumps(receipt, indent=2)+'\n')
    else:
        assert json.loads(path.read_text()) == receipt
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
