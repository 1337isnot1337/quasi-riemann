#!/usr/bin/env python3
"""Exact finite Airy/Gauss trace identities; no analytic trace estimate."""
import argparse
import json
from math import gcd, prod
from pathlib import Path

import sympy as S

from verify_jacobi_detector import convolution, emul

if not __debug__:
    raise RuntimeError("Verification requires assertions enabled.")

ROOT = Path(__file__).resolve().parents[1]
OMEGA_POWERS = [(1, 0), (0, 1), (-1, -1)]


def character(primes, embedding):
    tables = []
    for p in primes:
        root = next(r for r in range(p) if (r*r+r+1) % p == 0)
        tables.append((p, {1: 0, root: 1, root*root % p: 2}))

    def chi(x, power=1):
        value = (1, 0)
        for p, table in tables:
            if x % p == 0:
                return (0, 0)
            exponent = embedding*power*table[pow(x % p, (p-1)//3, p)] % 3
            value = emul(value, OMEGA_POWERS[exponent])
        return value
    return chi


def sums(n, chi, h, additive):
    kloosterman = [(0, 0)]*n
    airy = [(0, 0)]*n
    gauss = [(0, 0)]*n
    inv2 = pow(2, -1, n)
    for t in range(n):
        j = additive*h*(3*t-t**3)*inv2 % n
        a, b = airy[j]
        airy[j] = (a+1, b)
        gauss[additive*t % n] = chi(t, -1)
        if gcd(t, n) == 1:
            j = additive*(t+h*h*pow(4*t, -1, n)) % n
            a, b = kloosterman[j]
            c, d = chi(t)
            kloosterman[j] = (a+c, b+d)
    return kloosterman, airy, gauss


def equal(left, right, phi):
    z = phi.gen
    for part in (0, 1):
        coeff = [a[part]-b[part] for a, b in zip(left, right)]
        assert S.Poly.from_list(coeff[::-1], z).rem(phi).is_zero


def check_modulus(primes, frequencies, embeddings, additives):
    n = prod(primes)
    z = S.Symbol("z")
    phi = S.Poly(S.cyclotomic_poly(n, z), z)
    unit_checks = overlap_checks = 0
    for embedding in embeddings:
        chi = character(primes, embedding)
        for additive in additives:
            assert gcd(additive, n) == 1
            for h in frequencies:
                h %= n
                klo, airy, gauss = sums(n, chi, h, additive)
                g = gcd(h, n)
                d = n//g
                if g == 1:
                    equal(klo, [emul(chi(4*h), a) for a in airy], phi)
                    unit_checks += 1

                left = convolution(gauss, klo)
                right = [(0, 0)]*n
                if d == 1:
                    right[0] = (g, 0)
                else:
                    hd = h//g
                    cd = character([p for p in primes if d % p == 0], embedding)
                    _, ad, _ = sums(d, cd, hd, additive)
                    gd = [(0, 0)]*d
                    for t in range(d):
                        gd[additive*hd*t % d] = cd(t, -1)
                    for j, value in enumerate(convolution(gd, ad)):
                        right[g*j] = tuple(g*a for a in emul(cd(4), value))
                equal(left, right, phi)
                overlap_checks += 1
    return unit_checks, overlap_checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    unit_checks = overlap_checks = 0
    for p in (7, 13, 19, 31, 37):
        u, o = check_modulus([p], range(p), (1, 2), (1, 2, 3))
        unit_checks += u
        overlap_checks += o
    composite_checks = 0
    for primes in ([7, 13], [7, 19]):
        u, o = check_modulus(primes, (0, 1, 2, 7, 13, 19, 14, 26), (1, 2), (1, 2))
        unit_checks += u
        overlap_checks += o
        composite_checks += o
    # The g extraction removes g from the Gaussian argument and leaves 1/Ng.
    qg, qd, qh = S.symbols("qg qd qh", positive=True)
    assert S.simplify(qg*qh/(qg*qd)-qh/qd) == 0
    assert S.simplify(S.sqrt(qg)/(qg*qd)**S.Rational(3, 2)
                      -1/(qg*qd**S.Rational(3, 2))) == 0
    result = {
        "status": "exact finite Airy and gcd identities; no new analytic bound",
        "unit_airy_checks": unit_checks,
        "gauss_overlap_checks": overlap_checks,
        "composite_overlap_checks": composite_checks,
        "prime_norms": [7, 13, 19, 31, 37],
        "composite_norms": [91, 133],
        "cubic_embeddings_per_modulus": 2,
        "prime_additive_characters_per_embedding": 3,
        "phase": "h*(3*t-t^3)/2",
        "all_frequency_gcds_derived_for_squarefree_moduli": True,
        "nonsquarefree_moduli_estimated": False,
        "full_mean_zero_trace_estimated": False,
        "improved_quasi_riemann_bound": False,
    }
    path = ROOT/"results/airy-trace.json"
    if args.write:
        path.write_text(json.dumps(result, indent=2)+"\n")
    else:
        assert json.loads(path.read_text()) == result
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
