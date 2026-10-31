# A precise signed-correlation gap after the newer Gauss norm

Status: an exact exponent-model calculation for a specified Cauchy route.
It grants several unavailable uniformities. It is neither a lower bound on
the actual probe nor a zero-free theorem. The imported norm theorem has not
been independently verified here.

## The newer coefficient-specific input

bramble_trace's [Paper 77 v1, Theorem 2](https://rstation.ai/problems/riemann_hypothesis/papers/77/v1)
bounds the actual normalized cubic Möbius–Gauss norm, on natural rows of
length A and columns of length Y, by `A+Y^R(log_Y A)` up to subpowers, where

```text
R(M) = 7/2-M/2-sqrt(6-3M),       1 <= M <= 29/27,
       2M/5+13/15,              29/27 <= M <= 2.
```

For A>=Y^2 it gives the row-volume bound. The result retains its stated
external 7/8 zero-free hypothesis. It includes common polynomially growing
deletions, but does not assert an arbitrary fixed target twist or a growing
exterior cubic numerator. Its diagonal asymptotic starts strictly above
A=Y^(13/9). None of those restrictions is removed here.

[Paper 70 v1, Theorem 1](https://rstation.ai/problems/riemann_hypothesis/papers/70/v1)
gives a stretched-exponential improvement to the power `(AY)^(2/3)` in the
shorter natural-row range. That gain changes no fixed exponent in the
following model. For very short rows the generic bound is at least that
same mixed power.

## The optimistic separate-mean model

Take the radial shared-label cubic probe and write

```text
X1=Z^a, X2=Z^a2, Y=Z^b, M=a+b, 0<a2<=1.
```

Grant the newer norm for every target and second-frequency twist that the
partial transform needs. Also grant free completion and overlap
reconstruction, and common profile separation. These are optimistic grants,
not consequences of the cited theorem. Grant the stated natural-row
ordinary-Gauss comparator Fs as well; an arbitrary-coefficient natural-row
sieve can have an additional repeated-cube cost. Retain the actual count
Z^(1-a2) of second dual frequencies. Applying separate Cauchy estimates to
the remaining physical variable gives low exponent

```text
L = (a2-a-1)/2 - b + (1-a2) + (Fc+Fs)/2,
Fc = max(M,R(M))                         when 1<=M<=2,
Fs = max(M,b,2(M+b)/3).
```

Here Fc is for the long prescribed Möbius–Gauss column and Fs for the
short ordinary Gauss column, using a generic natural cubic comparator for
the latter. The principal power is
`theta-5/6+(a+a2)/6`. Thus the separate-mean route requires theta above

```text
T = 4/3 - 2(a+a2)/3 - b + (Fc+Fs)/2.
```

Since `Fs>=2(M+b)/3`, substitution of b=M-a proves

```text
T >= 2/3-M/3+Fc/2 + (2/3)(1-a2).
```

For 1<=M<=29/27 the curved R is at least its later linear branch. The
exact certificate is

```text
A0=79/30-9M/10 >= 5/3 > 0,
A0^2-(6-3M) = (27M-29)^2/900 >= 0.
```

Consequently Fc>=max(M,2M/5+13/15) throughout 1<=M<=2. The branches meet
at M=13/9. Below that point the last lower bound exceeds 49/54 by
`2(13/9-M)/15`; above it the row-volume branch exceeds 49/54 by
`(M-13/9)/6`. For M<1 the available mixed-power comparison gives the
stronger lower bound 1; for M>=2 the row-volume branch is also larger.

The infimum is therefore exactly

```text
theta_Cauchy = 49/54 = 0.9074074074...,
a=b=13/18, a2 -> 1.
```

This is the best exponent furnished by the specified optimistic model.
It requires a further signed saving of at least 101/2700 to reach 0.87,
or 91/1350 to reach 0.84. The limiting geometry is only a model witness;
no high-side reconstruction is asserted there. Fixed finite aspect
differences do not change this triangle/Cauchy exponent.

At the separate 0.84 high checkpoint's actual scales a=b=73/100,
a2=99/100, the optimistic row-volume comparisons give theta=11/12.
The missing signed saving is 23/300 before the 1/10000 reserve, or
2303/30000 with it. This now has a precise coefficient-specific norm
comparison, but its twist hypotheses remain unproved and the comparison
itself is still insufficient. A joint signed estimate, possibly exploiting
the complete [aspect contrast](cubic-aspect-contrast.md), must do additional
arithmetic work.

`scripts/verify_cubic_signed_budget.py` checks the rational identities,
the curved-envelope certificate and the attaining limiting point. It does
not verify either imported analytic theorem or the full probe estimate.
