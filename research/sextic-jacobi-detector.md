# Sextic Jacobi input, cubic Kloosterman output

Status: a changed Jacobi operator with a proved direct-side decay argument,
an exact all-prime-power reciprocal factorization, and a cubic Kloosterman
representation on squarefree moduli. The complete trace estimate is open.
The 0.8 implication below is conditional and is not a bound or a bound
submission. The sign of a Jacobi sum is classical prior work; the source and
credit discussion in [jacobi-detector.md](jacobi-detector.md) applies here.

The cubic Jacobi input in that note creates a sextic output trace. Reversing
these orders makes the output cubic and gives it the prescribed Mobius/Gauss
coefficient. This is a change of arithmetic operator, not an angular retuning.

## 1. The physical operator and its direct estimate

Use the same O, S, eta, alpha, e, V, W and U as in the cubic Jacobi control.
Put epsilon(c)=chi_c(4). This is a fixed cubic ray character supported at
2,3; all sources avoid those primes. Define, over all good ideals c,

```text
I6_eta(X,Z)=X^(-1/2)
 *sum_c eta(c)*bar(alpha(c))*epsilon(c)/sqrt(Nc)*V(Nc/Z)
      *sum_m chi_c(m^2-1)*W(Nm/X).
```

The source has no Gauss coefficient and no squarefree restriction. The
compensator may equivalently be put inside the character, replacing its
argument by 4*(m^2-1). The centered polynomial avoids a linear additive
phase in its Kummer transform. The elementary periodic-character proof in Section 2
of the control note applies with sextic reciprocity in place of cubic
reciprocity: for each fixed nonzero m^2-1, the source character is periodic
with period of norm at most C_(eta,S)*N(m^2-1). Its angular order is still
-1, so its zero lattice Fourier coefficient vanishes. Thus

```text
I6_eta(X,Z) <<_(A,eta,S) sqrt(X*Z)*(X^2/Z)^A
                           +X^(-1/2)*|V(1/Z)|, A>1.
```

In particular I6_eta(Z^(2/5),Z) has arbitrary-power decay. This argument
requires eta fixed, which suffices for a theorem about each finite target.
It asserts no uniformity for targets with growing conductor.

## 2. The complete zero frequency

Set

```text
J6_c(h)=sum_(x mod c) chi_c(x^2-1)*e(h*x/c).
```

Poisson gives I6_eta=I6_0+H6_eta with

```text
I6_0=sqrt(X)*U(0)*sum_c eta(c)*bar(alpha(c))*epsilon(c)
                                     *J6_c(0)/Nc^(3/2)*V(Nc/Z),
H6_eta=sqrt(X)*sum_c eta(c)*bar(alpha(c))*epsilon(c)/Nc^(3/2)
          *V(Nc/Z)*sum_(h!=0) J6_c(h)*U(X*Nh/Nc).           (H6)
```

Let p be good, Q=Np, and epsilon=chi_p(4). The residue-field Jacobi values
for exponents e=1,2,3,4,5,0 modulo six are exactly

```text
-p*bar(epsilon), -p*bar(epsilon), -1,
-bar(p)*epsilon, -bar(p)*epsilon, Q-2.
```

At p^e multiply the relevant entry by Q^(e-1). For e=1 the evaluation
follows from the Gauss identities in the pinned OpenAI source:

```text
J(chi,chi)=-p*chi(4)*chi(-1)^3.
```

The change t=2*x-1 is bijective modulo every good prime, and
t^2-1=4*x*(x-1). Thus the centered value multiplies the usual Jacobi sum
by chi(4)^e*chi(-1)^e in exponent e. This gives the displayed six values,
including -1 at e=3. The exact checks retain these signs and ray factors.

Put x=1+v for the source Mellin variable and
z=eta(p)*bar(alpha(p))*epsilon*Q^(1/2-x), q=1/Q. The zero-frequency
Euler factor is

```text
P_p(x)=[1-alpha*bar(epsilon)*sqrt(q)*z
          -alpha*bar(epsilon)*sqrt(q)*z^2-q*z^3
          -bar(alpha)*epsilon*sqrt(q)*z^4
          -bar(alpha)*epsilon*sqrt(q)*z^5-2*q*z^6]/(1-z^6).
```

This geometric series retains every prime power. Its first nonconstant term
is exactly -eta(p)*Q^(-x). Since epsilon^3=1, the full factorization is

