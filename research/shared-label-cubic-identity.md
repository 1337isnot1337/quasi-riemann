# The shared-label cubic identity

This note gives a written derivation of an exact global representation for a
changed probe. Its local kernel and unit packet have exact symbolic checks;
its Poisson normalization also has a separate numerical finite-Fourier check.
The latter includes direct sums at two actual primary Eisenstein primes of
norms 7 and 13, in all 16 source/label overlap configurations.
It proves no estimate for the signed row sum and no new zero-free half-plane.
The analytic derivation is not formalized in Lean.

## Definitions

Work in `O=Z[omega]` with norm `N`, and use the additive character
`e(z)=exp(2*pi*i*Tr(z/sqrt(-3)))`. Normalize Haar measure so that `O` has
covolume one. This pairing makes `O` self-dual. Fourier transforms use the
kernel `e(-zy)`.

Let `S` be a finite set of prime ideals containing those above 6 and the
conductor of a fixed finite-order Hecke character `eta`. Source ideals and
labels avoid `S` and use their multiplicative primary generators. Write
`chi_A` for the sextic residue character of the ideal `A`, extended by zero
at every prime of `A`, even when its exponent is divisible by six. Put
`alpha(A)=A/sqrt(N(A))` on primary generators and let `gamma_r(c)` be the
normalized Gauss sum for `chi_c^r` with the stated additive character.

Choose a smooth annular label profile `B`. The source profile `V` may be
annular or decrease faster than every power at both ends, with the same
property for all logarithmic derivatives. The choice

```
V(r)=(4*pi)^(-1/2) exp(-(log r)^2/4)
```

has the nowhere-zero Mellin transform `M[V](v)=exp(v^2)`.
Choose radial Schwartz profiles
`W_i(Nz)` whose Fourier transforms vanish at zero, and write their radial
Fourier profiles as `U_i`. In these self-dual coordinates the example

```
W(r)=exp(-pi*r)-2*exp(-2*pi*r)
```

has radial Fourier profile

```
U(r)=(2/sqrt(3)) [exp(-4*pi*r/3)-exp(-2*pi*r/3)].
```

Its Mellin value at `1/3` is nonzero. All transforms below use
`M[f](s)=integral_0^infinity f(r) r^s dr/r`.

For a completed source ideal `A=c*n^3`, define

```
P_i(A,s) = [N(s) X_i]^(-1/2)
    * sum_(m in O) chi_A(m)^2 chi_s(m)^4 W_i(N(m)/(N(s) X_i)).
```

The probe is

```
J_eta(X1,X2,Y,Z) = Y^(-1)
  * sum_(s squarefree, good) B(N(s)/Y) gamma_4(s)^(-2)
  * sum_(c squarefree,n good)
      gamma_2(c) conjugate(alpha(c*n^3)) eta(c*n^3)
      /[sqrt(N(c)) N(n)] * V(N(c*n^3)/Z)
      * P_1(c*n^3,s) P_2(c*n^3,s).
```

All overlaps are allowed. Gauss sums in the compensator have absolute value
one because `s` is squarefree and good. The label sum is finite, and all
source and element sums converge absolutely by the profile decay.

## The row representation

Index cube classes by `u=omega^r*u0`, `r=0,1,2`, where `u0` is the chosen
generator of a cube-free integral ideal. To include the prime above 3,
choose its generator `sqrt(-3)` and multiply it by the primary generator
of the remaining ideal. This gives a multiplicative generator convention.
Let `rho_u(p)=(u/p)_3` at good primes, with value zero at primes of `u`.
These are finite-order cubic Kummer Hecke characters, including their fixed
ramified components. Only the trivial cube class gives a principal character.

Put `x=3/2+v-t1-t2`. For each good prime define `A_p=Q^(-t1)`,
`B_p=Q^(-t2)`, and

```
D_p=eta(p) rho_u(p)^(-1) Q^(-x),
W_p=rho_u(p) Q^(-w),
T_p=eta(p) Q^(-x-w),
R_p=eta(p)^3 conjugate(alpha(p))^3 Q^(-1-3v).
```

The inverse character in `D_p` retains its zero at ramified primes.
The values `T_p` and `R_p` do not vanish there. Use the rational functions
`F_j,G_j,M_j` derived in [binary-cubic-probe.md](binary-cubic-probe.md).
For a fixed row set

```
K_u(v,t1,t2,w)
  = product_(p outside S) M_(v_p(u0))(A_p,B_p,Q,D_p,W_p,T_p,R_p)
    * product_(p in S) F_(v_p(u0))(A_p,B_p).
```

Here every valuation of `u0` is in `{0,1,2}`. On initial absolute lines
`Re(v)=6`, `Re(t1)=Re(t2)=2`, `Re(w)=2`, the identity is

```
J_eta = 12 sqrt(X1 X2)/(2*pi*i)^4
  * integral Z^v X1^(-t1) X2^(-t2) Y^(w-1)
      M[V](v) M[U_1](t1) M[U_2](t2) M[B](w)
      * sum_(cube classes u) K_u(v,t1,t2,w)
    dv dt1 dt2 dw.
```

