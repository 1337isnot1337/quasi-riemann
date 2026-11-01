# The binary cubic kernel and its shared label

Replacing the probe can change the character family, rather than retune the
existing sextic moment. This note audits one candidate: two cubic Poisson
transforms applied to the completed cubic-theta coefficient. The good-prime
Euler calculation is exact and retains all cube-completion valuations.
The global Poisson identity is derived in
[shared-label-cubic-identity.md](shared-label-cubic-identity.md); a direct bound
and the continued signed row estimate are not proved. The unmarked
version loses principal-row isolation; a shared cubic label below restores
its good-prime selector. No zero-free bound follows from this note.

## The phase identity is prior work

OpenAI's [September 30 paper at commit fd4aeeb](https://raw.githubusercontent.com/openai/math/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)
has `gamma_2(c)^3=mu(c) alpha(c)` for
squarefree good `c`, with `alpha(c)=c/|c|`. The two conjugate cubic duals are
explicitly suggested in the scope paragraph of span_of_dilates,
[Structural ceilings, version 5](https://rstation.ai/problems/riemann_hypothesis/papers/40).
The downloaded Markdown has SHA-256
`3a6ba61849965c81b3c6e24de8d229eea7c45c3155d74eb27bff9c36a29692a9`.
We claim no novelty for that phase configuration. Here we calculate what its
completed good-prime kernel would be and identify a missing selector.
The pinned TeX SHA-256 is
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`;
its complete cube source is equation `eq:unmarked-central-completion`.

The schematic source before finite ray corrections is

```
sum_(c squarefree,n) gamma_2(c) conjugate(alpha(c*n^3)) eta(c*n^3)
    / [sqrt(N(c))*N(n)] * V(N(c*n^3)/Z)
    * product_(i=1,2) [sum_m chi_(c*n^3)(m)^2 W_i(N(m)/X_i)].
```

All ideal variables avoid the fixed bad set. A literal global definition must
also fix the unit and ray sectors and the two self-dual Fourier normalizations.
This display does not silently identify that finite local vector with the
existing sextic probe's vector.

Two cubic Poisson transforms supply two more `gamma_2(c)` factors. Their
product with the source gives `mu(c) alpha(c)`, canceled by its angular weight.
The dual character depends on `h1*h2` through a cubic symbol. Group that product
as `u*a^3`, with `u` cube-free. The expected reciprocal is then a cubic-row
`1/L(x,eta*rho_u)`. This changes the family by changing the probe; no cubic
estimate is being applied to the old sextic row character.

## Exact good-prime calculation

Fix a good prime with `Q=N(p)`. Let `e=v_p(c)` be zero or one,
`ell=v_p(n)`, `a=v_p(h1)`, and `b=v_p(h2)`. Write

```
A=Q^(-t1), B=Q^(-t2), x=3/2+v-t1-t2,
D=eta(p)*rho_u(p)*Q^(-x),
R=eta(p)^3*conjugate(alpha(p))^3*Q^(-1-3v).
```

Here `v` is the Mellin variable for the completed source weight, and `t_i`
are for the two Fourier profiles. `D=0` at a prime of `u`. The phases defining
`rho_u` require the fixed reciprocity packet in a global statement.

For `e=1`, each lifted nonprincipal Gauss sum forces its frequency valuation
to equal `3ell`. Thus `a=b=3ell`, and the prime contributes `-D*R^ell`
only to `j=v_p(u)=0`. This includes the overlap `p|c` and `p|n`.

For `e=0, ell>=1`, dividing the principal Gauss sum modulo `p^(3ell)` by
that modulus gives exactly

```
r_ell(a) = 1_(a>=3ell) - Q^(-1) 1_(a>=3ell-1).
```

Both boundary terms matter, including their negative signs. Define

```
F0=(1+A*B^2+A^2*B)/[(1-A^3)(1-B^3)],
F1=(A+B+A^2*B^2)/[(1-A^3)(1-B^3)],
F2=(A^2+A*B+B^2)/[(1-A^3)(1-B^3)].
```

These are the generating series with `a+b=j mod 3`. For `j=0,1,2` put
`r_j=(j+1) mod 3` and

```
Gj = (1-Q^(-1))^2 Fj
   - Q^(-1)(1-Q^(-1)) [A^(-1)B^r_j/(1-B^3)
                       + A^r_j B^(-1)/(1-A^3)]
   + 1_(j=1) Q^(-2) A^(-1)B^(-1).
```

To prove this for every `ell`, split the frequency valuations into four
regions: both at least `3ell`, only the first equal to `3ell-1`, only the
second equal to `3ell-1`, and both equal to that boundary. The last region has
sum `1 mod 3`; this explains the `j=1` term. The generating function in each
case is `(A^3 B^3)^ell` times the corresponding displayed expression.
Multiplication by the source and Mellin powers makes each layer geometric
with ratio `R`. Summing all `ell` gives the complete good-prime factor

```
Pj = Fj + [R*Gj - 1_(j=0) D]/(1-R).
```

The checker verifies the rational formulas, the exact geometric tail, and
8,664 independent rational valuation cases. These finite cases supplement
the four-region all-size proof; they are not its replacement.

## The principal candidate survives completion locally

At `t1=t2=1/3`, put `q=Q^(-1)`. The expressions simplify to

```
G0=1, G1=2*q^(1/3), G2=q^(2/3),
F0=(1+2q)/(1-q)^2,
F1=q^(1/3)*(2+q)/(1-q)^2,
F2=q^(2/3)*3/(1-q)^2.
```

In particular, the principal factor is

```
P0 = [F0-D+R(1-F0)]/(1-R).
```

The scalar completion factor is the angular Hecke function
`L^S(1+3v,eta^3*conjugate(alpha)^3)`, not an ordinary factor with no
angular character. At the candidate residue, `1+3v=3x-3/2`.
For `Re(x)>5/6` this scalar Euler product is absolutely convergent and
nonzero. Thus the completion does not automatically cancel the candidate
target reciprocal in that range.

For `Re(x)>1/2`, both `|D|<1` and `|R|<1`. Since `F0>1`, the triangle
inequality proves `F0-D-R(F0-1)` is nonzero. For the ramified factors the
same argument uses

```
F1/q^(1/3) > 2,       F2/q^(2/3) > 1.
```

After the common scalar extractions, the good-prime correction at the
critical point is normally convergent: the `j=0` local defect is
`O(q^2 + Dq + Rq)`. These decay exponents exceed one for `Re(x)>1/2`.
Finite `j=1,2` factors have nonzero corrections of divisor size. These facts
concern the local kernel, without claiming the global row sum converges.

## The new obstruction: shared poles

Away from the finitely many primes of `u`, the fixed-row kernel has the
same four scalar factors,

```
zeta^S(3t1), zeta^S(3t2),
zeta^S(t1+2t2), zeta^S(2t1+t2).
```

Their common intersection is `t1=t2=1/3`. The nonzero ramified factors above
show that the good-prime calculation supplies these poles to other fixed
cubic rows as well. It supplies no pole specific to `u=1`. A global fixed
ray projection could alter the scalar factors and must be checked; the
good-prime formula by itself is not a principal-row isolation argument.

The candidate scalar power is

```
Z^(x-5/6) * (X1*X2)^(2/3),
```

with a possible polynomial of degree two in the logarithms from four poles
and two Mellin variables. This is a signal candidate before isolation, not
a proved principal term for the entire detector.

The existing probe's ordinary numerator supplied a principal-row-specific
pole. Removing it has removed that selector. Before seeking a new bound,
the binary probe needs a different projection that preserves the reciprocal
of the target and suppresses the other fixed cubic rows. The direct estimate
also changes: its completed theta row is indexed by `(m1*m2)^2`. An estimate
for all natural rows through norm `(X1*X2)^2` cannot be renamed as a mean
through norm `X1*X2`.

## A shared cubic label supplies a candidate selector

Use a squarefree label `s` on both physical averages, with the common factor

```
gamma_4(s)^(-2) * chi_s(m1*m2)^4.
```

Scale each physical profile by `N(s) X_i`, normalize each average by
`sqrt(N(s) X_i)`, and average the labels with `Y^(-1) W(N(s)/Y)`.
At primes not dividing the source, Poisson produces the label character
`chi_s(h1*h2)^2`; its two Gauss phases cancel against the compensator.
Consequently the squarefree label series gives

```
L^S(w,rho_u)/L^S(2w,rho_u^2).
```

This uses the same cubic row `u` as the inverse denominator. Its pole at
`w=1` can distinguish the principal cubic row. The denominator at that
residue is absolutely convergent and nonzero.

The overlap of `c`, `n`, and `s` cannot be deleted. It fortunately has an
exact phase cancellation. For two different primes let their source
valuations be `e,f`, label valuations `k,l`, and cube-completion valuations
`a,b`. In cubic residue-symbol exponents, the source contributes `2ef`,
the compensator `4kl`, and the two Fourier transforms contribute

```
2 [(e-k)(f+l+3b) + (f-l)(e+k+3a)].
```

Their sum is exactly

```
6 [ef+(e-k)b+(f-l)a].
```

It is divisible by three for all valuations, so every pair phase is one
by cubic reciprocity. At a common source/label prime the two local
characters cancel on units; their literal nonunit zeros remain, giving a
Ramanujan transform rather than an unramified Gauss sum. Its scalar phase
is `gamma_2(p)*gamma_4(p)^(-2)=-alpha(p)`, the required Möbius sign.

Let `W=rho_u(p)Q^(-w)` with its original zero extension, and put
`T=eta(p)Q^(-x-w)` even at a prime dividing `u`. The complete marked kernel is

```
Mj = Fj + [R*Gj + 1_(j=0)(W-D)
           - T Q^2 A^2 B^2 G_(j-1 mod 3)]/(1-R).
```

For the common source/label prime the modulus is `p^(3ell+2)`. Its two
normalized Ramanujan factors have the boundary at `3ell+1`. Their
generating series is `(A^3 B^3)^ell A^2 B^2 G_(j-1 mod 3)`, proving the
last term for every `ell`. Another 8,664 rational valuation cases replay
these overlapping branches independently of the closed formula.

At `t1=t2=1/3` the principal local numerator simplifies exactly to

```
(1-R)M0 = (1-D)(1+W) + (1-R)(F0-1).
```

Thus the inverse factor `1-D` and squarefree ordinary factor `1+W` survive
with a normally convergent correction after extracting the four frequency
scalar factors. At `w=1` on the principal row, `W=q=Q^(-1)` is positive.
The right side is a positive linear combination of `1-D` and `1-R`.
Its real part is strictly positive when `Re(x)>1/2`, so the good-prime
principal coefficient is nonzero. As before, the remaining angular scalar
is assured nonzero by absolute Euler convergence for `Re(x)>5/6`.

This gives a changed high-side design: a cubic inverse and a cubic ordinary
selector on the same row, with the completed source retained. A global
identity, including its unit count, self-dual normalization and factors at
excluded primes, is written in the linked note. Its local checks do not
independently verify the analytic derivation or estimate its continued row sum.

The immediate direct-side target comes from transforming only the second
average. On the coprime source/label sector its source coefficient becomes

```
gamma_2(c)^2*conjugate(alpha(c)) = mu(c)*gamma_4(c),
```

and the label coefficient becomes `gamma_2(s)`. Cubic Möbius–Gauss means
are therefore relevant to this new probe. A source-to-consumer proof must
still retain the fixed target character, the moving cubic numerator
`m1*h2^2`, the common label, all overlap divisors and the separate profiles.
A natural-row theorem with no such twist is not the required bound.

## Zero frequencies do not require a quadratic character

The old probe's auxiliary primitive character has order divisible by two
at some bad primes. Copying it would insert nonprincipal fixed twists in
the four cubic scalar factors and could remove the candidate poles too.
There is a local analytic alternative worth retaining: choose a radial
Schwartz profile of integral zero. In standard Euclidean normalization,

```
W(r)=exp(-pi*r)-2 exp(-2*pi*r),
Fourier(W)(s)=exp(-pi*s)-exp(-pi*s/2).
```

The Fourier value at zero vanishes, whereas its Mellin value at `1/3` is
`Gamma(1/3)*pi^(-1/3)*(1-2^(1/3))`, which is nonzero. This kills zero
frequencies without imposing an order-two multiplicative twist. It does
not replace the shared-label calculation. Unit sectors, bad-prime
corrections, and the exact self-dual scaling remain part of the global
construction to verify.