```text
D6_eta(x)=sum_c eta(c)*bar(alpha(c))*epsilon(c)
                            *J6_c(0)/Nc^(x+1/2)
 =L^S(6*x-3,eta^6*bar(alpha)^6)*K6_eta(x)/L^S(x,eta).
```

Here K6_p is the numerator of P_p divided by 1-eta(p)*Q^(-x). The decay
powers of its remaining terms are

```text
2*Re(x)-1/2, 3*Re(x)-1/2, 4*Re(x)-3/2,
5*Re(x)-2, 6*Re(x)-2.
```

They all exceed one for Re(x)>3/4, so K6 converges normally there. It also
never vanishes there. For Q>=7, the absolute values of the first five
nonconstant numerator terms are at most 1/4, 1/7, 1/18, 1/18, 1/18;
the last is at most 1/63. The rational checks use 7^3>4^4 and 7^3>18^2.
Consequently the numerator has modulus greater than

```text
1-1/4-1/7-3/18-1/63 =107/252 >0.
```

The completed-source L-factor is absolutely convergent and nonzero in
this entire half-plane, since Re(6*x-3)>3/2. Therefore the reciprocal's
coefficient is holomorphic and nonzero for every Re(x)>3/4. This improves
the signal domain over the cubic-Jacobi control; it supplies no trace bound.

## 3. On squarefree sources the trace has the actual cubic Gauss coefficient

For a good prime apply the centered Kummer transformation, with theta=chi_p
of order six. Expand theta(x^2-1) as
theta(-1)/g(bar(theta))*sum_(v!=0)bar(theta)(v)*e(v*(1-x^2)),
then complete the quadratic sum in x. Since theta(-1)*phi(-1)=1, this gives

```text
J6_p(h)=g(phi)/g(bar(theta))*S_(bar(theta)*phi)(1,h^2/4;p).
```

The output character is

```text
bar(theta)*phi=chi_p^2,
```

of order three. Including the source compensator gives the particularly
simple formula, valid for every good squarefree c,

```text
bar(alpha(c))*epsilon(c)*J6_c(h)
 =mu(c)*gamma_4(c)*S_(chi_c^2)(1,h^2/4;c),

S_nu(a,b;c)=sum_(t mod c, unit) nu(t)*e((a*t+b*t^(-1))/c).
```

The inverse t^(-1) here is the inverse in O/(c), not the reciprocal of a
complex number. This distinction must survive any unfolding of the modulus.

The Kummer prefactor is gamma_3(c)/gamma_5(c). The inherited Gauss identities give
gamma_3/gamma_5=mu*alpha*bar(epsilon)*gamma_4. Multiplying by the source
bar(alpha)*epsilon leaves mu*gamma_4. CRT gives
the same identity on squarefree composite c. It is not an extension to
arbitrary prime powers; those remain in (H6) with their local lift factors.

Thus the squarefree portion of the remaining bound is exactly

```text
sqrt(X)*sum_(c squarefree) mu(c)*eta(c)*gamma_4(c)/Nc^(3/2)*V(Nc/Z)
  *sum_(h!=0) S_(chi_c^2)(1,h^2/4;c)*U(X*Nh/Nc).
```

This is a prescribed Mobius/cubic-Gauss coefficient, a cubic Kloosterman
trace and a squared frequency. The centered physical polynomial removes the
linear additive phase exactly; the modular inverse inside S remains. Replacing
it by a complex reciprocal is not an application of an unweighted Gauss
mean. For the full operator, exponents 1,2,4,5 modulo six have the analogous
residue-field Kummer transformations; exponent 3 is quadratic and exponent
0 is principal. Every p^(e-1)|h condition and lift remains mandatory.

## 4. A single explicit estimate would reach 0.8

At X=Z^(2/5), the remaining sufficient contract is

```text
|H6_eta(Z^(2/5),Z)| <<_(eta,S,e) Z^e
for every e>0 and all Z>=2.                            (OPEN6)
```

Section 6 replaces this by an equivalent complete mean-zero trace contract,
with an arbitrary-power error and with every prime power retained.

The direct sum is already negligible. If (OPEN6) held, the exact Mellin
identity would be

```text
integral_0^infinity I6_0(Z^(2/5),Z)*Z^(-s) dZ/Z
 =U(0)*exp((s-1/5)^2)*D6_eta(s+4/5),
```

with a holomorphic left side for Re(s)>0. The coefficient in Section
2 is nonzero for Re(x)>3/4, so 1/L^S(x,eta) would be holomorphic for
Re(x)>4/5. This would give all-finite-Hecke, and hence all-Dirichlet,
nonvanishing there. A bound Z^(-1/10000) is a stronger sufficient version,
with a fixed reserve. The subpower contract is not proved. It includes the
entire nonzero-frequency sum, not just the displayed squarefree part.

