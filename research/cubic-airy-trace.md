# The Jacobi trace as a weighted cubic exponential sum

Status: a classical finite identity mapped to the squarefree, unit-frequency
part of the actual sextic Jacobi probe. It gives a linear frequency in a
cubic polynomial, while retaining a frequency-dependent Gauss weight. It
does not prove the complete trace estimate or a new zero-free region.

The cubic exponential-sum identity is prior work. Louvel,
[*On the distribution of cubic exponential sums*, v2](https://arxiv.org/abs/1107.0197v2),
Proposition 2.1, records it and attributes the version used there to
Patterson, Theorem 3.1. The residue-field trace calculation below is also
the one in [Paper 15 v1](https://rstation.ai/problems/riemann_hypothesis/papers/15/v1),
Lemma 3.1. The contribution here is the literal coefficient map and its
scope controls for [the sextic Jacobi detector](sextic-jacobi-detector.md).

## Finite identity and squared-frequency scaling

Let F have q elements, characteristic greater than three, and q=1 modulo
three. Let nu be either nontrivial cubic character, extended by zero, and
psi a nontrivial additive character. Put

```text
D(x)=x^3-3*x,
f(y)=#{x in F:D(x)=y}-1,
A(t)=sum_(x in F) psi(t*D(x)).
```

For every y, the following is an exact equality:

```text
f(y)=sum_(u!=0, u+u^(-1)=y) nu(u).
```

For split distinct roots u,u^(-1), the right side is 2 or -1 according
as u is a cube or not. The identity
`D(v+v^(-1))=v^3+v^(-3)` gives respectively three or zero roots on the
left. For nonsplit roots the norm-one torus has order q+1, coprime to
three; cubing is bijective there and D has exactly one rational root.
At y=2,-2 there are exactly two distinct roots of D(x)=y, and the unique
u=1,-1 has cubic character one. These cases exhaust F.

Fourier transforming this equality gives, for every t, including zero,

```text
S_nu(t,t)=A(t)-q*1_(t=0).
```

For h!=0 set t=h/2. The change of variable u=t*v in the Kloosterman sum
then gives the useful form

```text
S_nu(1,h^2/4)=nu(t)*A(t).
```

At h=0 the left side is the nonzero Gauss sum g(nu), while the right
side with a zero-extended nu would be zero. Thus the unit condition
cannot be dropped. The exact checker verifies both the trace-value and
squared-frequency identities at every residue of five split fields,
107 cases for each identity; the h=0 cases retain g(nu).

## The actual coefficient after the transformation

Now let c be good and squarefree and `(h,c)=1`. Take
`nu_c=chi_c^2` and `t=h/2` in O/(c). CRT extends the unit-frequency
identity, with each local additive character kept unchanged. Define

```text
A_c(t)=sum_(x mod c) e(t*(x^3-3*x)/c),
Gbar_c(t)=(Nc)^(-1/2)*sum_(u mod c) conjugate(nu_c(u))*e(t*u/c).
```

Since t is a unit, change u to t^(-1)*u to obtain
`Gbar_c(t)=nu_c(t)*gamma_4(c)`. Consequently the dressed trace of the
actual probe is exactly

```text
mu(c)*eta(c)*gamma_4(c)*S_(nu_c)(1,h^2/4;c)
 =mu(c)*eta(c)*Gbar_c(h/2)*A_c(h/2).
```

The common profile `U(X*Nh/Nc)` and source weight
`sqrt(X)*V(Nc/Z)/Nc^(3/2)` are unchanged. For the centered trace, retain
also the original subtraction
`mu(c)*eta(c)*gamma_4(c)*gamma_3(c)*gamma_5(c)`.
This formula covers the squarefree unit-frequency sector. Nonunit
frequencies have their original local Gauss terms; nonsquarefree sources
have the prime-power lifts of the full Jacobi formula. Neither is removed
by this rewriting.

## What published estimates still need

Louvel's Theorem 1.3 averages `A_c(1)/sqrt(Nc)` in source congruences.
Here the frequency grows, the coefficient contains the actual Mobius
function, and `Gbar_c(h/2)` is coupled to that same frequency. Removing
this coefficient by its absolute value discards the cancellation needed
for the target estimate. The unweighted theorem is not the required
weighted two-parameter theorem.

The linear frequency in `S_nu(t,t)` is still diagonal. Replacing its two
identical arguments by independent variables would change the sum.
Paper 15 estimates a bilinear form on two short windows at one squarefree
modulus. At its endpoint N=Q^(1/2), the bound for the normalized kernel's
operator norm is Q^(15/32+epsilon). A direct trace estimate from this norm
costs the rank N and is Q^(31/32+epsilon), whereas the pointwise Weil
estimate already gives O(N)=O(Q^(1/2)). Thus that theorem alone supplies
no saving for this diagonal sum, even in its permitted window range.
The probe's full frequency window has area Q/X=Q^(3/5), which additionally
exceeds that range when X=Q^(2/5).

This closes the elementary change-of-variables question. A new weighted
varying-modulus estimate, with the Gauss coefficient, diagonal restriction,
nonunit modes and prime-power lifts controlled, is still required.
