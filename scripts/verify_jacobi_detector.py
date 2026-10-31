#!/usr/bin/env python3
"""Exact Jacobi detector arithmetic; the nonzero-frequency estimate is open."""
import argparse
from fractions import Fraction
import json
from math import isqrt
from pathlib import Path

import sympy as s

if not __debug__:
    raise RuntimeError('Verification requires assertions enabled.')


def emul(x, y):
    a, b = x
    c, d = y
    return a*c-b*d, a*d+b*c-b*d


def convolution(x, y):
    n = len(x)
    out = [(0, 0)]*n
    for i, u in enumerate(x):
        for j, v in enumerate(y):
            a, b = emul(u, v)
            c, d = out[(i+j) % n]
            out[(i+j) % n] = (a+c, b+d)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    checks = []
    kummer_checks = 0
    for p in (7, 13, 19, 31, 37):
        root = next(r for r in range(p) if (r*r+r+1) % p == 0)
        lookup = {1: 0, root: 1, root*root % p: 2}
        radius = 2*isqrt(p)+2
        primary = [(a, b) for a in range(-radius, radius+1)
                   for b in range(-radius, radius+1)
                   if a*a-a*b+b*b == p and (a-1) % 3 == b % 3 == 0
                   and (a+b*root) % p == 0]
        assert len(primary) == 1
        a, b = primary[0]
        roots = [(1, 0), (0, 1), (-1, -1)]
        def chi(x, power=1):
            return roots[(power*lookup[pow(x % p, (p-1)//3, p)]) % 3]
        def phi(x):
            return 1 if pow(x % p, (p-1)//2, p) == 1 else -1
        gbar = [(0, 0)]+[chi(x, 2) for x in range(1, p)]
        gquad = [(0, 0)]+[(phi(x), 0) for x in range(1, p)]
        prefactor = emul(chi(-pow(4, -1, p)), (phi(-1), 0))
        for h in range(p):
            jacobi = [(0, 0)]*p
            kloosterman = [(0, 0)]*p
            for x in range(p):
                u = x*(x-1) % p
                if u:
                    aa, bb = chi(u)
                    cc, dd = jacobi[h*x % p]
                    jacobi[h*x % p] = (aa+cc, bb+dd)
            for t in range(1, p):
                nu = emul(chi(t, 2), (phi(t), 0))
                k = (t+h*h*pow(16*t, -1, p)) % p
                aa, bb = kloosterman[k]
                kloosterman[k] = (aa+nu[0], bb+nu[1])
            left = convolution(gbar, jacobi)
            right = convolution(gquad, kloosterman)
            shift = h*pow(2, -1, p) % p
            right = [emul(prefactor, right[(k-shift) % p]) for k in range(p)]
            difference = [(aa-cc, bb-dd) for (aa, bb), (cc, dd) in zip(left, right)]
            # Phi_p=1+z+...+z^(p-1), irreducible over Q(omega), p!=3.
            assert len(set(difference)) == 1
            kummer_checks += 1
        for e in (1, 2, 3):
            counts = [0, 0, 0]
            # O/(pi**e) is Z/(p**e) at these split degree-one primes.
            # The character reduces modulo p and retains its zero there.
            for x in range(p**e):
                t = x*(x-1) % p
                if t:
                    counts[(e*lookup[pow(t, (p-1)//3, p)]) % 3] += 1
            actual = (counts[0]-counts[2], counts[1]-counts[2])
            expected = ((-a*p**(e-1), -b*p**(e-1)) if e % 3 == 1
                        else ((b-a)*p**(e-1), b*p**(e-1)) if e % 3 == 2
                        else ((p-2)*p**(e-1), 0))
            assert actual == expected
            checks.append({'norm': p, 'power': e, 'jacobi': list(actual)})

    z, y, alpha = s.symbols('z y alpha', nonzero=True)
    local = (1-alpha*y*z-alpha**-1*y*z*z-2*y*y*z**3)/(1-z**3)
    polynomial = s.series(local, z, 0, 13).removeO().expand()
    for e in range(13):
        expected = (1 if e == 0 else -alpha*y if e % 3 == 1
                    else -alpha**-1*y if e % 3 == 2 else 1-2*y*y)
        assert s.cancel(polynomial.coeff(z, e)-expected) == 0
    D, E, q, R = s.symbols('D E q R')
    correction = (1-D-E-2*q*R)/(1-D)
    assert s.cancel(correction-1+(E+2*q*R)/(1-D)) == 0
    assert 7**5 > 5**6
    margin = 1-Fraction(1, 5)-Fraction(1, 7)-2*Fraction(1, 49)
    assert margin == Fraction(151, 245) and margin > 0
    x = s.symbols('x')
    assert (2*x-s.Rational(1, 2)).subs(x, s.Rational(3, 4)) == 1
    assert (3*x-s.Rational(3, 2)).subs(x, s.Rational(5, 6)) == 1

    a = Fraction(2, 5)
    theta = Fraction(21, 25)
    target = theta-1+a/2-Fraction(1, 10000)
    assert target == Fraction(399, 10000)
    assert Fraction(4, 5)+target == Fraction(8399, 10000)
    assert Fraction(8399, 10000) > Fraction(5, 6)
    assert 1-2*a == Fraction(1, 5)  # positive arbitrary-power direct decay.
    receipt = {
        'status': 'Jacobi detector identities and conditional target; no new bound',
        'finite_prime_power_checks': checks,
        'exact_kummer_trace_checks': kummer_checks,
        'trace_twist_order': 6,
        'formal_euler_coefficients_checked': 13,
        'zero_frequency_series':
            'L^S(3*x-3/2,eta^3*alpha_bar^3)*K_eta(x)/L^S(x,eta)',
        'local_numerator': '1-D-E-2*q*R',
        'local_numerator_nonzero_lower_bound': str(margin),
        'correction_absolute_domain': 'Re(x)>3/4',
        'nonzero_signal_domain': 'Re(x)>5/6',
        'ordinary_source_direct_bound_written': True,
        'direct_bound': 'I_eta <<_A sqrt(X*Z)*(X^2/Z)^A + X^(-1/2)*V(1/Z)',
        'direct_bound_uses_eta_finite_and_angular_order_minus_one': True,
        'target_X': 'Z^(2/5)',
        'unproved_complete_nonzero_frequency_bound': f'H_eta << Z^({target})',
        'conditional_zero_free_threshold': '21/25',
        'nonzero_frequency_bound_proved': False,
        'improved_L_function_bound_proved': False,
    }
    path = Path(__file__).resolve().parents[1]/'results/jacobi-detector.json'
    if args.write:
        path.write_text(json.dumps(receipt, indent=2)+'\n')
    else:
        assert json.loads(path.read_text()) == receipt
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
