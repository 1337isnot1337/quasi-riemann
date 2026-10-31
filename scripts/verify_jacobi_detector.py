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


def cyclotomic_equal(x, y):
    difference = [(a-c, b-d) for (a, b), (c, d) in zip(x, y)]
    # Phi_p=1+z+...+z^(p-1), irreducible over Q(omega), p!=3.
    assert len(set(difference)) == 1


def check_kummer(p, character, phi, centered=False):
    gbar = [(0, 0)]+[character(x, -1) for x in range(1, p)]
    gquad = [(0, 0)]+[(phi(x), 0) for x in range(1, p)]
    prefactor = emul(character(-1 if centered else -pow(4, -1, p)),
                       (phi(-1), 0))
    for h in range(p):
        jacobi = [(0, 0)]*p
        kloosterman = [(0, 0)]*p
        for x in range(p):
            u = (x*x-1 if centered else x*(x-1)) % p
            if u:
                a, b = character(u)
                c, d = jacobi[h*x % p]
                jacobi[h*x % p] = (a+c, b+d)
        for t in range(1, p):
            nu = emul(character(t, -1), (phi(t), 0))
            k = (t+h*h*pow((4 if centered else 16)*t, -1, p)) % p
            a, b = kloosterman[k]
            kloosterman[k] = (a+nu[0], b+nu[1])
        left = convolution(gbar, jacobi)
        right = convolution(gquad, kloosterman)
        shift = 0 if centered else h*pow(2, -1, p) % p
        right = [emul(prefactor, right[(k-shift) % p]) for k in range(p)]
        cyclotomic_equal(left, right)
    return p


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    checks = []
    kummer_checks = 0
    sextic_checks = []
    sextic_kummer_checks = 0
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
        kummer_checks += check_kummer(p, chi, phi)
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

        roots6 = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]
        lookup6 = {(aa+bb*root) % p: j for j, (aa, bb) in enumerate(roots6)}
        assert len(lookup6) == 6
        def chi6(x, power=1):
            return roots6[(power*lookup6[pow(x % p, (p-1)//6, p)]) % 6]
        epsilon = chi6(4)
        epsilon_bar = (epsilon[0]-epsilon[1], -epsilon[1])
        pi, pi_bar = (a, b), (a-b, -b)
        expected_residues = [emul(pi, epsilon_bar), emul(pi, epsilon_bar),
                             (1, 0), emul(pi_bar, epsilon),
                             emul(pi_bar, epsilon), (2-p, 0)]
        for e in range(1, 7):
            actual = (0, 0)
            for xx in range(p):
                u = (xx*xx-1) % p
                if u:
                    aa, bb = chi6(u, e)
                    actual = (actual[0]+aa, actual[1]+bb)
            expected = tuple(-t for t in expected_residues[e-1])
            assert actual == expected
            sextic_checks.append({'norm': p, 'exponent': e, 'jacobi': list(actual)})
        assert all(emul(chi6(t, -1), (phi(t), 0)) == chi6(t, 2)
                   for t in range(1, p))
        sextic_kummer_checks += check_kummer(p, chi6, phi, centered=True)
        # Exact Gauss phase after including the ordinary source compensator.
        scalar = emul(pi_bar, epsilon)
        left = [(0, 0)]+[emul(scalar, (phi(t), 0)) for t in range(1, p)]
        right = convolution([(0, 0)]+[chi6(t, 4) for t in range(1, p)],
                            [(0, 0)]+[chi6(t, 5) for t in range(1, p)])
        cyclotomic_equal(left, [(-aa, -bb) for aa, bb in right])

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
    epsilon = s.symbols('epsilon', nonzero=True)
    local6 = (1-alpha*epsilon**-1*y*z-alpha*epsilon**-1*y*z**2-y*y*z**3
              -alpha**-1*epsilon*y*z**4-alpha**-1*epsilon*y*z**5
              -2*y*y*z**6)/(1-z**6)
    poly6 = s.series(local6, z, 0, 13).removeO().expand()
    residues = [1-2*y*y, -alpha*epsilon**-1*y, -alpha*epsilon**-1*y, -y*y,
                -alpha**-1*epsilon*y, -alpha**-1*epsilon*y]
    for e in range(13):
        assert s.cancel(poly6.coeff(z, e)-(1 if e == 0 else residues[e % 6])) == 0
    margin6 = 1-Fraction(1, 4)-Fraction(1, 7)-3*Fraction(1, 18)-Fraction(1, 63)
    assert margin6 == Fraction(107, 252) and margin6 > 0
    assert 7**3 > 4**4 and 7**3 > 18**2
    assert Fraction(4, 5)-Fraction(1, 10000) > Fraction(3, 4)
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
        'sextic_jacobi_variant': {
            'finite_residue_field_checks': sextic_checks,
            'exact_kummer_trace_checks': sextic_kummer_checks,
            'exact_source_Gauss_phase_checks': 5,
            'Kloosterman_twist_order': 3,
            'formal_euler_coefficients_checked': 13,
            'completion_factor': 'L^S(6*x-3,eta^6*alpha_bar^6)',
            'physical_polynomial': 'm^2-1',
            'source_compensator': 'alpha_bar(c)*epsilon(c)',
            'linear_additive_phase_absent': True,
            'squarefree_high_coefficient': 'mu(c)*eta(c)*gamma_4(c)',
            'nonzero_signal_domain': 'Re(x)>3/4',
            'local_numerator_lower_bound': str(margin6),
            'unproved_complete_trace_bound': 'H6_eta(Z^(2/5),Z) << Z^(-1/10000)',
            'conditional_zero_free_threshold': '4/5',
            'trace_bound_proved': False,
        },
    }
    path = Path(__file__).resolve().parents[1]/'results/jacobi-detector.json'
    if args.write:
        path.write_text(json.dumps(receipt, indent=2)+'\n')
    else:
        assert json.loads(path.read_text()) == receipt
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
