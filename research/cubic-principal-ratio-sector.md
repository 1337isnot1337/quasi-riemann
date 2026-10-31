# Small physical cubic cores are below the 0.84 target

Status: written elementary bounds for full sectors of the radial cubic
probe, using its exact one-Poisson identity and standard ideal counting.
Completion indices and source/label overlaps are included. It does not bound
the complementary sector or prove a new zero-free region. The analytic proof
is not formalized in Lean; the local Gauss inequalities and exponent accounting
have exact checks in `scripts/verify_cubic_signed_budget.py`.

Use the probe and profiles of the separate
[shared-label identity](https://github.com/1337isnot1337/quasi-riemann/blob/297a7efac59ea6f8f801b027d3f4f03872716a68/research/shared-label-cubic-identity.md).
Thus A=c*n^3, c and the label s are squarefree, B is annular, V has arbitrary
power decay at both ends, W1 is a radial Schwartz function, and the second
radial Fourier profile U2 is Schwartz with U2(0)=0. All character and Gauss
zero masks are the original ones. Write q_a=N(a).

## Definition of the sector

Poisson transform only P2 and retain the physical element m of P1. Denote
the nonzero second frequency by h. Let J_cube be the resulting complete
subsum with m/h a cube up to an S-unit. This is a geometric partition of
the actual sum, before any character or Gauss estimate. For coprime,
completion-free variables it includes the principal cubic ratio character.
It also includes the fixed bad-prime cube classes. The target eta, completion
n and all source/label overlaps remain in the subsum.

The claim, for X1,X2,Y,Z>=1, is

```text
|J_cube| << Z^(7/6) * (X1*Y)^(-1/6) * X2^(-2/3).
```

The constant depends on S and fixed profile seminorms. At
X1=Y=Z^(73/100), X2=Z^(99/100), this is Z^(79/300). The reserved
direct target Z^(8797/30000) is larger by exactly Z^(299/10000).

## A Gauss bound that retains every imprimitive case

For M=A*s the character chi_A^2*chi_s^4 is, at each good prime, either
principal on the units or induced from a nonprincipal character modulo p.
For a modulus p^v, the latter Gauss sum is zero unless v_p(h)=v-1, and
then its absolute value is q^(v-1/2). The principal case is the Ramanujan
sum: its absolute value is q^(v-1) at valuation v-1, at most q^v at
valuation at least v, and zero below v-1. Hence in every case

```text
|g_(chi_A^2*chi_s^4)(A*s,h)|
 <= sqrt(q_(A*s))*sqrt(q_gcd(A*s,h))
 <= sqrt(q_(A*s))*sqrt(q_h).
```

Chinese remaindering preserves this bound. The fixed self-dual lattice
normalization has only a fixed S-dependent factor. No coprimality between
c,n,s or h is imposed in this estimate.

Combining it with the exact one-Poisson factor
`sqrt(X2)/(q_A*sqrt(q_s))`, the source factor `1/(sqrt(q_c)*q_n)`,
and the P1 normalization gives the absolute coefficient majorant

```text
sqrt(X2/X1)/Y * 1/[q_c*q_n^(5/2)*sqrt(q_s)] * sqrt(q_h).
```

## Counting the cube-ratio pairs

First ignore the finitely many S-unit classes. The ideals of m and h have
one common cube-free core u, so write `(m)=u*a^3`, `(h)=u*b^3`.
For q_m<=M, q_h<=H and M,H>=1, ideal counting gives

```text
#pairs << M^(1/3) H^(1/3) sum_(q_u<=min(M,H)) q_u^(-2/3)
       << M^(1/3) H^(2/3).
```

Unit multiplicities are bounded. S-prime valuations modulo three give
finitely many additional fixed representatives; their cube parts enter
a,b. Thus the same bound holds for cubes up to S-units. Dyadic summation
with the fixed Schwartz profiles, including the factor sqrt(q_h), yields

```text
sum_(m/h cube up to S-unit) sqrt(q_h)
    * |W1(q_m/M) U2(q_h/H)| << M^(1/3) H^(7/6).
```

This remains true when H<1, by rapid decay of U2 at infinity. Here
M=q_s*X1>=1 and H=q_A/X2. Zero h contributes nothing because U2(0)=0;
zero m vanishes by the original character mask for sufficiently large Y.

## Summing all original variables

The s sum costs `Y^(5/6)*X1^(1/3)` after the factor q_s^(-1/2).
For each n, with T=Z/q_n^3, arbitrary power decay of V and ideal counting give

```text
sum_c q_c^(-1) (q_c*q_n^3)^(7/6) |V(q_c*q_n^3/Z)|
 = q_n^(7/2) sum_c q_c^(1/6) |V(q_c/T)| << Z^(7/6).
```

For T<1 choose a decay order greater than 7/6; for T>=1 use dyadic ideal
counting. This bound is uniform in n. Finally sum q_n^(-5/2), which
converges. Combining the factors proves the claimed full-sector bound.
No Möbius or Gauss cancellation was used.

Every fixed aspect-rescaled copy satisfies the same exponent, so the
three-term contrast's cube sector is below its target too. Consequently
the missing 0.84 direct estimate can be restricted to the complementary
physical ratios. This does not identify that complement with a published
centered-source remainder: its prescribed coefficients, profiles and masks
still need to be retained.

This physical partition uses m/h after one Poisson step. The high reciprocal
signal instead uses the cube class of h1*h2 after two Poisson steps. The two
conditions differ; bounding the former sector does not remove that signal.

## A positive-power range of small cores can also be removed

Let u=u1*u2^2 be the cube-free ideal of the Kummer class of m/h outside S.
Here u1,u2 are squarefree and coprime. Fix this class and write the cube-free
parts of m,h with valuations jm,jh in {0,1,2}. At a prime of u, the permitted
pairs and their counting weights are

```text
v_p(u)=1: (jm,jh)=(1,0),(2,1),(0,2),
          q^(-1/3), q^(-4/3), q^(-4/3);
v_p(u)=2: (jm,jh)=(2,0),(0,1),(1,2),
          q^(-2/3), q^(-2/3), q^(-5/3).
```

These weights follow by extracting the fixed factors m0,h0 from m,h:
the weighted count gains `q_m0^(-1/3)*q_h0^(-2/3)`. In particular the
sqrt(q_h0) in the Gauss bound has been included. At the other primes the
cube-free parts agree and are counted by the common core as before.
Summing the three local allocations bounds the fixed-class count by

```text
3^omega(u) * q_u^(-1/3) * M^(1/3)*H^(7/6).
```

The remaining c,n,s sums are identical. Ideal divisor bounds and counting
therefore give, for R>=1 and every epsilon>0,

```text
|J_(q_u<=R)| <<_epsilon
  Z^(7/6)*(X1*Y)^(-1/6)*X2^(-2/3) * R^(2/3+epsilon).
```

At the 0.84 scales take R=Z^(1/25). The exponent is then
`79/300+2/75=29/100`, below 8797/30000 by exactly 97/30000 before
arbitrarily small losses. This estimate again keeps all completion and
overlap terms. The same finite-sum triangle applies to the aspect contrast.

Thus the unresolved direct estimate can be restricted further to physical
cubic cores larger than Z^(1/25). At good primes the primitive cubic
conductor is rad(u), whose norm is at least sqrt(q_u); every remaining
geometric ratio class consequently has cubic Kummer inducing conductor
larger than Z^(1/50), up to the fixed bad-prime data. To use a theorem on
a further transformed row family, check any changes to this parameter
caused by overlap extractions. This elementary bound supplies no such
source-to-consumer map and no estimate for the remaining signed sum.
