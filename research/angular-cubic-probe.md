# Angular orders for the shared-label cubic probe

Status: exact angular bookkeeping for a candidate modification. No global
angular Poisson identity, principal asymptotic, full low estimate or improved
zero-free bound is proved here. The radial shared-label construction is the
separate checkpoint `297a7ef` referenced in `binary-cubic-low-budget.md`.

The relevant external input is bramble_trace's
[Paper 5 v3, Theorem 1](https://rstation.ai/problems/riemann_hypothesis/papers/5/v3).
It bounds cubic-character means with prescribed coefficient
`D_j(c)=mu(c)*alpha(c)^j*gamma_2(c)*nu(c)` for j=2 or -2, common annular tests,
all natural element rows and a puncture fixed during the mean. Its normalized
bound is `N+B^3/N+N^(2/3)B^(1/2)` up to subpowers. The theorem is not an
arbitrary-coefficient result, and has not been independently verified here.

## Why the radial coefficient does not match

On the coprime completion-free branch, one Poisson transformation of the radial
binary probe leaves c coefficient `mu(c)*conjugate(gamma_2(c))`. Conjugating the
whole c polynomial gives `mu(c)*gamma_2(c)` with the conjugate cubic character.
That is D_0, not either admitted D_j. A fixed finite ray phase cannot change its
angular order. The published angular theorem cannot simply replace the generic
cubic comparator in that radial calculation.

## A compatible angular choice

Replace the source angular factor by alpha(A)^ell and take physical profiles
of the form `alpha(m)^k_i W_i(Nm)` in the two averages. For the complex-bilinear
self-dual Fourier pairing, an angular order k transforms to order -k. At dual
frequency h/(A*s), this supplies

```text
alpha(h)^(-k) * alpha(A*s)^k.
```

The two physical averages use the same cubic character. Their nonzero unit
conditions require both k_i even and k1=k2 mod 6. The source and two good-prime
Gauss roots give `gamma_2(c)^3=mu(c)*alpha(c)`. Preserving the finite-order target
therefore requires

```text
ell+k1+k2=-1.
```

Give the label compensator the extra factor `alpha(s)^(-k1-k2)` to remove its
net angle. After transforming only the second average, the c coefficient is

```text
mu(c)*alpha(c)^(-k1)*conjugate(gamma_2(c)),
```

up to the fixed finite ray factors. Conjugating the whole c polynomial gives
D_(k1) with a fourth-power cubic character, the orientation in Theorem 1.
Thus k1=2 or -2 matches that input.

The concrete choice

```text
(k1,k2,ell)=(2,-4,1),
label compensator = alpha(s)^2 * gamma_4(s)^(-2)
```

satisfies the unit congruence and target phase condition. After one transform,
the label coefficient is `alpha(s)^(-2)*gamma_2(s)`; it is not D_j because it
has no Möbius factor. Retain that distinction in a Cauchy argument. The paper's
row-scale theorem for that coefficient is a sextic-character mean. Our remaining
label character is cubic; replacing its row m by m^4 would change the row norm
range and cannot be done at no cost.

## The frequency poles change

In the good-prime binary kernel replace its frequency variables by

```text
A=alpha(p)^(-2)*Q^(-t1), B=alpha(p)^4*Q^(-t2).
```

The four radial zeta factors then have angular orders

```text
3t1: -6,   3t2: 12,   t1+2t2: 6,   2t1+t2: 0.
```

Only the last retains the ordinary zeta pole. The source completion angle
also changes; substituting A and B alone is not a derivation of the full
angular prime kernel. Two independent untwisted
frequency factors would force k1=k2=0, since any two of their four angular
linear forms are independent. The covered nonzero angular mode therefore
cannot preserve the old four-pole signal calculation.

On the candidate pole `2t1+t2=1`, using `x=3/2+v-t1-t2`, the scale factor is

```text
Z^(x-1/2)*sqrt(X1/X2) * [X2^2/(Z*X1)]^t1.
```

The coupled scales X2^2=Z*X1 remove that remaining free Mellin power. A Mellin
integral still remains; this identity does not prove that its coefficient is
nonzero. The full unit/ray packet, completion variables, overlap masks,
ordinary selector, and every contour error must be rederived for this angular
probe. In particular, the second dual-frequency sum cannot be dropped or
charged as a constant when its range is a positive power of Z.

The exact order, rank and scale calculations are included in
`scripts/verify_mellin_annihilator.py` and its receipt. They do not certify the
unproved global or analytic steps above.
