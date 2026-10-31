#!/usr/bin/env python3
"""Exact residue-character algebra and amplification cost, not an analytic bound."""
import json
import sympy as s

if not __debug__:
    raise RuntimeError("Verification requires assertions enabled; omit -O/PYTHONOPTIMIZE.")


def prime_factors(n):
    result = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0)+1
            n //= p
        p += 1
    if n > 1:
        result[n] = result.get(n, 0)+1
    return result


def character_table(p):
    generator = next(g for g in range(2, p)
                     if len({pow(g, j, p) for j in range(p-1)}) == p-1)
    table = {0: None}
    for j in range(p-1):
        table[pow(generator, j, p)] = j % 6
    return table


def multiply(x, y):
    return None if x is None or y is None else (x+y) % 6


def main():
    phase_checks = 0
    failed_without_compensator = 0
    for p in [7, 13, 19, 31, 37, 43, 61]:
        table = character_table(p)
        for u in range(p):
            for a in range(p):
                lifted = table[u*pow(a, 3, p) % p]
                compensator = table[pow(a, 3, p)]
                expected = None if a == 0 else table[u]
                assert multiply(lifted, compensator) == expected
                phase_checks += 1
                failed_without_compensator += lifted != expected
        # On coprime columns the compensator removes all amplifier phase.
        assert all(multiply(table[pow(a, 3, p)], table[pow(a, 3, p)]) == 0
                   for a in range(1, p))
    assert failed_without_compensator > 0

    # Prime cubic lifts of sixth-free cores have only logarithmic multiplicity.
    # This is a finite replay of the valuation proof, not a bound by sampling.
    collision_checks = 0
    for value in range(1, 20001):
        valuations = prime_factors(value)
        allowed = [p for p, e in valuations.items()
                   if e >= 3 and all(k-3*(q == p) < 6
                                     for q, k in valuations.items())]
        assert len(allowed) <= sum(e >= 3 for e in valuations.values())
        assert 2**(3*len(allowed)) <= value
        for p in allowed:
            assert all(e < 6 for e in prime_factors(value//p**3).values())
            collision_checks += 1
    assert collision_checks > 0

    r, tau = s.symbols("r tau", real=True)
    exponent = 1+(2+tau)*(r-1)/3
    assert s.factor(exponent.subs(tau, s.Rational(1, 2))-(1+5*r)/6) == 0
    assert s.factor(exponent.subs(tau, 0)-(1+2*r)/3) == 0
    assert s.factor(exponent.subs(tau, 1)-r) == 0
    direct_threshold = s.Rational(1, 2)+(2+tau)/6
    assert s.factor(direct_threshold-(5+tau)/6) == 0
    print(json.dumps({
        "status": "exact cubic compensation and cost identities; mixed analytic estimate unproved",
        "finite_field_phase_checks": phase_checks,
        "uncompensated_failures": failed_without_compensator,
        "integer_prime_lift_preimages_checked": collision_checks,
        "mixed_family_cost": "U*V^(3+tau), D <= U*V^3",
        "extracted_source_exponent_r_ge_1": str(exponent),
        "strict_improvement_requires": "tau < 1/2",
        "tau_half_recovers_existing_sextic_exponent": True,
        "amplifier_phase_on_common_coprime_columns": "identically one, not oscillatory",
        "conditional_direct_mertens_threshold": str(direct_threshold),
        "phase_lean_file": "lean/CubicCompensation.lean",
        "l_function_bound_established": False,
    }, indent=2))


if __name__ == "__main__":
    main()
