# A polynomial-phase representation of the squarefree Jacobi trace

Status: exact finite identities, an explicit extraction of every frequency
overlap on squarefree moduli, and an absolute-line Mellin identity. No new
trace bound or zero-free threshold is proved. Non-squarefree moduli and the
full finite-mean subtraction remain in the original open problem.

This uses the classical Duke--Iwaniec identity, not a new exponential-sum
identity. The primary comparison source is Friedberg--Offen,
[*On the cubic Shimura lift to PGL(3): The fundamental lemma*](https://doi.org/10.4171/JEMS/1503),
equation (7.4), printed p. 1726. The paper proves a local fundamental lemma;
it does not provide the global analytic estimate needed here. Its exact PDF
is pinned in `sources.lock.json`.

## 1. Eliminate the modular inverse at unit frequencies

Use the notation of [sextic-jacobi-detector.md](sextic-jacobi-detector.md).
For a squarefree good c put kappa_c=chi_c^2, a cubic symbol, and define

```text
A_c(h) = sum_(t mod c) e(h*(3*t-t^3)/(2*c)),
g_4(h;c) = sum_(z mod c) chi_c(z)^4*e(h*z/c),
gamma_4(h;c) = g_4(h;c)/sqrt(Nc).
```

Inverses of 2 in this formula are taken in O/(c). These formulas are
independent of the chosen residue representatives. For (h,c)=1,

```text
S_(kappa_c)(1,h^2/4;c) = kappa_c(4*h)*A_c(h).           (1)
```

At a prime, substitute `a=-4/(27*h^2)` in Duke--Iwaniec:

```text
sum_x e((x+a*x^3)/c)
 = kappa_c(a)^(-1)*sum_(u!=0) kappa_c(u)*e((u-1/(27*a*u))/c).
```

Then x=3*h*t/2 gives the polynomial phase in A, and
`kappa_c(a)=kappa_c(4*h)` since cubes and -1 have trivial cubic symbol.
This proves (1). For a squarefree composite, use CRT. At a factor p, the
additive character has the cofactor inverse; normalizing the first
Kloosterman argument contributes kappa_p(c/p), which cancels the cofactor
in kappa_p(4*h/(c/p)). Thus no extra CRT multiplier remains in (1).

The existing sextic Kummer identity therefore gives, at unit frequencies,

```text
bar(alpha(c))*epsilon(c)*J6_c(h)
 = mu(c)*epsilon(c)^2*gamma_4(h;c)*A_c(h).              (2)
```

Here epsilon(c)=chi_c(4), so kappa_c(4)=epsilon(c)^2. The Gauss sum now
has numerator h. Treating it as gamma_4(1;c) would discard a cubic symbol.

## 2. Extract all frequency overlaps

For any h, including nonunits, let g=(h,c), d=c/g and h'=h/g. Choose
primary generators so c=g*d. Since c is squarefree, (g,d)=1 and (h',d)=1.
The exact identity is

```text
g_4(1;c)*S_(kappa_c)(1,h^2/4;c)
 = Ng*epsilon(d)^2*g_4(h';d)*A_d(h').                  (3)
```

To prove it, factor both sums by CRT. The g component of S has second
argument zero and is g_2(1;g), up to its cofactor character. Its product
with g_4(1;g) is Ng. The cofactor characters cancel against those in the
d component of g_4 and S. Apply (1) at d and use
`g_4(h';d)=kappa_d(h')*g_4(1;d)`. This proof uses neither a replacement
of a modular inverse by a complex reciprocal nor an omission of character
zeros. At h=0, take g=c,d=1; (3) reduces to g_4(1;c)*g_2(1;c)=Nc.

Consequently the full squarefree trace, with its original phase, satisfies

```text
bar(alpha(c))*epsilon(c)*J6_c(h)
 = mu(g)*mu(d)*sqrt(Ng)*epsilon(d)^2
                         *gamma_4(h';d)*A_d(h').      (4)
```

The equality includes all frequency gcds. The split-prime and composite
checks in the accompanying script are exact cyclotomic equalities; they
are finite checks in addition to the CRT proof.

## 3. The squarefree high sum and an explicit reciprocal factor

Let H6_sf be the original uncentered H6 with c restricted to squarefree
good sources. Substituting (4) and using
`Nh/Nc=Nh'/Nd` gives the exact convergent identity, for X,Z>0,

```text
H6_sf(X,Z) = sqrt(X)*sum_(d sf) mu(d)*eta(d)*epsilon(d)^2/Nd^(3/2)
 *sum_(h'!=0,(h',d)=1) gamma_4(h';d)*A_d(h')*U(X*Nh'/Nd)
 *sum_(g sf,(g,d)=1) mu(g)*eta(g)/Ng*V(Ng*Nd/Z).        (5)
```

The Gaussian frequency profile is independent of g after extraction.
Every original pair (c,h) occurs exactly once. A subscript 1 means the
trivial modulus with A_1=gamma_4(*;1)=1.

With X fixed, Mellin inversion of V on Re(v)=2 factors the g sum:

```text
sum_(g sf,(g,d)=1) mu(g)*eta(g)/Ng^(1+v)
 = [1/L^S(1+v,eta)]*prod_(p|d) [1-eta(p)*Np^(-1-v)]^(-1).
```

Thus

```text
H6_sf(X,Z) = sqrt(X)/(2*pi*i)*integral_(2)
                exp(v^2)*Z^v*E_eta(v;X)/L^S(1+v,eta) dv,

E_eta(v;X) = sum_(d sf) mu(d)*eta(d)*epsilon(d)^2/Nd^(3/2+v)
 *prod_(p|d) [1-eta(p)*Np^(-1-v)]^(-1)
 *sum_(h!=0,(h,d)=1) gamma_4(h;d)*A_d(h)*U(X*Nh/Nd).   (6)
```

These interchanges are justified on the stated line: |A_d|<=Nd,
|gamma_4(h;d)|=1 on unit h, and the Gaussian h sum is O_X(Nd).
The d sum is therefore absolutely convergent for Re(v)>3/2. Gaussian
Mellin decay permits the vertical integral. Formula (6) does not assert
continuation of E_eta across that domain.

The corresponding squarefree zero frequency has the particularly simple
coefficient `mu(c)*eta(c)/Nc`. Its Mellin factor is exactly
`sqrt(X)*U(0)/L^S(1+v,eta)`. Accordingly the physical squarefree probe has
the same integral as (6) with E_eta replaced by U(0)+E_eta. This displays
the reciprocal factor explicitly. A polynomial-phase representation alone
does not remove its possible poles.

## 4. What remains to reach the main target

The original direct-side rapid decay uses all sources, including every
prime power. Restricting to the squarefree source in (5) changes that
estimate. The e=2,4 branches of the complete sextic Jacobi trace have cubic
input and sextic Kloosterman output, and the e=3,0 branches also remain.
Friedberg--Offen's higher-conductor extension for cubic Kloosterman
integrals does not automatically identify these different local branches.

Likewise (5) is for the uncentered sum. The complete finite-frequency mean
removed in OPEN6o is over all moduli. Its rapid-decay proof must not be
applied to a squarefree restriction without a new argument.

The next analytic question is whether an actual global cubic transfer or
coefficient-sensitive Airy/Gauss estimate controls (5), together with those
other local branches, in the required coupled X,Z range. A local
fundamental lemma supplies no such global bound on its own. This is an
explicit alternate representation of the open trace, not a new
conditional numerical bound.

## 5. Reproduce

`python3 scripts/verify_airy_trace.py` checks (1) for both cubic embeddings,
three primitive additive characters at five split primes, and (3) for
prime and composite moduli with all sampled frequency gcds. All arithmetic
is exact in cyclotomic rings. The composite samples use product residue
fields; the identities hold for arbitrary primitive additive characters,
so no special complex embedding is silently imposed. The proof and the
absolute-line argument are written, not Lean formalized.
