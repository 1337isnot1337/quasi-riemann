#!/usr/bin/env python3
"""Check the local cube-support lemma with labelled ideal primes."""
from itertools import product
import json
from math import prod
from pathlib import Path

if not __debug__:
    raise RuntimeError("Verification requires assertions enabled; omit -O/PYTHONOPTIMIZE.")


def main():
    # Two distinct primes of norm 7 model conjugate split ideal primes.
    norms = (7, 7, 13)
    cases = pure_powers = 0
    by_order = {}
    for order in range(2, 7):
        count = 0
        for inv in product(range(2), repeat=3):
            for ordinary in product(range(2*order+3), repeat=3):
                total = tuple(a+b for a, b in zip(inv, ordinary))
                root = tuple(v//order for v in total)
                core = tuple(v % order for v in total)
                assert all((order-1)*b <= e for b, e in zip(root, ordinary))
                nd = prod(q**v for q, v in zip(norms, inv))
                ne = prod(q**v for q, v in zip(norms, ordinary))
                na = prod(q**v for q, v in zip(norms, core))
                nb = prod(q**v for q, v in zip(norms, root))
                assert nd*ne == na*nb**order
                assert ne % nb**(order-1) == 0
                assert na**(order-1)*ne >= nd**(order-1)
                if not any(core):
                    assert nd**(order-1) <= ne
                    pure_powers += 1
                cases += 1
                count += 1
        by_order[str(order)] = count
    # The all-size proof treats the two inverse valuations and all residues.
    residues = []
    for order in range(2, 7):
        for inv in range(2):
            for rem in range(order):
                carry = (rem+inv)//order
                residual_constant = rem-(order-1)*carry
                assert residual_constant >= 0
                residues.append({"order": order, "inverse_valuation": inv,
                                 "ordinary_residue": rem,
                                 "ordinary_minus_root_power": f"t+{residual_constant}"})
    # Both hypotheses matter: squarefree ideal support, not rational norm support.
    assert 2*((2+1)//3) > 1  # inverse valuation 2 invalidates the lemma.
    assert all(v <= 1 for v in (1, 1, 0))
    assert norms[0]*norms[1] == 7**2  # norm-squarefree would wrongly reject it.
    # Equality holds for d=p, e=p^2: de=p^3 and root^2=e.
    assert 2*((1+2)//3) == 2
    receipt = {
        "status": "ideal-valuation support lemma and finite checks; no moment estimate",
        "lemma": "d squarefree and d*e=a*b^k with a k-free imply b^(k-1) divides e",
        "norm_consequence": "N(a)^(k-1)*N(e) >= N(d)^(k-1)",
        "all_size_proof": residues,
        "finite_labelled_prime_norms": list(norms),
        "finite_cases": cases, "pure_power_cases": pure_powers,
        "finite_cases_by_order": by_order,
        "negative_controls": ["inverse valuation 2", "distinct equal-norm prime ideals"],
        "analytic_mixed_energy_proved": False,
    }
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    path = Path(__file__).resolve().parents[1]/"results/inverse-support.json"
    if args.write:
        path.write_text(json.dumps(receipt, indent=2)+"\n")
    else:
        assert json.loads(path.read_text()) == receipt
    print(json.dumps({k: receipt[k] for k in (
        "status", "finite_cases", "negative_controls", "analytic_mixed_energy_proved")}, indent=2))


if __name__ == "__main__":
    main()
