#!/usr/bin/env python3
"""Algebraic certificate, not a formal proof of the analytic Picard theorem."""
import argparse
import json
from pathlib import Path

import sympy as S

ROOT = Path(__file__).resolve().parents[1]
if not __debug__:
    raise RuntimeError("Verification requires assertions enabled.")


def exact_checks():
    a, z, s, nu, r = S.symbols("a z s nu r")
    # Clear (a+cosh(u))^(s+2) from the differentiated integrand.
    d = a + z
    second_u = -s*z*d + s*(s+1)*(z*z-1)
    from_ode = s*s*d*d - s*(2*s+1)*a*d + s*(s+1)*(a*a-1)
    assert S.expand(second_u-from_ode) == 0

    g = S.Function("g")(r)
    first_a = S.diff(g, r)/S.sinh(r)
    second_a = S.diff(first_a, r)/S.sinh(r)
    pulled = S.sinh(r)**2*second_a + (2*s+1)*S.cosh(r)*first_a + (s*s-nu*nu)*g
    radial = S.diff(g, r, 2) + 2*s*S.coth(r)*S.diff(g, r) + (s*s-nu*nu)*g
    assert S.simplify(pulled-radial) == 0

    y = S.Function("y")(r)
    scale = S.sinh(r)**(S.Rational(1, 2)-s)
    conjugated = (S.diff(scale*y, r, 2) + 2*s*S.coth(r)*S.diff(scale*y, r)
                  + (s*s-nu*nu)*scale*y)/scale
    target = (S.diff(y, r, 2) + S.coth(r)*S.diff(y, r)
              - (nu*nu-S.Rational(1, 4)+(s-S.Rational(1, 2))**2/S.sinh(r)**2)*y)
    assert S.simplify(S.expand(conjugated-target)) == 0
    assert S.Rational(1, 9)-S.Rational(1, 4) == -S.Rational(5, 36)

    # Cross term becomes -1/2 * integral cosh(r)*|y|^2 after integration.
    energy_coefficient = -S.cosh(r)/2 + S.sinh(r)/4 + S.exp(-r)/2 + S.sinh(r)/9
    assert S.simplify(energy_coefficient+S.Rational(5, 36)*S.sinh(r)) == 0
    p, q = S.symbols("p q", real=True)
    assert S.expand(S.im((p+S.I*q)**2)) == 2*p*q
    assert S.expand(S.re((p+S.I*q)**2).subs(q, 0)) == p*p

    return {
        "status": "exact identities checked; analytic proof is written, not Lean",
        "integrand_identity": True,
        "hyperbolic_pullback": True,
        "conjugated_ode": True,
        "energy_identity": True,
        "complex_parameter_algebra": True,
        "written_proposition": "F(s,x) != 0 for real x >= 2 and Re(s) > 1/2",
        "analytic_boundary_terms_formalized": False,
        "goldfeld_hinkle_spectral_theorems_independently_verified": False,
        "improved_quasi_riemann_bound": False,
    }


def numerical_checks():
    import mpmath as m

    m.mp.dps = 45
    cases = [("2.25", "0.6", "7"), ("5", "0.8", "2"), ("10", "1.2", "11")]
    rows = []
    for xstr, sigma, height in cases:
        x, s = m.mpf(xstr), m.mpc(sigma, height)
        # The omitted tail has an explicit elementary absolute bound.
        cutoff = 160
        quadrature = 2*m.quad(
            lambda u: m.cosh(u/3)*m.exp(-s*m.log(x-1+m.cosh(u))),
            list(range(cutoff+1)),
        )
        tail_bound = 2**(1+s.real)*m.exp(-(s.real-m.mpf(1)/3)*cutoff)/(s.real-m.mpf(1)/3)
        mu = s-m.mpf(1)/2
        legendre = (m.sqrt(2*m.pi)*m.gamma(s+m.mpf(1)/3)*m.gamma(s-m.mpf(1)/3)
                    /m.gamma(s)*((x-1)**2-1)**(-mu/2)
                    *m.legenp(-m.mpf(1)/6, -mu, x-1, type=3))
        hypergeom = (2**s*m.gamma(s+m.mpf(1)/3)*m.gamma(s-m.mpf(1)/3)/m.gamma(2*s)
                     *(x/2)**(-mu)*m.hyp2f1(m.mpf(1)/6, m.mpf(5)/6, s+m.mpf(1)/2, 1-x/2))
        assert abs(quadrature-legendre) < tail_bound + m.mpf("1e-35")
        assert abs(legendre-hypergeom) < m.mpf("1e-38")*max(1, abs(legendre))
        rows.append({"x": xstr, "s": f"{sigma}+{height}i",
                     "absolute_quadrature_defect": m.nstr(abs(quadrature-legendre), 8),
                     "tail_bound": m.nstr(tail_bound, 8)})
    print(json.dumps({"numerical_diagnostics_only": rows}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--numerical", action="store_true")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = exact_checks()
    path = ROOT/"results/picard-factor.json"
    if args.write:
        path.write_text(json.dumps(result, indent=2)+"\n")
    else:
        assert json.loads(path.read_text()) == result
    print("Picard factor: five groups of exact identities passed; analytic theorem has a written proof.")
    if args.numerical:
        numerical_checks()


if __name__ == "__main__":
    main()
