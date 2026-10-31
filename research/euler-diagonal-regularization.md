# Extracting the diagonal Euler factor

This is a local Euler-product continuation lemma for the existing detector.
It does not bound the signed sum over rows or improve a zero-free half-plane.
Its purpose is to reach the diagonal `x+w=1` before taking absolute values.
Three explicit scalar extractions leave a normally convergent remainder near
both that diagonal and `z=1/6`, for `51/100<=Re(x)<=7/8`.

## Source and notation

We use the complete local identity in OpenAI's 30 September 2026 paper,
Section "The scalar Euler identity", equations `old-eq:5.13a` and
`eq:local-H-definition`. The [pinned TeX source](https://raw.githubusercontent.com/openai/math/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)
has SHA-256 `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.
The tracker counterparts `Detector/EulerCoordinates.lean`,
`HighEulerRational.lean`, `HighRowsUnramified.lean` and `CorrectionBounds.lean`
are hash-pinned in the source lock. We have inspected these formulas, without
building their upstream Lean dependency closure. Credit for the complete local
identity belongs to the source authors; the factorization below is our audit.

Let `u` be a nonzero sixth-power-free row, coprime to the fixed bad set `S`.
At a prime ideal outside `S`, put `Q=N(p)`, `j=v_p(u)`, and `sigma=x+w`.
The target character is `eta`. Write

```
V = Q^(-6z),               R = a^2 Q^(4-6x-6z),
T = eta(p) Q^(-sigma).
```

Here `a`, `b`, and `rho` are the unit phases in the source, with `b^3=a^2`.
At an unramified prime, also put
`D=eta(p) rho^(-1) Q^(-x)` and `W=rho Q^(-w)`, so `DW=T`.
At a prime dividing `u`, `D=W=0` by the original character's zero extension,
whereas `T` remains the displayed target-character value. Confusing these two
definitions would erase the ramified correction.

## Continuation lemma

On the real box

```
51/100 <= Re(x) <= 7/8,
99/100 <= Re(sigma) <= 101/100,
17/50  <= Re(z),
```

the product

```
K_eta,u(x,w,z) = product_(p outside S) [(1-T) H_p(x,w,z)]
```

converges normally on a neighborhood of every point. It is holomorphic there.
Uniformly in all imaginary parts and unit phases, for every positive epsilon,

```
|K_eta,u(x,w,z)| <<_epsilon
    N(u)^(max(0,1-Re(sigma))/2 + epsilon).
```

In particular, its row growth is `N(u)^epsilon` on and to the right of the
diagonal. On the overlap with the source's original convergence region,

```
H_eta,u = L^S(sigma,eta) K_eta,u.
```

This identity supplies a meromorphic continuation of the source correction
across the diagonal. When `eta` is principal, `L^S(sigma,eta)` has a simple pole
at `sigma=1`; it must be retained in any subsequent contour argument. The lemma
does not assert that `K` is nonvanishing or that this pole never cancels.

## Proof at unramified primes

The complete local formula gives

```
P = 1/(1-V) + W/(1-W)
  + { [R(1-1/Q)-(Q-1)T V]/(1-V) - D + WR }/(1-R),
H = P (1-V)(1-W)/(1-D).
```

There is no `1-W` denominator after simplification. Set `B=1-D+T` and

```
E = V [D(1-W)(1+W-QW)-W]
  + R [B-(1-V)W^2+(W-1)/Q].
```

Exact rational algebra gives

```
H = B/(1-D) + E/[(1-R)(1-D)],
[(1-T)H-1](1-R)(1-D)
  = (1-R)T(D-T) + (1-T)E.
```

The numerator in the last line has 20 Laurent monomials. A monomial
`D^d W^v V^k R^r Q^q` has absolute value at most `Q^(-e)`, where

```
e = (d-v+6r) Re(x) + v Re(sigma)
  + (6k+6r) Re(z) - 4r - q.
```

For all 20 terms, `e>=11/10` on the entire box. The accompanying rational
certificate checks every vertex of the rectangle and the nonnegative
coefficient of `Re(z)`. Thus it covers the unbounded z half-line, rather than a
finite grid. The minimum is attained by the term `R`.

Also `|D|<=Q^(-51/100)` and `|R|<=Q^(-11/10)`. Both denominators are uniformly
bounded away from zero, proving `(1-T)H-1=O(Q^(-11/10))`. Strict margins in
these estimates give a neighborhood of each point of the stated box.

The extraction matters already with `R=V=0`: then

```
H = 1 + T/(1-D),
(1-T)H - 1 = T(D-T)/(1-D).
```

The original leading term `T` has decay exponent `Re(sigma)`, which does not
give absolute prime summability on the diagonal. The remaining terms do.

## Ramified primes and the row cost

For valuation one, the exact formula simplifies to

```
H_1 = (1+T-QTV-R/Q)/(1-R),
[(1-T)H_1-1](1-R)
  = -T^2-QTV+QT^2V+R-R/Q+RT/Q.
```

Each of these six monomials also has decay at least `11/10` on the box.
Hence all primes of valuation zero or one together have a uniformly bounded
normally convergent product, independently of the choice of `u`.

For valuations `j=2,3,4,5`, the complete formula is

```
H_j = [1-R/Q-(Q-1)T+(1-V)J_j]/(1-R).
```

The respective source boundary terms have minimum decay exponents

| j | Minimum decay exponents of the terms in J_j |
|---|---|
| 2 | 3/100 |
| 3 | 1/100, 1/25 |
| 4 | 1/50 |
| 5 | 3/50 |

The only possible positive power is `QT`, with magnitude
`Q^(1-Re(sigma))`. Thus each such prime contributes at most
`C Q^max(0,1-Re(sigma))` for an absolute `C`. Their product is bounded by

```
C^omega(u) rad_(valuation>=2)(u)^max(0,1-Re(sigma)).
```

Every prime in this radical divides `u` to at least the second power, so the
radical's norm is at most `N(u)^(1/2)`. The standard divisor-product estimate
absorbs `C^omega(u)` into `N(u)^epsilon`. This proves the stated row growth.
In particular, claiming a uniform `N(u)^epsilon` bound throughout the left side
of the box would omit an actual repeated-prime cost.

## A second extraction reaches the z residue

The term `-QTV` in the first remainder can itself approach prime-summability's
boundary as `z` approaches `1/6`. Extract its Euler factor too. Define

```
K2_p = (1-T) H_p / (1-QTV).
```

On the larger, overlapping box

```
4/5 <= Re(x) <= 7/8,
99/100 <= Re(sigma) <= 101/100,
33/200 <= Re(z),
```

the unramified and valuation-one defects satisfy
`K2_p-1=O(Q^(-219/200))`. Here
`|QTV|<=Q^(-49/50)`, so the additional local denominator is bounded away
from zero. The same all-size vertex argument checks the 22 monomials in

```
(K2_p-1)(1-R)(1-D)(1-QTV)
```

at unramified primes. At valuation one its numerator is the preceding
six-term numerator plus `QTV(1-R)`, whose worst term cancels.
For higher valuations every `J_j` term still has positive decay, and the
radical bound is unchanged. Consequently `K2=product K2_p` is holomorphic
near this second box with the same stated row growth. On the overlap,

```
H_eta,u = L^S(sigma,eta) / L^S(sigma+6z-1,eta) * K2_eta,u.
```

This is a meromorphic continuation, with the new reciprocal explicitly
retained. A contour crossing zeros of its denominator needs a separate
argument. The appearance of `4/5` here describes a local convergence region;
it is not a zero-free threshold.

On the hyperplane `z=1/6` the scalar L-ratio cancels as a meromorphic function
of `sigma`. This restriction does not remove intersecting polar divisors
from the surrounding two-variable function. For principal `eta`, if
`t=z-1/6` and `r=sigma-1`, its leading polar geometry is

```
L^S(sigma,eta)/L^S(sigma+6z-1,eta) ~ (r+6t)/r.
```

Multiplication by `zeta_F^S(6z)` therefore retains poles on both `t=0`
and `r=0`. Restricting to `t=0` before moving contours would hide the latter.
Indeed the residue on `sigma=1` of this entire scalar factor is exactly
the residue of `zeta_F^S` at one: `zeta_F^S(6z)` cancels the denominator
in that residue, initially away from its zeros and poles and then by
meromorphic continuation.

## Extracting the angular geometric factor

The remaining factor `(1-R)^(-1)` is also a scalar Euler factor. In the
source, `alpha(p)` is the normalized complex embedding of the prime's primary
generator. Thus

```
psi_eta(p) = conjugate(alpha(p))^6 eta(p)^6
```

extends multiplicatively to a unitary Hecke character, with angular infinity
type -6. Changing the generator by a unit has no effect on its sixth power;
the finite character's sixth power is unit-trivial too. Equivalently this
uses the multiplicative primary generators and `angularFactor_mul` in the
baseline `Arithmetic/IdealMobius.lean`. Consequently

```
product_p (1-R)^(-1) = L^S(6x+6z-4,psi_eta)
```

in absolute convergence. This character has nontrivial infinity type, so its
standard Hecke L-function has entire continuation, by the global continuation
theorem in [Tate's thesis](https://sites.math.rutgers.edu/~alexk/2023S572/Tate1950.pdf).
It occurs in the numerator,
and its zeros require no division. It is different from the source's finite-order
row family and should not be silently counted as a member of that family.

Put `K3_p=(1-R)K2_p`. On

```
51/100 <= Re(x) <= 7/8,
99/100 <= Re(sigma) <= 101/100,
33/200 <= Re(z),
```

the unramified defect has just 18 Laurent monomials after multiplication
by `(1-D)(1-QTV)`, with minimum decay `101/100`. The limiting term is
`-RW^2`, whose decay is `4 Re(x)+2 Re(sigma)+6 Re(z)-4`.
At valuation one the cleared numerator is

```
-T^2+QT^2V-R/Q+RT/Q.
```

The ramified boundary terms and radical bound are the same as before; the
`1-R` denominator has now canceled. Hence `K3=product K3_p` is normally
convergent and holomorphic near the box, with the same row growth, and

```
H_eta,u = L^S(6x+6z-4,psi_eta)
          * L^S(sigma,eta)/L^S(sigma+6z-1,eta) * K3_eta,u.
```

The identity is obtained first in the source's convergence region and then
continued through the overlapping boxes. It is not a claim that the original
uncorrected Euler product converges in the enlarged region. The exact
certificate verifies the local rational identity and every affine decay bound;
the identification and continuation of the fixed angular Hecke L-factor use
standard Hecke character theory, rather than a new kernel proof in this repo.

## What is still needed

Substitution into the original fixed-row identity gives

```
F_eta,u = zeta_F^S(6z) L^S(w,chi_u) L^S(x+w,eta)
          / L^S(x,eta*conjugate(chi_u)) * K_eta,u.
```

The second extraction replaces its last two factors by the displayed L-ratio
and `K2`, reaching a neighborhood of the original z residue as well.
This reaches the diagonal at the level of an individual row's correction.
It does not justify continuation or rearrangement of the infinite sum over
`u`, nor does it bound its root-number phases. The row series is far outside
absolute convergence at the contemplated z line. A full detector argument must
control that signed series, retain all crossed poles, and preserve the nonzero
principal signal and its normalization. These are the next proof obligations.

The existing return-model obstruction also explains a limit of this result:
moving only the z contour cancels from the exponent at the obstructing scale
`d=h`. Thus even the larger correction region does not by itself cross that
barrier. It is useful only if it enables a different treatment of the coherent
row sum or a change to the detector's signal/error comparison.

Replay the rational identities, all-size affine decay inequalities, and both
negative controls with `scripts/verify_euler_regularization.py`. Its receipt is
`results/euler-regularization.json`. This is a symbolic certificate and a written
analytic proof, without a Lean formalization or a new zero-free bound.
