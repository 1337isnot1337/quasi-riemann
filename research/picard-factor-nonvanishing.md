# Nonvanishing of the cubic Pell Picard factor

Status: a complete written proof for the exact special-function factor below,
with separately reproducible algebra and numerical checks. This is not a Lean
formalization, an independent verification of Goldfeld--Hinkle's spectral
theorems, or a quasi-Riemann bound. No priority claim is made for the classical
Legendre-function argument. The application to the Pell L-function imports
the published theorems explicitly.

## 1. Source and statement

Goldfeld and Hinkle, [*The cubic Pell equation L-function*, arXiv:2209.11874v3](https://arxiv.org/abs/2209.11874v3),
p. 2, define

```text
F(s,x) = integral_0^1 [t^(s-4/3)+t^(s-2/3)]
                         *[x*t+(t-1)^2/2]^(-s) dt, Re(s)>1/3.
```

Their Theorem 1.1 continues `F(s,(d+1)^2/(2*d))*L_d(s)` to Re(s)>1/2
with at most a simple pole at s=2/3. Theorem 1.3 permits additional poles
of L_d at zeros of F. Conjecture 1.4 says those additional poles do not
occur. The paper's d is a fixed positive cubefree rational integer greater
than one. Its coefficient is `tau(nu)*conj(tau(1+d*nu))`, as shown in
Definition 5.1 on p. 6. The conjugation is essential.

**Proposition.** For every real x>=2 and every complex s with Re(s)>1/2,
the integral F(s,x) is nonzero.

In particular the proposition applies to `(d+1)^2/(2*d)>2` for every d>1.
All powers of positive real numbers in this note use their real logarithms.

## 2. Hyperbolic representation and differential equation

Put nu=1/3 and define, for a>=1,

```text
G_s(a) = integral_0^infinity cosh(nu*u)*(a+cosh(u))^(-s) du.
```

The substitution t=exp(-u) gives `F(s,x)=2*G_s(x-1)`. The integrand
and each of its a derivatives are locally uniformly integrable for
Re(s)>nu. Thus G_s is holomorphic in s there and smooth in a>=1.

Two integrations by parts in u give

```text
(a^2-1)*G_s''(a) + (2*s+1)*a*G_s'(a)
                         + (s^2-nu^2)*G_s(a) = 0.       (1)
```

Here is an explicit justification. For f(u)=(a+cosh(u))^(-s),
the endpoint terms in
`integral cosh(nu*u)*f''(u) du = nu^2*G_s(a)` vanish: at zero both
f' and sinh(nu*u) are zero; at infinity they decay at rate
exp(-(Re(s)-nu)*u). Direct differentiation of f then gives (1).

For a=cosh(r), write g(r)=G_s(cosh(r)), set mu=s-1/2, and put

```text
y(r) = sinh(r)^mu * g(r), r>0.
```

Equation (1), first under a=cosh(r), and then under this conjugation, becomes

```text
g'' + 2*s*coth(r)*g' + (s^2-nu^2)*g = 0,
y'' + coth(r)*y' + [5/36 - mu^2/sinh(r)^2]*y = 0,
(sinh(r)*y')' + (5/36)*sinh(r)*y - mu^2*y/sinh(r) = 0.   (2)
```

These are identities, not spectral assumptions.

## 3. Boundary behavior

The value at a=1 follows from the beta integral after u=2*v:

```text
G_s(1) = 2^(s-1)*Gamma(s+1/3)*Gamma(s-1/3)/Gamma(2*s).
```

It is nonzero for Re(s)>1/2. Smoothness in a near 1 gives

```text
y(r) = r^mu * [G_s(1)+O_s(r^2)],
y'(r) = r^(mu-1) * [mu*G_s(1)+O_s(r^2)]     as r -> 0+.
```

Consequently, with Re(mu)>0, the three integrals

```text
A = integral_0^R sinh(r)*|y'(r)|^2 dr,
B = integral_0^R sinh(r)*|y(r)|^2 dr,
C = integral_0^R |y(r)|^2/sinh(r) dr
```

are finite for each R>0. Also
`sinh(r)*y'(r)*conj(y(r)) -> 0` as r->0+.
These limits justify the integrations below by first integrating on [delta,R]
and then letting delta tend to zero. In particular, one must not drop this
endpoint argument when mu is complex or close to the imaginary axis.

## 4. Energy contradiction

Suppose F(s,x)=0 for x>2, and let `R=arcosh(x-1)>0`. Then y(R)=0,
whereas y is nonzero near zero by Section 3. Multiplying (2) by conj(y)
and integrating gives

```text
A - (5/36)*B = -mu^2*C.                                (3)
```

The left side is a strictly positive real number. More precisely, completing
the square, with both endpoint terms zero, gives the exact identity

```text
A - (5/36)*B
 = integral_0^R sinh(r)*|y'(r)+y(r)/2|^2 dr
      + (1/2)*integral_0^R exp(-r)*|y(r)|^2 dr + (1/9)*B > 0. (4)
```

Since C>0, (3) forces mu^2 to be a negative real number. Write mu=p+i*q
with p>0. Its imaginary part gives 2*p*q=0, so q=0; but then mu^2=p^2>0,
a contradiction. This proves the proposition for x>2. At x=2 it follows
directly from the nonzero beta-integral value above. This completes the proof.

## 5. Classical normalization check

The integral is a classical associated Legendre function. For x>2,
`a=x-1`, `mu=s-1/2`, [DLMF 14.12.4](https://dlmf.nist.gov/14.12.E4) gives

```text
F(s,x) = sqrt(2*pi)*Gamma(s+1/3)*Gamma(s-1/3)/Gamma(s)
              *(a^2-1)^(-mu/2)*P_(-1/6)^(-mu)(a).
```

Equivalently, the hypergeometric representation is

```text
F(s,x) = 2^s*Gamma(s+1/3)*Gamma(s-1/3)/Gamma(2*s)
       *(x/2)^(1/2-s)*2F1(1/6,5/6;s+1/2;1-x/2).
```

The proof above does not assume a zero theorem for P or 2F1. The special
function formulas provide independent normalization checks and explain why
a second-order energy argument is available despite the original Appell
description.

## 6. Consequence and research boundary

Combining the proposition with **the imported Goldfeld--Hinkle Theorem 1.1**
shows that L_d is meromorphic on Re(s)>1/2 with at most a simple pole at 2/3.
Combining it with their **imported Theorem 1.3** gives their stated growth
bound away from that remaining possible pole. This removes the exceptional
Picard-zero alternative in that paper, assuming its spectral theorems.
The proof here is written and source-bound; the repo does not independently
replay those spectral theorems.

This does not yet improve the all-Dirichlet quasi-Riemann threshold. In
particular, replacing a same-character Jacobi input by
`chi_c(d*m)*conj(chi_c(1+d*m))` produces the right opposite conjugations,
but does not supply an identity with L_d. A cubic character with a numerator
having valuation two at a good prime is still nontrivial and has a nonzero
primitive Gauss sum. In contrast, Definition 3.2 of Goldfeld--Hinkle makes
tau vanish at that valuation. Their nonzero local support is squarefree
times a cube. The completion variables and finite target character also
need an exact map. Restricting physical variables to that support changes
their complete Jacobi mean and cannot be omitted from a reciprocal detector.

The unresolved task is a source-compatible identity or estimate connecting
these shifted theta series to the full trace in
[sextic-jacobi-detector.md](sextic-jacobi-detector.md), or to the complete
signed correlation in
[cubic-signed-correlation-contract.md](cubic-signed-correlation-contract.md).
Neither follows from the proposition alone.

## 7. Reproduce

```sh
make verify
python3 scripts/verify_picard_factor.py --numerical
make sources
```

The checker certifies the differentiated integrand identity, both changes
of the differential equation, the square completion, and the complex-parameter
contradiction algebra. The optional numerical checks compare quadrature,
Legendre, and hypergeometric evaluations at specified points. Neither the
finite algebra nor the numerical evaluations replace the analytic boundary
and positivity arguments in Sections 2--4.

The exact arXiv v3 PDF is hash-pinned in `sources.lock.json`; its original
pages 2, 5 and 6 were rendered and checked for the definition of F, the
valuation support, and the conjugation, respectively. The later journal
version is [Acta Arithmetica 210 (2023), 235--277](https://doi.org/10.4064/aa220918-18-8).
This note uses the arXiv v3 source, not a claimed byte-identical journal copy.