The row sum and Euler products converge absolutely on these lines. This
identity alone gives no continuation of the infinite row sum to other lines.

## Proof and the finite local factors

For each fixed source and label, the product character in `P_i` has modulus
`A*s`. Lattice Poisson gives

```
P_i(A,s) = sqrt(X_i)/[N(A) sqrt(N(s))]
    * sum_(h in O) g_(chi_A^2 chi_s^4)(A*s,h) U_i(X_i N(h)/N(A)).
```

The zero frequency vanishes because `U_i(0)=0`. This holds for principal
and imprimitive characters as well. Mellin inversion of the four radial
profiles gives the displayed outside powers. No auxiliary quadratic
character is needed to delete zero frequencies.

At a good prime, let source, cube and label valuations be `e,ell,k`, with
`e,k` in `{0,1}`. The modulus has exponent `e+3ell+k`, and its unit
character has cubic exponent `e-k`. If exactly one of `e,k` is one, the
two Gauss lifts force both frequency valuations to be `3ell`. If both are
zero or both one, the two principal Gauss lifts give the Ramanujan branches
in the local note. The scalar phases are respectively `-1`, `+1` and `-1`
after combining the source, compensator and angular weight. These yield
`-D`, `W`, and the `-T Q^2 A_p^2 B_p^2` overlap term.

Every cross-prime phase is one by the exact divisible-by-six identity in
the local note and cubic reciprocity for primary generators. Thus the
resulting coefficients factor over good primes even when `c,n,s` overlap.
At primes in `S`, all three source valuations are zero, so the only factor
is the frequency generating series `F_j`. There are no hidden Gauss factors
or target-dependent conductors at those frequency primes.

Finally, for each pair of frequency ideals there are 36 element unit pairs.
Exactly 12 pairs have their product in each of the three unit cube classes.
Their phases are absorbed in `rho_(omega^r u0)`. This proves the factor 12
and accounts for the complete unit packet. The checker verifies its cubic
orthogonality exactly for all nine pairs of source/label unit characters.
Absolute convergence on the initial lines permits all rearrangements used
in this derivation.

## The principal selector and its limits

The supports also retain a useful restriction before any bound is applied.
If a local Fourier term is nonzero, its frequency valuation is at least
`e+3ell+k-1` when the modulus is nontrivial. It follows in every branch that
both frequencies are divisible by

```
n^3/rad(n),       and       n^2*gcd(c,s).
```

Consequently `N(n)^2 N(gcd(c,s)) <= N(h_i)`. A second average with
`X2=Z^(1-epsilon)` restricts its effective frequency range to
`N(h2)<=Z^(epsilon+small_loss)`, so the completion index and source/label
overlap are short. In particular, since `N(c*n^3)` is comparable to `Z`,
the source column satisfies `N(c) >= Z/N(h2)^(3/2)`, up to fixed constants.
These are support consequences, not cancellation estimates. They avoid
discarding a long completion tail that this probe does not actually have.

For each fixed row, scalar extraction gives the ordinary factor

```
L^S(w,rho_u)/L^S(2w,rho_u^2)
```

and inverse factor `1/L^S(x,eta*rho_u^(-1))`. The common frequency factors
are the four zeta functions in the local note, and the angular factor is
`L^S(1+3v,eta^3*conjugate(alpha)^3)`. The remaining Euler product is normally
convergent near `t1=t2=1/3`, `w=1`, `Re(x)>1/2`, for each fixed row. Its
good-prime defect has decay `O(Q^(-2)+Q^(-1-Re(x))+Q^(-3Re(x)+1/2))` there.

Only the trivial cube class contributes the ordinary pole at `w=1`.
At that pole and at the frequency intersection, the good-prime principal
numerator is

```
(1-D)(1+Q^(-1)) + (1-R)(F0-1).
```

It has positive real part for `Re(x)>1/2`. All bad-prime factors at this
point are positive. The remaining angular L-factor is nonzero for
`Re(x)>5/6` by absolute convergence. Thus this scalar extraction preserves
the target reciprocal locally in that range; it does not replace it by a
sum of unrelated fixed reciprocals.

Four frequency poles meet in two variables, so extraction can produce a
quadratic logarithmic factor, with candidate power

```
Z^(x-5/6) (X1 X2)^(1/6).
```

The final asymptotic and its contour errors are not proved here. With
`X_i=Z^(a_i)`, `0<a_i<1`, Schwartz truncation suggests a cube-free row range
`N(u)<=Z^(2-a1-a2+epsilon)`. Proving the required continued, truncated row
estimate and the direct bound is the next analytic task. Character order
three alone supplies no improved inverse moment: the available cubic
normalized comparator `U+U^(1/3)N` cannot be renamed as a bound `U` through
column length `N=U`. Every source used on this changed probe needs its
actual length and twist conditions checked.
