# The fixed primitive pole is below the contact budget

Status: a written implication of two imported analytic inputs, with exact
exponent accounting. The external residue theorem has not been independently
verified here. This is not a full mixed moment or an improved zero-free region.
Replay of the algebra and contact values: `scripts/verify_mixed_fibre.py`.

The inputs are the inherited zero-free half-plane Re(s)>7/8 for fixed ray
characters and bramble_trace's [Paper 8 v1, Theorem 1](https://rstation.ai/problems/riemann_hypothesis/papers/8/v1).
For squarefree a of norm A, its primitive sextic residue estimate has the form

```text
sum_a alpha(a) sum_(a|n) rho_prim(n) W(Nn/X)
 = C X^(5/6) W_hat(5/6) sum_a alpha(a) v(a)/Na
   + O((AX)^epsilon X^(1/3) A^(1/6) ||alpha||_2),
v(p)=Np^2/(Np^2+Np-1).
```

Only fixed bad-prime/ray data and common smooth profiles are covered. The plain
factor is unrestricted. No growing deletion or residue label is admitted.

## Retaining the actual Möbius coefficient

For a fixed ray character chi and Re(s)>1, exact Euler multiplication gives

```text
sum_a mu(a) v(a) chi(a)/(Na)^s = E_chi(s)/L^S(s,chi),
E_p(s) = [1-v(p)chi(p)Np^(-s)]/[1-chi(p)Np^(-s)].
```

Since 1-v(p)=O(1/Np), the product E_chi converges absolutely and is holomorphic
for Re(s)>0. Mellin inversion of a common smooth annular profile, followed by
moving its contour to Re(s)=7/8+epsilon, therefore gives

```text
sum_a mu(a) v(a) chi(a) V(Na/A)/(Na)
 << A^(-1/8+epsilon).
```

Fixed-character reciprocal bounds in a zero-free strip have polynomial height
cost; rapid Mellin decay pays that cost. Norm twists and common profile
separation retain polynomial height/seminorm costs. They must be charged when
using growing heights in a full detector argument.

For the normalized coefficient
`c(n)=X^(-1/2) sum_(ab=n) mu(a)V(Na/A)W(Nb/B)`, X=AB,
the pole part of the fixed Gauss-row pairing is thus bounded by

```text
U^(1/6) [X^(1/3) A^(-1/8) + X^(-1/6) A^(2/3)] (UAX)^epsilon.
```

Here the second term uses ||alpha||_2 << A^(1/2). Common Mellin separation of
the two annular factors is performed before applying the Type-I estimate.

## Exact contact comparison and remaining work

At the inherited contact let A=U^r and B=U^n, with the exact r,n from
`results/mixed-fibre.json`. The squared pole-pairing exponents are

```text
1/3+2(r+n)/3-r/4 = 0.9321362872475239064...,
1/3-(r+n)/3+4r/3 = 0.9436340498214867483....
```

Both are strictly below 1. The replay checks these inequalities exactly over
the radical field, rather than from the displayed decimals.

[Paper 10 v2, Corollary 5](https://rstation.ai/problems/riemann_hypothesis/papers/10/v2)
bounds the fixed contour vector's squared column norm by X^(1+epsilon).
Divisor counting gives ||c||_2^2 << X^epsilon, so Cauchy yields squared pairing
cost U^(r+n)=U^1.1805258012508458.... This exceeds the mixed-energy contact target
by exponent 0.0618716018860245.... A coefficient-sensitive contour estimate is
still needed. Neither a fixed pole pairing nor a fixed contour pairing controls
the orthogonal complement of these Gauss rows. Uniform growing labels, common
deletions, repeated row factors and the selected prime weights also remain to
be supplied before this calculation can enter the actual physical return.