The direct estimate makes H6=-I6_0 plus an arbitrary-power error in this
regime. Thus the desired cancellation is substantial arithmetic information;
it does not follow from the smallness of the full physical sum. The purpose
of this reformulation is to expose an actual cubic trace with the right
coefficient, rather than rename a generic norm or introduce a zero-free axiom.

## 5. Checkpoint and outstanding source-to-consumer map

The shared checker records thirty direct residue-field Jacobi evaluations,
107 exact sextic-input Kummer transformations, five exact Gauss prefactor
checks, and the all-size period-six Euler identity. The cubic-input control
has its separate fifteen prime-power checks and 107 exact Kummer checks.
These are arithmetic certificates, not a check of (OPEN6).

The character order now agrees with the cubic Kloosterman theorem in
[Paper 15 v1](https://rstation.ai/problems/riemann_hypothesis/papers/15/v1),
but its fixed squarefree modulus, two short linear arguments and operator
norm do not directly estimate the varying-modulus, squared-frequency
correlation above. The prescribed signed Kubota sources in Papers 54 and
58 likewise require an actual transformation of the modular-inverse phase,
fixed eta and all prime powers. None of those theorem-to-consumer maps is
established here. That is the active analytic task.

The [cubic Airy reformulation](cubic-airy-trace.md) maps the squarefree
unit-frequency sector further to the classical polynomial x^3-3*x. Its
literal coefficient is still mu(c)*eta(c) times a normalized Gauss sum at
the same moving frequency. The linearized Kloosterman arguments are
diagonal; neither Louvel's unweighted average nor Paper 15's bilinear norm
estimates this weighted varying-modulus trace.

Even a favorable factorization h=u*v does not put the current parameters
inside the fixed-modulus short-window theorem. Kloosterman scaling turns its
arguments into u^2 and v^2/4. If Nu and Nv are balanced and Nh is of order
Nc/X, those argument windows have norm scale N=Nc/X. The direct regime
X<Nc^(1/2) forces N>Nc^(1/2), whereas Paper 15 requires N<=Nc^(1/2).
Partitioning or a theorem for monomial arguments would need a new cost
analysis; neither is a free invocation of that theorem.

## 6. Remove the complete finite frequency mean

There is one full mode that can be removed unconditionally, without changing
the signal or the target estimate. Put delta(c)=chi_c(-1), a fixed ray
character, and define

```text
J6_c^o(h)=J6_c(h)-delta(c),
H6_eta^o=sqrt(X)*sum_c eta(c)*bar(alpha(c))*epsilon(c)/Nc^(3/2)*V(Nc/Z)
                       *sum_(h!=0) J6_c^o(h)*U(X*Nh/Nc).
```

This is the actual finite Fourier mean: for every good c, including all
prime powers, orthogonality gives

```text
(1/Nc)*sum_(h mod c) J6_c(h)=chi_c(-1)=delta(c).
```

The removed contribution is rapidly decreasing when X=Z^a, 0<a<1.
To see this, put

```text
T_k(Z)=sum_c eta(c)*bar(alpha(c))*epsilon(c)*delta(c)/Nc^k*V(Nc/Z).
```

For each fixed k the finite coefficient is periodic, and its angular order
is -1. The same lattice Poisson argument as for the direct sum, now with
a fixed period, gives T_k(Z)=O_B(Z^(-B)) for every B. The Gaussian Poisson
formula in h, using integral U=1, gives

```text
sum_(h!=0) U(X*Nh/Nc)=Nc/X-U(0)+O_A((Nc/X)^(-A)).
```

Consequently

```text
H6_eta-H6_eta^o
 =X^(-1/2)*T_(1/2)(Z)-sqrt(X)*U(0)*T_(3/2)(Z)
   +O_A(sqrt(X)*X^A*Z^(-A-1/2)).
```

The last estimate uses absolute ideal counting with the lognormal test;
its Mellin moments converge at every real exponent. All three terms have
arbitrary-power decay at X=Z^a, 0<a<1. Thus (OPEN6) is equivalent to

```text
|H6_eta^o(Z^(2/5),Z)| <<_(eta,S,e) Z^e for every e>0.   (OPEN6o)
```

On squarefree c the centered Kloosterman version is exactly

```text
bar(alpha(c))*epsilon(c)*J6_c^o(h)
 =mu(c)*gamma_4(c)
   *[S_(chi_c^2)(1,h^2/4;c)-gamma_3(c)*gamma_5(c)].
```

The bracket has complete h mean zero. Opening the Kloosterman sum and doing
the complete quadratic sum in h gives its mean gamma_3*gamma_5 directly.
The checker verifies these finite means together with the Kummer identities.

This removes a complete finite-frequency mean. It is different from a
Kubota residue or the polar correction of Paper 54; its proof does not
identify the remaining trace with that paper's controlled output. No
estimate for the residual mean-zero covariance is asserted. The new input
needed for a bound is now specified by (OPEN6o), with the full all-modulus
definition above, rather than by subtracting an unspecified bad component.

## 7. The local kernel is a positive resolvent average

There is a stronger reason that the local numerator does not vanish. Let
theta=chi_p and z be as in Section 2. For |z|<1, direct summation of the
literal zero-extended character powers gives

```text
P_p(z)=1+(1/Q)*sum_(t!=1,-1) sum_(j>=1) [theta(t^2-1)*z]^j
      =2/Q+(1/Q)*sum_(t!=1,-1) 1/[1-theta(t^2-1)*z].
```

For |u|<1, Re(1/(1-u))=1/2+(1-|u|^2)/(2*|1-u|^2)>1/2. Hence

```text
Re(P_p(z))>1/2+1/Q.
```

This proves local nonvanishing for every Re(x)>1/2, with no restriction on
the target phase. It uses all six prime-power classes and the two character
zeros; it is not a numerical root search.

The global correction can be continued to the same half-plane by extracting
three further inverse L-functions. Define

```text
psi2=eta^2*bar(alpha)*epsilon,
psi4=eta^4*bar(alpha)^5*epsilon^2,
psi5=eta^5*bar(alpha)^6.
```

These have nonzero angular order when eta is finite. With E2,E4,E5 denoting
the corresponding numerator terms in Section 2, put

```text
Htilde_p=N_p/[(1-D)*(1-E2)*(1-E4)*(1-E5)],

D6_eta(x)=L^S(6*x-3,eta^6*bar(alpha)^6)*Htilde_eta(x)
 /[L^S(x,eta)*L^S(2*x-1/2,psi2)
   *L^S(4*x-3/2,psi4)*L^S(5*x-2,psi5)].
```

After clearing the denominator, every defect monomial has decay exponent
greater than one for Re(x)>1/2. The slowest are 3*x-1/2, 5*x-3/2 and
6*x-2. The exact script checks all thirteen monomials. Thus Htilde converges
normally there. Each of its local factors is nonzero by the positive
resolvent formula, and its denominators have modulus less than one in their
nonconstant terms. Htilde is therefore holomorphic and nonzero in that
half-plane.

This gives a meromorphic continuation of D6_eta to Re(x)>1/2. Its coefficient
of 1/L^S(x,eta) has no zeros for Re(x)>2/3: the numerator L-function is
absolutely convergent there, while each additional inverse L-function has
poles but no zeros, since its angular character is nonprincipal. Consequently
those new reciprocal factors cannot conceal a zero of the target. This is a
coefficient analysis, not an improved zero-free region.

An abstract zero-supremum argument can go further if a future trace estimate
is proved for a larger family. The family

```text
nu=eta_finite*alpha^k, k<=0,
```

is closed under nu -> nu^6*bar(alpha)^6, whose angular order is 6*k-6.
Its direct estimate and removed-mean estimate still hold: the source angular
order is k-1, which is nonzero. Constants may depend on the fixed k.
If (OPEN6o) were replaced throughout this family by the unproved bound

```text
H6_nu^o(Z^(2/5),Z) <<_(nu,e) Z^(theta-4/5+e), every e>0,
```

with one fixed theta>3/5, all those L-functions would be nonvanishing for
Re(x)>theta. Indeed let beta be the supremum of their zero real parts.
If beta>theta, choose a zero rho sufficiently close to beta so that
6*Re(rho)-3>beta. At rho the completed-source character is still in the
family, so its L-value in the numerator cannot vanish. The other extracted
reciprocals cannot cancel the target pole, and Htilde is nonzero. This
contradicts the holomorphy furnished by the trace bound. The inequality is
possible because (6*beta-3)-beta=5*beta-3>0.

This last argument requires the enlarged family explicitly. An estimate only
for finite-order eta cannot be used with a supremum over angular twists.
No such family trace estimate is proved here. In particular neither this
bootstrap nor local positivity establishes the requested bound.
