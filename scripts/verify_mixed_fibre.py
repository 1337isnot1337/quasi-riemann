#!/usr/bin/env python3
"""Exact mixed-moment accounting on a fixed detector fibre; no analytic claim."""
import json
from pathlib import Path

import sympy as s

if not __debug__:
    raise RuntimeError("Verification requires assertions enabled; omit -O/PYTHONOPTIMIZE.")

ROOT = Path(__file__).resolve().parents[1]
Q = s.Rational


def main():
    delta, p, B, lam, m, n, R, T, z = s.symbols(
        "delta p B lam m n R T z", real=True)
    q = delta*p
    plain_count = 1-2*delta*m-2*q*(B-2*m)/lam
    cap_n = (B-2*n)/lam
    cap_mixed = (B-m-n)/lam
    fourth = (3*R+1)/4-q*cap_n/2
    mixed_plain = (R+1-delta*m)/2-q*cap_mixed
    # A mixed S/P estimate gives exactly the interpolation of two old bounds.
    assert s.factor(mixed_plain-fourth-(plain_count-R)/4) == 0

    # A simultaneous extremizer for every budgeted two-ordinary-factor moment.
    l1, l2 = s.symbols("l1 l2", real=True)
    alpha = (1-R-2*q*B/lam)/4
    amplitude = lambda l: alpha+q*l/lam
    energy = R+2*amplitude(l1)+2*amplitude(l2)+2*q*z
    assert s.factor(energy-1-2*q*(l1+l2+lam*z-B)/lam) == 0
    assert s.factor((amplitude(m)-delta*m/2).subs(R, plain_count)) == 0
    assert s.factor(R+amplitude(n)-fourth) == 0

    def fibre(density, packet_length):
        prime = density/2
        V = Q(5, 6)-density
        J = Q(3, 2)*V+density/2
        cutoff = 1+density/(4*J)
        inv = 2*cutoff/3
        plain = cutoff/3
        count = 1-density+V*(cutoff-1)
        ap = density*plain/2
        ai = density*inv/2
        an = (1-count-prime)/4+prime*packet_length/2
        cn = (1-2*packet_length)/2
        sp = (1-2*plain)/2
        si = (1-inv)/2
        snp = (1-packet_length-plain)/2
        assert s.simplify(count+4*ap+2*prime*sp-1) == 0
        assert s.simplify(count+2*ai+2*prime*si-1) == 0
        assert s.simplify(count+4*an+2*prime*cn-1) == 0
        assert s.simplify(count+2*ap+2*an+2*prime*snp-1) == 0
        assert 0 < density < Q(3, 4) and 0 < count < 1
        assert 0 < plain < Q(1, 2) and 0 < packet_length < Q(1, 2)
        assert 0 < inv < 1 and 0 < cn and 0 < si and 0 < sp
        # Neither the trivial pointwise bound nor empty-slot pair moments exclude it.
        assert 0 < ap <= plain/2 and 0 < an <= packet_length/2
        assert 4*ap <= 1-count and 4*an <= 1-count
        # New mixed inverse/numerator moment, with selected width z.
        inv_mixed = (count+T-density*inv)/2-prime*z
        packet = count+an
        threshold = s.simplify(2*packet-count+density*inv+2*prime*z)
        assert s.simplify(inv_mixed-packet-(T-threshold)/2) == 0
        return {"delta": density, "n": packet_length, "t": cutoff,
                "r": inv, "m": plain, "R": count, "q": prime,
                "packet_amplitude": an, "plain_amplitude": ap,
                "inverse_amplitude": ai, "packet_sum": packet,
                "inverse_mixed_T_critical_without_marks": threshold.subs(z, 0),
                "inverse_mixed_support_without_marks": packet_length+inv}

    rational = fibre(Q(3, 7), Q(3, 7))
    radical = s.sqrt(1081)
    density = (61-radical)/66
    c = (75+radical)/852
    h = Q(32, 71)+Q(838, 76751)*radical
    nstar = s.simplify(2*(4*c-Q(1, 3))/h)
    contact = fibre(density, nstar)
    serial = lambda data: {k: str(s.simplify(v)) for k, v in data.items()}
    receipt = {
        "status": "exact fixed-fibre exponent obstruction and mixed-input accounting; no L-function theorem",
        "mixed_plain_minus_fourth": "(plain_count-R)/4",
        "continuum_energy_identity": "R+2*a(l1)+2*a(l2)+2*q*z = 1+(2*q/lam)*(l1+l2+lam*z-B)",
        "rational_fibre": serial(rational),
        "inherited_contact_fibre": serial(contact),
        "inherited_contact_decimals": {k: str(s.N(v, 25)) for k, v in contact.items()},
        "mixed_inverse_input_proved": False,
        "scope": "one common detector fibre; abstract positive arrays, not actual Hecke characters",
    }
    path = ROOT/"results/mixed-fibre.json"
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    if args.write:
        path.write_text(json.dumps(receipt, indent=2)+"\n")
    else:
        assert json.loads(path.read_text()) == receipt, "Stored certificate differs from replay"
    print(json.dumps({"status": receipt["status"],
                      "mixed_plain_gain": "none when R<=plain_count",
                      "inverse_mixed_T_critical_without_marks": str(s.N(contact[
                          "inverse_mixed_T_critical_without_marks"], 25)),
                      "mixed_inverse_input_proved": False}, indent=2))


if __name__ == "__main__":
    main()
