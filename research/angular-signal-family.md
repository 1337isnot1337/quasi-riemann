# An angular identity and a separating family of candidate residues

Status: a written Poisson identity on absolute lines and an analysis of its
fixed-principal-row residue. The angular Fourier, unit, completion and local
nonvanishing algebra have exact certificates. The contour shifts exposing this
residue in the full probe, the other rows and the direct bound remain unproved.
There is no improved zero-free threshold.

The starting candidate is [angular-cubic-probe.md](angular-cubic-probe.md).
For the radial construction and all its valuation branches, use the separate
[shared-label identity at f3e7ebc](https://github.com/1337isnot1337/quasi-riemann/blob/f3e7ebc638892c630645d38d326c20e514b6b9df/research/shared-label-cubic-identity.md)
and its linked local-kernel derivation. The cubic Gauss identity and theta
completion are inherited from OpenAI's September 30 manuscript, at the source
pin recorded there. No novelty is claimed for those inputs.

## 1. Physical definition and Fourier normalization

Use the ring, primary generators, bad set S, characters and self-dual Fourier
pairing of the radial identity. Thus alpha(a)=a/sqrt(Na) and the Fourier kernel
is exp(-2*pi*i*Tr(zy/sqrt(-3))), with Haar density 2/sqrt(3).
For k1=2 and k2=-4 choose

```text
W_i(r)=r^(abs(k_i)/2)*exp(-pi*r),
U_i(r)=(2/sqrt(3))^(abs(k_i)+1)
       *r^(abs(k_i)/2)*exp(-4*pi*r/3).
```

Then alpha(z)^k_i W_i(Nz) is a Schwartz polynomial Gaussian. Its Fourier
transform is alpha(y)^(-k_i) U_i(Ny). Both U_i(0) vanish. In particular,

```text
M[U_i](t)=(2/sqrt(3))^(abs(k_i)+1)
          *(4*pi/3)^(-t-abs(k_i)/2)*Gamma(t+abs(k_i)/2).
```

The checker derives both polynomial Fourier transforms by differentiation of
the ordinary two-dimensional Gaussian transform, including the Haar factor.

For A=c*n^3 define

```text
P_i(A,s)=[Ns*X_i]^(-1/2)
  *sum_m chi_A(m)^2 chi_s(m)^4 alpha(m)^k_i
         W_i(Nm/(Ns*X_i)).

J_eta=Y^(-1)*sum_(s squarefree,good)
        B(Ns/Y)*alpha(s)^2*gamma_4(s)^(-2)
  *sum_(c squarefree,n good)
     gamma_2(c)*alpha(c*n^3)*eta(c*n^3)/(sqrt(Nc)*Nn)
     *V(N(c*n^3)/Z)*P_1(c*n^3,s)*P_2(c*n^3,s).
```

Use B smooth, nonnegative, supported on 1<r<2 and not identically zero, and
`V(r)=(4*pi)^(-1/2)*exp(-(log r)^2/4)`, with `M[V](v)=exp(v^2)`.
There is no ambiguity at m=0: its polynomial Gaussian value is zero.

Poisson supplies alpha(h_i)^(-k_i)*alpha(A*s)^k_i in each average. The
source/label phases consequently satisfy

```text
alpha(A)^1*alpha(s)^2*alpha(A*s)^(k1+k2)=alpha(A)^(-1).
```

After both transforms the source and label phases are exactly those in the
radial derivation; the frequency phases are new. This accounts for every
source/label overlap, rather than assuming coprimality.

## 2. The complete row identity on absolute lines

Write u=omega^r*u0, r=0,1,2, for the cube classes used in the radial identity.
Put rho_u(p)=(u/p)_3, with its literal zero at p|u, and
x=3/2+v-t1-t2. At each good prime of norm Q set

```text
A_p=alpha(p)^(-2)*Q^(-t1), B_p=alpha(p)^4*Q^(-t2),
D_p=eta(p)*rho_u(p)^(-1)*Q^(-x), W_p=rho_u(p)*Q^(-w),
T_p=eta(p)*Q^(-x-w),
R_p=eta(p)^3*alpha(p)^3*Q^(-1-3v).
```

The completion ratio R is important. Each new cube layer increases BOTH
frequency valuations by three. Its angular factor is
(alpha^(-2)*alpha^4)^3=alpha^6. Thus the old bar(alpha)^3 in R becomes
alpha^3. Substituting angular A,B while retaining the radial R is incorrect.

For j=0,1,2 define, with den=(1-A^3)*(1-B^3),

```text
F0=(1+A*B^2+A^2*B)/den,
F1=(A+B+A^2*B^2)/den,
F2=(A^2+A*B+B^2)/den,
r_j=(j+1) mod 3,
Gj=(1-1/Q)^2*Fj
   -(1-1/Q)/Q*[A^(-1)*B^r_j/(1-B^3)
                +A^r_j*B^(-1)/(1-A^3)]
   +1_(j=1)/(A*B*Q^2),
Mj=Fj+[R*Gj+1_(j=0)*(W-D)-T*Q^2*A^2*B^2*G_(j-1 mod 3)]/(1-R).
```

All four branches (c,s) at a prime and all n valuations are included in this
formula. Their derivation is the radial valuation proof with the displayed
frequency phases and new geometric ratio. Cross-prime Gauss phases are
unchanged, because the total source/label phase after Poisson is unchanged.

The unit packet also changes. For fixed frequency ideals, there are twelve
unit pairs in each product cube class omega^r. Their angular weight is
omega^r: if the units are signs times omega^a,omega^b, then
omega^(-2*a+4*b)=omega^(a+b). The cubic Gauss phase is constant in each
class and remains in rho_u. This gives

```text
K_u=product_(p outside S) M_(v_p(u0))
     *product_(p in S) F_(v_p(u0)),

J_eta=12*sqrt(X1*X2)/(2*pi*i)^4
  *integral Z^v X1^(-t1) X2^(-t2) Y^(w-1)
     M[V](v) M[U1](t1) M[U2](t2) M[B](w)
     *sum_(u=omega^r*u0) omega^r*K_u  dv dt1 dt2 dw.
```

This identity holds on Re(v)=6, Re(t1)=Re(t2)=2, Re(w)=2, where the
rearrangements converge absolutely. The checker verifies the unit identity
for all three cubic characters, as well as the twelve-pair multiplicity.
It does not justify continuation of this infinite row sum to other lines.
The Fourier support conditions from the radial identity are unchanged.

## 3. A nonzero local principal residue

For a fixed row, the extracted scalar frequency factors are

```text
L^S(3*t1,alpha^(-6))*L^S(3*t2,alpha^12)
*L^S(t1+2*t2,alpha^6)*zeta^S(2*t1+t2).
```

The other scalar factors are

```text
L^S(1+3*v,eta^3*alpha^3)
*L^S(w,rho_u)/L^S(2*w,rho_u^2)/L^S(x,eta*rho_u^(-1)).
```

Only u=1 has the ordinary w=1 pole. In that row take w=1, t2=1-2*t,
Re(t)=1/3, and v=x-1/2-t. Write q=1/Q and z=A^3/q, so |z|=1 and
A^2*B=q. The exact simplifications are

```text
den=(1-q*z)*(1-q/z^2),
F0=(1+q+q/z)/den,
G0=(1-q)/(1-q/z^2), B*G2=q/z^2*G0,
E=(1-R)*M0=F0+R*(G0-F0)+q-D*(1+B*G2).
```

If Re(x)>5/6, then |R|<q and |D|=Q^(-Re(x))<1/5 for Q>=7;
the latter follows from 7^5>5^6. The elementary bounds

```text
|F0|>=1/(1+q)^2,
|G0-F0|<=(2*q-q^2)*|F0|+2*q,
|B*G2|<=5*q
```

therefore give, uniformly in the angular phases and imaginary parts,

```text
|E| >= (49/64)*(1-(1/7)*(2/7-1/49))
        -2/49-1/7-(1/5)*(1+5/7)
     =1647/7840 >0.
```

The corresponding good-prime correction is

```text
H_p=(1-q*z)*(1-q/z^2)*(1-q/z)*(1-q)*E/[(1-D)*(1+q)].
```

Its defect is O(q^2+|D|*q+|R|*q), uniformly on this line and locally
uniformly in x. In fact the coefficient of q, with D,R kept as parameters,
is (D-R)*(z+1)^2/[z*(1-D)]. The product of these corrections converges
normally and never vanishes in Re(x)>5/6. The finitely many bad-prime F0
factors are also nonzero: their numerator has modulus at least one and
their denominator does not vanish. This proves local noncancellation of
the candidate residue for every target eta, rather than just eta=1.

## 4. A scale family avoids an unexplained nonzero-coefficient assumption

Put kappa=X2^2/(Z*X1). Taking the two scalar residues just described would
give a principal contribution of the form

```text
c_S * Z^(-1/2)*sqrt(X1/X2)/(2*pi*i)
 *integral Z^x A_eta(x,kappa)/L^S(x,eta) dx,

A_eta(x,kappa)=1/(2*pi*i)*integral_(Re(t)=1/3) kappa^t
 *exp((x-1/2-t)^2)*M[U1](t)*M[U2](1-2*t)
 *L^S(3*t,alpha^(-6))*L^S(3-6*t,alpha^12)
 *L^S(2-3*t,alpha^6)
 *L^S(3*x-1/2-3*t,eta^3*alpha^3)*H_eta(x,t) dt,

c_S=12*Res_(s=1)(zeta^S(s))^2*M[B](1)/zeta^S(2)>0.
```

Here H_eta includes the finite bad-prime factors from Section 3. This formula
analyzes a fixed-row scalar residue; it is not yet an asymptotic for J_eta.

For every fixed complex x with Re(x)>5/6, the inner Mellin integrand is
not identically zero as a function of t. Its H factor is nonzero by Section
3. The completed-source L-factor is in Re(s)>1 and is nonzero there. The
three nonprincipal angular Hecke L-functions are analytic and none is
identically zero. Their zero sets on the t-line are discrete; no theorem
asserting their nonvanishing on the entire line is needed. The Gamma factors
and exp((x-1/2-t)^2) do not vanish either.

The integrand has Gaussian decay as |Im(t)| tends to infinity, using fixed
degree Hecke growth and the displayed Gamma factors. Thus A_eta(x,exp(l))
is an entire function of the complex variable l. Fourier uniqueness on the
t-line implies that it is not identically zero. In particular,

```text
for every Re(x)>5/6, some rational kappa in [1,2]
satisfies A_eta(x,kappa)!=0.
```

Indeed vanishing at all those rational points would imply vanishing on an
interval, then identically, contradicting uniqueness. This countable family
separates every target zero in that half-plane. A proof may use whichever
fixed kappa detects its hypothetical zero; no particular single kappa needs
an unproved nonvanishing assertion. Bounded fixed kappa does not alter a
power-of-Z estimate. If X1=Z^a and X2=sqrt(kappa)*Z^((1+a)/2), the candidate
signal power is x-3/4+a/4, with a fixed kappa-dependent constant.

## 5. What remains

This closes the elementary angular global-identity and local/noncommon-zero
questions. It leaves the substantial analytic problems: expose the stated
principal residue by permitted contour shifts in the full row sum, bound all
other rows and remaining contours, and prove a direct physical estimate
strictly smaller than the signal power at a new threshold. The second
frequency range is Z^((1-a)/2), a positive power unless a=1; its sum cannot
be treated as a constant.

The coefficient-specific comparison remains bramble_trace,
[Paper 5 v3, Theorem 1](https://rstation.ai/problems/riemann_hypothesis/papers/5/v3).
Its downloaded Markdown has SHA-256
`414d196862672b5aefbfa671b4b2e60f60ad9dde12dc3042d038a1bfb1d08d39`.
After one transform, the source matches D_2 after conjugation. The label
coefficient lacks the Mobius factor, so the same cubic theorem cannot be
applied to it. Nothing in the separation argument supplies that missing mean
estimate or its moving-label uniformity.
