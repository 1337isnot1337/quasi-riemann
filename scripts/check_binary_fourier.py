#!/usr/bin/env python3
"""Numerical normalization check against direct finite Fourier sums at Q=7.

This is a diagnostic, not an exact proof or a zero-free bound certificate.
"""
import cmath
from functools import lru_cache
from itertools import product
from math import pi, prod, sqrt


Q = 7
# 3 generates F_7^*. Its cubic character is extended by zero at zero.
chi = {pow(3, k, Q): cmath.exp(2j*pi*(k % 3)/3) for k in range(Q-1)}
chi[0] = 0j


@lru_cache(None)
def gauss(power, orientation, valuation):
    if power == 0:
        return 1+0j
    modulus = Q**power
    frequency = pow(Q, valuation, modulus)
    return sum((chi[a % Q]**orientation if orientation else int(a % Q != 0))
               * cmath.exp(2j*pi*((a*frequency) % modulus)/modulus)
               for a in range(modulus))


def check_eisenstein_crt():
    """Direct sums in O/(c*s), including c/s overlaps at norms 7 and 13."""
    omega = cmath.exp(2j*pi/3)
    # (primary generator coordinates, norm, image of omega in the quotient)
    primes = [(-2, -3, 7, 4), (1, -3, 13, 9)]

    def multiply(z, w):
        a, b = z
        c, d = w
        return a*c-b*d, a*d+b*c-b*d

    def norm(z):
        a, b = z
        return a*a-a*b+b*b

    def generator(mask):
        z = (1, 0)
        for i, p in enumerate(primes):
            if mask >> i & 1:
                z = multiply(z, p[:2])
        return z

    def cubic(i, value):
        _, _, q, root = primes[i]
        if value % q == 0:
            return 0j
        residue = pow(value % q, (q-1)//3, q)
        return omega**next(k for k in range(3) if pow(root, k, q) == residue)

    @lru_cache(None)
    def normalized_gauss(mask, orientation):
        if not mask:
            return 1+0j
        z = generator(mask)
        n, b = norm(z), z[1]
        return sum(prod(cubic(i, a)**orientation for i in range(2) if mask >> i & 1)
                   *cmath.exp(-2j*pi*((b*a) % n)/n) for a in range(n))/sqrt(n)

    def actual_gauss(c, s, h):
        z = multiply(generator(c), generator(s))
        n, (a, b) = norm(z), z
        frequency = (-b*h[0]+a*h[1]) % n
        total = 0j
        for value in range(n):
            char = 1+0j
            for i in range(2):
                if (c | s) >> i & 1:
                    v = cubic(i, value)
                    if v == 0:
                        char = 0j
                        break
                    char *= v**(((c >> i & 1)-(s >> i & 1)) % 3)
            total += char*cmath.exp(2j*pi*((frequency*value) % n)/n)
        return total

    errors = []
    for c, s in product(range(4), repeat=2):
        z = generator(c)
        alpha = (z[0]+z[1]*omega)/sqrt(norm(z))
        d = generator(c & s)
        actual = (normalized_gauss(c, 1)*normalized_gauss(s, 2)**(-2)
                  *alpha.conjugate()*actual_gauss(c, s, d)
                  *actual_gauss(c, s, multiply(d, d)))
        expected = (-1)**((c & ~s).bit_count())
        for i, p in enumerate(primes):
            if (c ^ s) >> i & 1:
                expected *= p[2]
            elif (c & s) >> i & 1:
                expected *= p[2]**2*(p[2]-1)
        errors.append(abs(actual/expected-1))
    assert max(errors) < 1e-10
    print(f"Actual Eisenstein CRT diagnostic: 16 cases; maximum relative error {max(errors):.3g} < 1e-10.")


def main():
    gamma2 = gauss(1, 1, 0)/sqrt(Q)
    gamma4 = gauss(1, 2, 0)/sqrt(Q)
    alpha = -gamma2**3
    assert abs(gamma2*gamma4-1) < 1e-12
    eta = cmath.exp(.3j)
    v, t1, t2, w = 1, 1, 1, .75
    x = 1.5+v-t1-t2
    A, B = Q**(-t1), Q**(-t2)
    D, W = eta*Q**(-x), Q**(-w)
    T = eta*Q**(-x-w)
    R = eta**3*alpha**(-3)*Q**(-1-3*v)
    den = (1-A**3)*(1-B**3)
    f = [(1+A*B**2+A**2*B)/den, (A+B+A**2*B**2)/den,
         (A**2+A*B+B**2)/den]
    g = []
    for j in range(3):
        residue = (j+1) % 3
        g.append((1-1/Q)**2*f[j]-(1-1/Q)/Q*(
            A**-1*B**residue/(1-B**3)+A**residue*B**-1/(1-A**3))
            +int(j == 1)/(A*B*Q**2))
    direct = [0j]*3
    for e in range(2):
        for k in range(2):
            for ell in range(2):
                t = e+3*ell
                modulus_power = t+k
                orientation = (e-k) % 3
                source = (gamma2**e*gamma4**(-2*k)*eta**t*alpha**(-t)
                          *Q**(-e/2-ell-t*v+t*(t1+t2)-2*t-k*(1+w)))
                values = [gauss(modulus_power, orientation, a) for a in range(19)]
                for a in range(19):
                    for b in range(19):
                        direct[(a+b) % 3] += source*values[a]*values[b]*A**a*B**b
    expected = [f[j]+R*g[j]+((W-D)*(1+R) if j == 0 else 0)
                -T*Q**2*A**2*B**2*g[(j-1) % 3]*(1+R) for j in range(3)]
    error = max(abs(a-b) for a, b in zip(direct, expected))
    assert error < 1e-10, error
    print(f"Direct local Fourier diagnostic: 3 row sectors; maximum error {error:.3g} < 1e-10.")
    check_eisenstein_crt()


if __name__ == "__main__":
    main()
