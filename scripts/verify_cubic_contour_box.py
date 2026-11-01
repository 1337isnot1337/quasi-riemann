#!/usr/bin/env python3
"""Exact Euler-contour and exponent bookkeeping for an unproved direct target."""
import argparse
from itertools import product
import json
from pathlib import Path

import sympy as S

if not __debug__:
    raise RuntimeError("Verification requires assertions enabled.")


def main():
    A, B, Q, R, D, W, T = S.symbols("A B Q R D W T")
    x, t1, t2, w = S.symbols("x t1 t2 w")
    epsilon = S.Rational(1, 1000)
    x_buffer = S.Rational(1, 1000000)
    theta = S.Rational(21, 25)
    a1, a2, y = S.Rational(73, 100), S.Rational(99, 100), S.Rational(73, 100)
    h = 2-a1-a2
    zlo, zhi = S.Rational(1, 3)-epsilon, S.Rational(1, 3)+epsilon
    wlo = S.Rational(1, 2)+epsilon
    ranges = ((theta,), (zlo, S.Integer(2)),
              (zlo, S.Integer(2)), (wlo, S.Integer(2)))
    vertices = [dict(zip((x, t1, t2, w), v)) for v in product(*ranges)]

    den = (1-A**3)*(1-B**3)
    f = [v/den for v in (1+A*B**2+A**2*B, A+B+A**2*B**2, A**2+A*B+B**2)]
    g = []
    for j in range(3):
        rj = (j+1) % 3
        g.append((1-1/Q)**2*f[j]-(1-1/Q)/Q*(
            A**-1*B**rj/(1-B**3)+A**rj*B**-1/(1-A**3))
            +int(j == 1)/(A*B*Q**2))
    marked0 = f[0]+(R*g[0]+W-D-D*W*Q**2*A**2*B**2*g[2])/(1-R)
    correction = marked0*(1-R)*den*(1-A*B**2)*(1-A**2*B)/((1-D)*(1+W))
    numerator = S.expand(S.cancel((correction-1)*(1-D)*(1+W)))

    def exponent(term):
        powers = term.as_powers_dict()
        aa, bb, qq, rr, dd, ww, tt = [powers.get(k, 0) for k in (A,B,Q,R,D,W,T)]
        assert all(v >= 0 for v in (rr, dd, ww, tt))
        return S.expand(dd*x+ww*w+tt*(x+w)+aa*t1+bb*t2
                        +rr*(3*x-S.Rational(7,2)+3*t1+3*t2)-qq)

    rows = []
    for term in S.Add.make_args(numerator):
        decay = exponent(term)
        assert S.Poly(decay, x, t1, t2, w).total_degree() <= 1
        assert S.diff(decay, x) >= 0  # covers the unbounded x half-line.
        lo = min(decay.subs(v) for v in vertices)
        assert lo >= S.Rational(267, 200)
        rows.append({"term": str(term), "decay": str(decay), "minimum": str(lo)})
    assert len(rows) == 78
    assert min(S.Rational(r["minimum"]) for r in rows) == S.Rational(267, 200)
    r_decay = 3*x-S.Rational(7,2)+3*t1+3*t2
    r_min = min(r_decay.subs(v) for v in vertices)
    assert r_min == S.Rational(507, 500) and r_min > 1

    # At the estimating lines, finite ramified factors retain N(u)^(-zhi).
    ramified = {}
    for j in (1, 2):
        mj = f[j]+(R*g[j]-T*Q**2*A**2*B**2*g[(j-1) % 3])/(1-R)
        nr = S.expand(S.cancel(mj*(1-R)*den))
        local = []
        for term in S.Add.make_args(nr):
            decay = S.expand((exponent(term)-j*t1).subs({t1: zhi, t2: zhi}))
            assert S.diff(decay, x) >= 0
            lo = min(decay.subs({x: vx, w: vw}) for vx, vw in product(ranges[0], ranges[3]))
            assert lo >= 0
            local.append({"term": str(term), "relative_decay": str(decay), "minimum": str(lo)})
        ramified[str(j)] = local

    # Full row count plus classical conductor convexity; no density input.
    small_loss = S.Rational(1, 100000)
    row_exponent = 1+(1-wlo)/2-zhi+3*small_loss
    high = x_buffer+h*(zhi-S.Rational(1,3))+y*(wlo-1)+(h+epsilon)*row_exponent
    assert high < -S.Rational(1, 10)
    assert -y/2+S.Rational(11,12)*h == -S.Rational(13,120)

    freq_margins = {
        "first_left_integral": (a2-a1)*epsilon-x_buffer,
        "skew_pole_residue": ((1-a1)/2-(1-a2))*epsilon-x_buffer,
        "triple_pole_left_integral": (1-a2)*epsilon-x_buffer,
    }
    assert 1-a1 > 2*(1-a2)
    assert min(freq_margins.values()) == S.Rational(9, 1000000)
    assert all(v > S.Rational(1,200000) for v in freq_margins.values())

    principal_shift = S.Rational(5,6)-(a1+a2)/6
    direct_reserve = S.Rational(1,10000)
    direct_power = theta-principal_shift-direct_reserve
    assert principal_shift == S.Rational(41,75)
    assert theta-principal_shift == S.Rational(22,75)
    # Comparison only: diagonal Gauss means plus Cauchy are still insufficient.
    m = a1+y
    ideal_diagonal_direct = S.Rational(1,2)-a2/2-y/2+m/2
    assert ideal_diagonal_direct+principal_shift == S.Rational(11,12)
    assert ideal_diagonal_direct-(theta-principal_shift) == S.Rational(23,300)

    receipt = {
        "status": "exact contour and exponent certificate; direct estimate unproved",
        "theta_target": str(theta), "parameters": {"a1":str(a1),"a2":str(a2),"y":str(y),"h":str(h)},
        "contour_box": {str(k):list(map(str,v)) for k,v in zip((x,t1,t2,w),ranges)},
        "x_upper_endpoint": "infinity; all decay coefficients of x nonnegative",
        "unramified_numerator": rows, "minimum_decay": "267/200", "angular_minimum":str(r_min),
        "ramified_relative_decay": ramified,
        "x_buffer":str(x_buffer), "frequency_displacement":str(epsilon),
        "high_relative_exponent":str(high), "high_saving_at_least":"1/10",
        "frequency_error_margins": {k:str(v) for k,v in freq_margins.items()},
        "principal_power": "x-41/75", "principal_log_degree":2,
        "direct_target_power":str(direct_power), "direct_reserve":str(direct_reserve),
        "ideal_diagonal_Cauchy_threshold":"11/12", "missing_correlation_saving":"23/300",
        "direct_estimate_proved":False, "new_zero_free_bound_proved":False,
        "analytic_derivation_formalized":False,
    }
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    path = Path(__file__).resolve().parents[1]/"results/cubic-contour-box.json"
    if args.write:
        path.write_text(json.dumps(receipt,indent=2)+"\n")
    else:
        assert json.loads(path.read_text()) == receipt
    print(json.dumps({k:receipt[k] for k in ("status","theta_target","minimum_decay",
        "high_saving_at_least","direct_target_power","direct_estimate_proved")},indent=2))


if __name__ == "__main__":
    main()
