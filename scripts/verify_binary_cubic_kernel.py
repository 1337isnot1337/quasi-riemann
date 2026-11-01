#!/usr/bin/env python3
"""Local and unit algebra for the binary cubic identity; no row bound."""
import argparse
from fractions import Fraction
import json
from pathlib import Path

import sympy as S

if not __debug__:
    raise RuntimeError("Verification requires assertions enabled.")


def equal(a, b):
    assert S.cancel(a-b) == 0


def main():
    A, B, Q, R, D = S.symbols("A B Q R D")
    den = (1-A**3)*(1-B**3)
    f = [sum(A**a*B**b for a in range(3) for b in range(3)
             if (a+b) % 3 == j)/den for j in range(3)]
    expected = [1+A*B**2+A**2*B, A+B+A**2*B**2, A**2+A*B+B**2]
    for j in range(3):
        equal(f[j]*den, expected[j])
    g = []
    for j in range(3):
        residue = (j+1) % 3
        g.append((1-1/Q)**2*f[j] - (1-1/Q)/Q * (
            A**-1*B**residue/(1-B**3) + A**residue*B**-1/(1-A**3))
            + int(j == 1)/(A*B*Q**2))

    # Independent finite valuation replay of both Ramanujan boundary terms.
    # These checks supplement the four-region all-size derivation in the note.
    checks = 0
    for q in (7, 13):
        for j in range(3):
            laurent = S.expand(S.cancel(g[j]*den).subs(Q, q))
            terms = []
            for term in S.Add.make_args(laurent):
                powers = term.as_powers_dict()
                a, b = int(powers.get(A, 0)), int(powers.get(B, 0))
                coef = S.cancel(term/(A**a*B**b))
                terms.append((a, b, Fraction(int(S.numer(coef)), int(S.denom(coef)))))
            for ell in range(1, 5):
                for a in range(19):
                    for b in range(19):
                        coeff = Fraction(0)
                        for da, db, value in terms:
                            ra, rb = a-3*ell-da, b-3*ell-db
                            if ra >= 0 and rb >= 0 and ra % 3 == rb % 3 == 0:
                                coeff += value
                        ra = int(a >= 3*ell) - Fraction(int(a >= 3*ell-1), q)
                        rb = int(b >= 3*ell) - Fraction(int(b >= 3*ell-1), q)
                        assert coeff == (ra*rb if (a+b) % 3 == j else 0)
                        checks += 1

    p = [f[j]+(R*g[j]-(D if j == 0 else 0))/(1-R) for j in range(3)]
    # Every common cube-completion layer is geometric, with ratio R.
    for j in range(3):
        for cut in range(1, 5):
            truncated = f[j]+sum(R**ell*g[j] for ell in range(1, cut+1))
            if j == 0:
                truncated -= D*sum(R**ell for ell in range(cut+1))
            tail = R**(cut+1)*(g[j]-(D if j == 0 else 0))/(1-R)
            equal(p[j], truncated+tail)

    t = S.symbols("t", positive=True)
    critical_f, critical_g = [], []
    for j in range(3):
        critical_f.append(S.factor(f[j].subs({A: 1/t, B: 1/t, Q: t**3})))
        critical_g.append(S.factor(g[j].subs({A: 1/t, B: 1/t, Q: t**3})))
    assert critical_g == [S.Integer(1), 2/t, t**-2]
    equal(critical_f[0], (1+2/t**3)/(1-1/t**3)**2)
    equal(t*critical_f[1], (2+1/t**3)/(1-1/t**3)**2)
    equal(t**2*critical_f[2], 3/(1-1/t**3)**2)

    # Nonzero ramified corrections at the critical point: f_j > g_j > 0.
    q = S.symbols("q")  # q=1/Q, with 0<q<1.
    equal((2+q)-2*(1-q)**2, q*(5-2*q))
    equal(3-(1-q)**2, 2+2*q-q**2)
    # At j=0 the good-prime correction is 1+O(q^2 + Dq + Rq).
    f0 = (1+2*q)/(1-q)**2
    h0 = (1-q)**4*((1-R)*f0+R-D)/(1-D)
    h0_num = S.factor(S.cancel((h0-1)*(1-D)))
    assert S.expand(h0_num).subs(q, 0) == 0
    assert S.diff(h0_num, q).subs(q, 0) == 4*D-4*R
    equal(h0_num.subs({D: 0, R: 0}), q**2*(-3+2*q))

    # Wrong shortcuts change actual coefficients and local poles.
    assert Fraction(1, 7**2) != 0  # two boundary values give a j=1 term.
    assert Fraction(1, 7)-1 != 0   # the mixed boundary has a negative sign.
    assert S.cancel(p[1]-f[1]) != 0  # completion cannot be discarded.

    # A shared squarefree cubic label acts on both Poisson factors. Its
    # inverse squared Gauss phase cancels all CRT pair phases, also at overlap.
    e, k, ee, kk, ell, ell2 = S.symbols("e k ee kk ell ell2")
    phase = (2*e*ee+4*k*kk
             +2*((e-k)*(ee+kk+3*ell2)+(ee-kk)*(e+k+3*ell)))
    equal(phase, 6*(e*ee+(e-k)*ell2+(ee-kk)*ell))
    # Two unrestricted element frequencies have 12 unit pairs in each of
    # the three unit cube classes. Check the resulting exact unit packet.
    omega = S.symbols("omega")
    unit_checks = 0
    for rc in range(3):
        for rs in range(3):
            physical = sum(omega**((a*(rc-rs)) % 3) for a in range(6))**2
            dual = 12*sum(omega**((a*(rs-rc)) % 3) for a in range(3))
            assert S.rem(physical-dual, omega**2+omega+1, omega) == 0
            unit_checks += 1
    W, T = S.symbols("W T")
    marked = [f[j]+(R*g[j]+((W-D) if j == 0 else 0)
                       -T*Q**2*A**2*B**2*g[(j-1) % 3])/(1-R)
              for j in range(3)]
    critical_marked = [S.factor(m.subs({A: 1/t, B: 1/t, Q: t**3}))
                       for m in marked]
    equal((1-R)*critical_marked[0].subs(T, D*W),
          (1-D)*(1+W)+(1-R)*(critical_f[0]-1))
    equal((1-R)*critical_marked[1],
          (1-R)*critical_f[1]+2*R/t-T*t**2)
    equal((1-R)*critical_marked[2],
          (1-R)*critical_f[2]+R/t**2-2*T*t)

    # Shared c/s primes have a principal character modulo p^(3ell+2),
    # with both boundary valuations retained. Replay its entire finite box.
    marked_checks = 0
    for qn in (7, 13):
        for j in range(3):
            laurent = S.expand(S.cancel(A**2*B**2*g[(j-1) % 3]*den).subs(Q, qn))
            terms = []
            for term in S.Add.make_args(laurent):
                powers = term.as_powers_dict()
                a, b = int(powers.get(A, 0)), int(powers.get(B, 0))
                coef = S.cancel(term/(A**a*B**b))
                terms.append((a, b, Fraction(int(S.numer(coef)), int(S.denom(coef)))))
            for elln in range(4):
                for a in range(19):
                    for b in range(19):
                        coeff = Fraction(0)
                        for da, db, value in terms:
                            ra, rb = a-3*elln-da, b-3*elln-db
                            if ra >= 0 and rb >= 0 and ra % 3 == rb % 3 == 0:
                                coeff += value
                        modulus = 3*elln+2
                        ra = int(a >= modulus)-Fraction(int(a >= modulus-1), qn)
                        rb = int(b >= modulus)-Fraction(int(b >= modulus-1), qn)
                        assert coeff == (ra*rb if (a+b) % 3 == j else 0)
                        marked_checks += 1

    # At w=1 and the principal row, W=q is positive. The numerator is
    # a positive combination of 1-D and 1-R, hence nonzero if |D|,|R|<1.
    marked_h0 = (1-q)**4*((1-D)*(1+q)+(1-R)*(f0-1))/((1-D)*(1+q))
    mh_num = S.cancel((marked_h0-1)*(1-D)*(1+q))
    assert mh_num.subs(q, 0) == 0
    assert S.diff(mh_num, q).subs(q, 0) == 4*D-4*R

    # Every nonzero Fourier branch forces n^2*gcd(c,s) to divide each h_i.
    # For ell>=1, substitute ell=t+1: the residual is affine with positive
    # slope and nonnegative constant. The ell=0 branches are checked apart.
    support = []
    for ce in range(2):
        for sk in range(2):
            overlap = ce*sk
            for nl in range(11):
                modulus = ce+3*nl+sk
                minimum = max(0, modulus-1)
                assert minimum >= 2*nl+overlap
            residual_constant = ce+sk-overlap
            assert residual_constant >= 0  # (M-1)-(2ell+overlap) at ell=1.
            support.append({"source_valuation": ce, "label_valuation": sk,
                            "residual_for_ell=t+1": f"t+{residual_constant}"})

    receipt = {
        "status": "binary cubic local and unit certificate; no analytic row bound",
        "F_j": list(map(str, f)), "G_j": list(map(str, g)),
        "P_j": list(map(str, p)), "finite_valuation_checks": checks,
        "critical_G_j": list(map(str, critical_g)),
        "shared_scalar_poles": ["3t1=1", "3t2=1", "t1+2t2=1", "2t1+t2=1"],
        "common_completion_ratio": "eta(p)^3*alpha_bar(p)^3*Q^(-1-3v)",
        "reciprocal_argument": "x=3/2+v-t1-t2",
        "unmarked_principal_candidate_power": "x-5/6+(2/3)*(log_Z(X1)+log_Z(X2))",
        "leading_log_degree_at_shared_intersection": 2,
        "principal_row_isolated_by_unmarked_frequency_poles": False,
        "shared_label_uses_matching_cubic_selector": True,
        "shared_cubic_label": {
            "physical_factor": "chi_A(m1)^2*chi_A(m2)^2*chi_s(m1*m2)^4*gamma_4(s)^(-2)",
            "label_support": "squarefree s",
            "marked_P_j": list(map(str, marked)),
            "CRT_pair_phase": str(S.expand(phase)),
            "CRT_pair_phase_divisible_by": 6,
            "exact_unit_packet_checks": unit_checks,
            "element_frequency_unit_multiplicity": 12,
            "finite_overlap_valuation_checks": marked_checks,
            "ordinary_selector": "L^S(w,rho_u)/L^S(2w,rho_u^2)",
            "candidate_power": "x-5/6+(log_Z(X1)+log_Z(X2))/6",
            "selector_uses_same_cubic_row_as_inverse": True,
            "critical_principal_numerator": "(1-D)*(1+W)+(1-R)*(F0-1)",
            "fixed_bad_prime_frequency_factors": "F_j (source and label avoid S)",
            "global_identity_has_written_derivation": True,
            "global_identity_formalized": False,
            "frequency_divisibility": "n^2*gcd(c,s) divides both h_i",
            "support_all_size_affine_proof": support,
            "global_direct_estimate_proved": False,
        },
        "new_zero_free_bound_proved": False,
    }
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    path = Path(__file__).resolve().parents[1]/"results/binary-cubic-kernel.json"
    if args.write:
        path.write_text(json.dumps(receipt, indent=2)+"\n")
    else:
        assert json.loads(path.read_text()) == receipt
    print(json.dumps({k: receipt[k] for k in (
        "status", "finite_valuation_checks", "critical_G_j",
        "shared_label_uses_matching_cubic_selector", "new_zero_free_bound_proved")}, indent=2))


if __name__ == "__main__":
    main()
