#!/usr/bin/env python3
"""Numerical atomic phase diagnostic for the paused Fourier-coupled prototype."""
import cmath
from functools import lru_cache
from itertools import product
from math import sqrt

if not __debug__:
    raise RuntimeError("Diagnostics require assertions enabled.")

OMEGA = cmath.exp(2j*cmath.pi/3)
PRIMES = [(-2, -3, 7, 4), (1, -3, 13, 9)]


def multiply(z, t):
    a, b = z
    c, d = t
    return a*c-b*d, a*d+b*c-b*d


def norm(z):
    a, b = z
    return a*a-a*b+b*b


def generator(mask):
    z = (1, 0)
    for i, p in enumerate(PRIMES):
        if mask >> i & 1:
            z = multiply(z, p[:2])
    return z


def character(mask, z):
    out = 1+0j
    for i, (_, _, q, root) in enumerate(PRIMES):
        if mask >> i & 1:
            value = (z[0]+root*z[1]) % q
            if value == 0:
                return 0j
            residue = pow(value, (q-1)//3, q)
            out *= OMEGA**next(k for k in range(3) if pow(root, k, q) == residue)
    return out


@lru_cache(None)
def gauss(c, s, h):
    z = multiply(generator(c), generator(s))
    n = norm(z)
    if n == 1:
        return 1+0j
    frequency = (-z[1]*h[0]+z[0]*h[1]) % n
    return sum(character(c, (a, 0))*character(s, (a, 0)).conjugate()
               *cmath.exp(2j*cmath.pi*((frequency*a) % n)/n) for a in range(n))


def normalized_gauss(mask):
    return gauss(mask, 0, (1, 0))/sqrt(norm(generator(mask)))


def main():
    errors = []
    overlaps = 0
    for c, s, m in product(range(4), repeat=3):
        if c & s:
            continue
        cp = c & ~m
        zc, zm = generator(c), generator(m)
        alpha = (zc[0]+zc[1]*OMEGA)/sqrt(norm(zc))
        gc, gs, gcp = map(normalized_gauss, (c, s, cp))
        actual = (gc**2*alpha.conjugate()/gcp*character(cp, zm)*character(c, generator(s))
                  *gauss(cp, s, zm)/sqrt(norm(generator(cp))*norm(generator(s))))
        expected = (-1)**c.bit_count()*gc.conjugate()*gs.conjugate()*character(s, multiply(zc, zm))
        errors.append(abs(actual-expected))
        overlaps += int(bool(c & m))
    assert len(errors) == 36 and overlaps == 11
    assert max(errors) < 1e-10
    print(f"Coupled Fourier diagnostic: 36 actual Eisenstein CRT cases, 11 source-row overlaps; "
          f"maximum absolute error {max(errors):.3g} < 1e-10. No global estimate checked.")


if __name__ == "__main__":
    main()
