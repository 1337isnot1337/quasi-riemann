# A Jacobi detector with an ordinary source

Status: written exact identities and a direct-side rapid-decay proof for a
changed operator. The complete nonzero-frequency estimate needed to improve
the quasi-Riemann bound is open. The arithmetic certificate checks fifteen
prime-power examples, the all-size Euler formula and the conditional exponent
arithmetic. None of the analytic arguments is Lean formalized.

## 1. Change the operator

The cubic Gauss identity in OpenAI's
[September 30 source](https://raw.githubusercontent.com/openai/math/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)
is gamma_2(p)^3=-alpha(p) for good primary primes. The elementary
Gauss/Jacobi identity gives

```text
sum_(x mod p) chi_p(x*(x-1))^2 = -p.
```

Indeed for the cubic character theta=chi_p^2,
J(theta,theta)=g(theta)^2/g(theta^2)
=sqrt(Q)*gamma_2(p)^3. Replacing 1-x by x-1 changes nothing because
theta(-1)=1. The Gauss/Jacobi identity follows by grouping g(theta)^2
according to the nonzero sum of its two variables; the zero-sum contribution
vanishes. These identities are prior arithmetic, not a new claim about Gauss
sums. The pinned TeX hash is
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.
The final scope paragraph of span_of_dilates,
[Structural ceilings v5](https://rstation.ai/problems/riemann_hypothesis/papers/40/v5),
already emphasizes that every such Jacobi sum carries a Mobius sign. The
sign is not the new ingredient. This note tests a particular all-ideal
operator, its direct bound and its complete Fourier remainder.

Work in O=Z[omega], with the same primary generators, alpha, self-dual pairing
and finite bad set S containing the primes above 6. The fixed target eta is
any finite-order Hecke character with conductor supported in S. All source
ideals c below are good; importantly, they are **not** restricted to squarefree
ideals and have no Gauss coefficient. Take

```text
V(r)=(4*pi)^(-1/2)*exp(-(log r)^2/4),
W(r)=exp(-pi*r), U(r)=(2/sqrt(3))*exp(-4*pi*r/3),

I_eta(X,Z)=X^(-1/2)*sum_c eta(c)*bar(alpha(c))/sqrt(Nc)*V(Nc/Z)
                *sum_(m in O) chi_c(m*(m-1))^2*W(Nm/X).
```

The sextic character chi_c is multiplied in the denominator, then squared;
all its powers retain the nonunit zeros. At c=1 the character is one, also
at zero. At every other c it vanishes at m=0,1. The lognormal test ensures
absolute convergence of the source sum and of all rearrangements here.

## 2. The direct physical side is small when X^2 is shorter than Z

For fixed nonzero r=m*(m-1), cubic reciprocity makes

```text
a_r(c)=eta(c)*chi_c(r)^2*1_(c primary and good)
```

a bounded periodic function of the element c. A period ideal M_r can be
chosen with N(M_r)<=C_(eta,S)*N(rad(r))<=C_(eta,S)*Nr. The fixed factors at
3 include the finitely many supplementary and ramified Kummer classes; the
literal zeros at all primes of r stay in this period. No cancellation in
eta or a zero-free hypothesis is used.

Put f(z)=z^(-1)*V(Nz), with value zero at z=0. This is a Schwartz function:
the lognormal profile and all its derivatives vanish faster than every
power both at zero and infinity. Its angular order is -1, so its integral,
and hence its Fourier transform at zero, is zero. The c summand is
Z^(-1/2)*f(c/sqrt(Z)). Expanding a_r on its finite additive Fourier group
gives coefficients of absolute value at most one. Lattice Poisson therefore
gives, for every A>1,

```text
|sum_c a_r(c)*bar(alpha(c))/sqrt(Nc)*V(Nc/Z)|
 <= C_A*sqrt(Z)*sum_(h in O, h!=0)
           |sqrt(Z/N(M_r))*h|^(-2*A)
 <<_(A,eta,S) sqrt(Z)*(Nr/Z)^A.
```

Here the displayed sum stands for the resulting bound on the nonzero dual
lattice: the Schwartz estimate supplies the negative power and the norm
sum converges for A>1. The zero dual term is absent even if a_r has a
nonzero mean. The period ideal is principal, so its dual is a rotated copy
of the lattice at scale N(M_r)^(-1/2); rotation does not affect this estimate.

Since Nr<=C*(1+Nm)^2 and
sum_m exp(-pi*Nm/X)*(1+Nm)^(2*A)<<_A X^(2*A+1) for X>=1,

```text
I_eta(X,Z) <<_(A,eta,S) sqrt(X*Z)*(X^2/Z)^A
                         +X^(-1/2)*|V(1/Z)|.                 (D)
```

The last term accounts for m=0,1, where only c=1 survives. Thus for every
fixed 0<a<1/2, I_eta(Z^a,Z) decreases faster than every power of Z. This is
a written proof using ordinary lattice Poisson, not a numerical observation.

## 3. The zero frequency contains the target reciprocal

Define the complete polynomial-character trace

```text
J_c(h)=sum_(x mod c) chi_c(x*(x-1))^2*e(h*x/c),
e(z)=exp(2*pi*i*Tr(z/sqrt(-3))).
```

Poisson in m gives I_eta=I_0+H_eta, where

```text
I_0=sqrt(X)*U(0)*sum_c eta(c)*bar(alpha(c))*J_c(0)
                              /Nc^(3/2)*V(Nc/Z),
H_eta=sqrt(X)*sum_c eta(c)*bar(alpha(c))/Nc^(3/2)*V(Nc/Z)
                      *sum_(h!=0) J_c(h)*U(X*Nh/Nc).         (H)
```

Keep the complete H, including all source prime powers. At a good prime
of norm Q, the all-size zero-frequency formula is

```text
J_(p^e)(0)=Q^(e-1)*[-p, -bar(p), Q-2]_(e mod 3), e>=1,
```

where the entries correspond to residues 1,2,0. This follows because the
character reduces modulo p and each residue has Q^(e-1) lifts. CRT makes
J_c(0) multiplicative without an additive Gauss reciprocity phase.

For Re(x)>1 the Mellin Dirichlet series consequently factors as

```text
D_eta(x)=sum_c eta(c)*bar(alpha(c))*J_c(0)/Nc^(x+1/2)
 = L^S(3*x-3/2,eta^3*bar(alpha)^3)*K_eta(x)/L^S(x,eta),

D=eta(p)*Q^(-x), E=eta(p)^2*bar(alpha(p))^3*Q^(1/2-2*x),
R=eta(p)^3*bar(alpha(p))^3*Q^(3/2-3*x), q=1/Q,
D_(eta,p)=(1-D-E-2*q*R)/(1-R),
K_(eta,p)=(1-D-E-2*q*R)/(1-D).
```

The three residue classes form one exact geometric series in R. The K
product converges normally for Re(x)>3/4: its defect is bounded by a
constant times Q^(-(2*Re(x)-1/2))+Q^(-(3*Re(x)-1/2)). It is holomorphic
there. For Re(x)>5/6, Q>=7 gives |D|<1/5, |E|<1/7, |R|<1/7, so

```text
|1-D-E-2*q*R| > 1-1/5-1/7-2/49 =151/245.
```

Every K factor, and therefore K_eta, is nonzero in that half-plane. The
completed-source L-factor has real part greater than one in its argument,
so is also nonzero there. The signal coefficient is thus explicitly
nonzero for every target eta and every Re(x)>5/6.

## 4. One complete trace estimate would give 0.84

Choose X=Z^(2/5). Formula (D) makes the full I smaller than any power.
The one remaining analytic contract is

```text
|H_eta(Z^(2/5),Z)| <<_(eta,S) Z^(399/10000), all Z>=2.   (OPEN)
```

If this held for each finite-order eta, I_0 would obey the same bound.
Its Mellin transform converges for Re(s)>399/10000. At zero, I_0 has
arbitrary power decay by the source test. On an initial right half-plane,
absolute convergence and the substitution r=Nc/Z give exactly

```text
integral_0^infinity I_0(Z^(2/5),Z)*Z^(-s) dZ/Z
 =U(0)*exp((s-1/5)^2)*D_eta(s+4/5).
```

Thus D_eta continues holomorphically to Re(x)>8399/10000. Its nonzero
holomorphic coefficient above prevents a pole of 1/L^S(x,eta) there. This
would prove nonvanishing for Re(x)>21/25, with reserve 1/10000. The usual
norm-lift factorization then gives the all-Dirichlet conclusion. This is a
conditional reduction, not an assertion of (OPEN) or a new bound.

The changed operator solves its direct physical estimate and moves the hard
part to one explicit nonzero-frequency trace average. It does not make that
average small automatically. In the chosen range the relevant h have norms
up to about Z^(3/5); dropping them would remove the obstruction by assumption.
In fact H_eta=-I_0+an arbitrary-power error here. This makes the arithmetic
strength of (OPEN) clear and rules out treating H as an innocuous tail.

## 5. The Fourier trace is a sextic Kloosterman trace

There is an elementary finite-field transformation that identifies the
remaining trace more precisely. At a good prime let theta=chi_p^2 be cubic,
let phi be quadratic, and let g use the same nontrivial additive character
as J. For every h, including zero,

```text
g(bar(theta))*J_p(h)
 =theta(-1/4)*phi(-1)*g(phi)*e(h/2)
   *S_(bar(theta)*phi)(1,h^2/16),

S_nu(a,b)=sum_(v!=0) nu(v)*e(a*v+b/v).
```

This holds for any nontrivial additive character, so it preserves the
Eisenstein normalization. To prove it, set x=(1+t)/2 and use

```text
theta(1-t^2)=g(bar(theta))^(-1)
               *sum_(v!=0) bar(theta)(v)*e(v*(1-t^2)),
sum_t e(-v*t^2+h*t/2)=phi(-v)*g(phi)*e(h^2/(16*v)).
```

The twist is bar(theta)*phi=chi_p, of exact order six. The Gauss ratio
g(phi)/g(bar(theta)) has modulus one. At h=0 the identity agrees with the
Jacobi value above. At the conjugate cubic mode e=2 mod 3 the twist is
chi_p^5. In particular, this transformation does not reduce the trace to
a cubic Kloosterman sum.

The checker verifies this formula for every h at five split primes, in
107 exact cyclotomic computations. It multiplies out the Gauss denominator,
uses coefficients in Z[omega], and reduces the additive polynomial by
Phi_p=1+z+...+z^(p-1). No floating-point comparison is used.

## 6. The precise remaining arithmetic

At p^e the trace vanishes unless p^(e-1)|h, and then equals Q^(e-1) times
the residue-field trace with character exponent e and frequency h/p^(e-1).
For e=0 mod 3 its nonzero residue-field frequencies are exactly
-1-e(h/p). Other residues give the Fourier transform of a cubic Jacobi
function. These are explicit facts about the full modulus, not permission
to restrict H to squarefree c.

[Paper 15 v1](https://rstation.ai/problems/riemann_hypothesis/papers/15/v1)
provides bilinear cubic Kloosterman bounds at a fixed squarefree modulus.
Our trace has a sextic twist, squared frequency and a varying modulus, so
that statement does not match this consumer; it also asserts no prime-power
extension. [Paper 13 v1](https://rstation.ai/problems/riemann_hypothesis/papers/13/v1)
separately estimates residues and complete zero covariance for a different
partial cubic packet, and explicitly leaves the regular/nonzero covariance
open. Neither theorem is being used to assert (OPEN). The next task is an
actual transformation or spectral estimate for this specific Jacobi trace,
with the fixed target twist, all h, and every prime power retained.
