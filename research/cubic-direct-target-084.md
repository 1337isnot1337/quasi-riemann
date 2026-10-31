# A single direct estimate that would give 0.84

**The direct estimate below is unproved. No improved zero-free region is
claimed.** This note derives its implication for the shared-label cubic probe,
including the row error and principal extraction. The arithmetic and exponent
checks are exact; the analytic argument is written and is not Lean formalized.

## Fixed probe and the remaining input

Use `J_eta` from [the shared-label identity](shared-label-cubic-identity.md).
Fix the lognormal source profile with Mellin transform `exp(v^2)`, and fix
both physical profiles to `exp(-pi*r)-2 exp(-2*pi*r)`. Choose the nonnegative
label profile

```
B(r)=exp(-1/((r-1)(2-r))) for 1<r<2, and B(r)=0 otherwise.
```

Its Mellin value at one is positive. For every finite-order Hecke target
`eta`, take `S` to contain the primes above 6 and its conductor. Constants
may depend on this fixed data; all displayed powers must be independent of
the target. Put

```
X1=Z^(73/100), X2=Z^(99/100), Y=Z^(73/100),
theta=21/25, h=2-log_Z(X1)-log_Z(X2)=7/25.
```

The remaining direct estimate is

```
|J_eta(X1,X2,Y,Z)| <<_(eta,S) Z^(8797/30000)
```

for every sufficiently large real `Z`. This is the candidate principal
power `22/75` minus reserve `1/10000`. It concerns the original complete
probe, with every cube factor, Gauss compensator, overlap and mask retained.
A bound on its pole-subtracted part does not assert this input.

The following conditional implication is the point of the construction:
**if this direct estimate holds for every fixed target, the shared-label
probe gives nonvanishing for Re(s)>21/25 for finite-order Hecke L-functions
over the Eisenstein field, and hence for all Dirichlet L-functions.**
The proof below uses classical Hecke convexity and the standard reciprocal
strip estimate on a global zero-free line. It does not assume a new density
theorem or a stronger inverse-polynomial moment.

The reciprocal strip input is the source's
`Hecke/ReciprocalGrowth.lean:reciprocal_subpower`, based on
`Hecke/LogarithmicActual.lean:primitive_reciprocal_subpower`. Its positive
margin parameter may be chosen below kappa/8. Both files and the primitive
functional equation are hash-pinned; their upstream Lean closure was not
rebuilt here.

## A normal-convergence box for all contour moves

Write `x=3/2+v-t1-t2`, and set

```
epsilon=1/1000, kappa=1/1000000,
z_minus=1/3-epsilon, z_plus=1/3+epsilon, w0=1/2+epsilon.
```

For the unramified local kernel define

```
H_p = M0 (1-R)(1-A^3)(1-B^3)(1-A*B^2)(1-A^2*B)
           /[(1-D)(1+W)],
```

where `T=DW`. The cleared defect `(H_p-1)(1-D)(1+W)` has 78 Laurent
monomials. Each has norm at most `Q^(-267/200)` throughout

```
Re(x)>=21/25,
z_minus<=Re(t1),Re(t2)<=2,
w0<=Re(w)<=2.
```

For a monomial `D^d W^j A^a B^b R^r Q^q`, its decay exponent is

```
d Re(x)+j Re(w)+a Re(t1)+b Re(t2)
  +r[3 Re(x)-7/2+3 Re(t1)+3 Re(t2)]-q.
```

It is affine, and its coefficient of `Re(x)` is nonnegative. The exact
certificate therefore checks all finite vertices and the whole unbounded
x half-line. Both remaining local denominators are bounded away from zero.
The angular argument has real part at least `507/500>1`, so that scalar
L-factor stays in absolute convergence too.

The finite ramified factors are holomorphic on this box. On the final
equal frequency lines their bounds retain `N(u)^(-z_plus)`, up to an
arbitrary divisor loss. The checker verifies every monomial after that row
weight is removed. These bounds are uniform in imaginary parts and unit
phases. They give actual convergence and row weights, rather than only a
formal local simplification at real residue points.

## The whole row error needs no improved count

Let `beta_*` be the supremum of real parts of nontrivial zeros across all
finite-order Hecke L-functions over the field. Euler convergence gives
`beta_*<=1`. Assume for contradiction `beta_*>theta`.

The source profile is rapidly decreasing at both ends, and the Fourier
profiles are Schwartz. Before any contour move, the source and frequencies
may thus be truncated so that

```
N(u)<=Z^(h+epsilon)
```

with an error smaller than every fixed negative power. For example, first
restrict the completed source norm to `Z^(1+-epsilon/8)` and each frequency
to norm at most `Z^(1-a_i+epsilon/4)`. The omitted profile tails dominate
all polynomial costs of the finite Gauss sums. Fix these row sets before
moving their Mellin variables.

Move the reciprocal coordinate to `Re(x)=beta_*+kappa`, the two frequency
coordinates to `z_plus`, and `w` to `w0`. The frequency zeta arguments stay
to the right of one. The only w pole crossed is the ordinary pole of the
trivial cubic row at one. The denominator `L^S(2w,rho_u^2)` has real part
greater than one throughout the move, so it creates no zero poles.

For the retained w line, classical conductor convexity gives numerator
size at most `N(u)^((1-w0)/2+small_loss)`. The inverse on
`Re(x)=beta_*+kappa` is `N(u)^small_loss` times a polynomial in height:
the global zero-free line, strip growth, Borel--Caratheodory and
three-circles give the standard reciprocal strip estimate. Its constant
may depend on the fixed positive kappa. The correction contributes its
row weight `N(u)^(-z_plus+small_loss)`. The number of row ideals through
norm U is O(U), including all three unit classes.

For clarity, the convexity power here follows from the primitive Hecke
functional equation: on `Re(s)=1+delta` Euler convergence gives a uniform
bound, and on `Re(s)=-delta` the functional equation gives conductor power
`1/2+delta`. Interpolation yields `(1-Re(s))/2+delta/2`. Choose delta
below twice the allocated small loss. The finite-order characters have
trivial infinity type, and the principal character is treated away from
its pole. This refines the coarse strip exponent used elsewhere in the
baseline without assuming a new subconvexity theorem.

Ignoring adjustable losses, the resulting exponent relative to the
candidate principal scale is

```
-y/2 + (11/12)h = -13/120.
```

The exact replay also charges the x displacement, frequency displacement,
row cutoff enlargement and three conductor/divisor losses of `1/100000`.
Its resulting relative exponent is less than `-1/10`.
Thus the unresidued row integral is power smaller with the full row count;
no improved count at a critical density class is assumed.

The all-height integral and horizontal joins are justified by the normal
box, polynomial Hecke bounds, the Gaussian source Mellin transform, the
gamma decay of the two Fourier-profile Mellin transforms, and arbitrarily
rapid decay of the label Mellin transform. Finite row truncation leaves
only polynomial norm costs, which these tails absorb.

## Extracting the principal term

Write `H1=Z/X1=Z^(27/100)` and `H2=Z/X2=Z^(1/100)`. The four frequency
poles meet at `t1=t2=1/3`. We have the strict inequality `H1>H2^2` in
power scale, which makes an iterated extraction particularly simple.

After the w residue, shift t1 from z_plus to z_minus with t2 still at
z_plus. Cross `3t1=1` and `2t1+t2=1`; the pole `t1+2t2=1` lies to the
left of the new line and is not crossed in this step.

The remaining t1 integral saves `(27/100-1/100)epsilon` in power. The
skew-pole residue has `t1=(1-t2)/2` and saves
`(27/200-1/100)epsilon`. In the `3t1=1` residue, the three remaining
factors have a triple pole at `t2=1/3`. Moving t2 to z_minus saves
`(1/100)epsilon` in the remainder. After charging kappa, the three
positive margins are respectively

```
259/1000000, 124/1000000, 9/1000000.
```

Fixed logarithmic powers fit within a final frequency-error saving
`1/200000`. The normal box covers every residual line, including the skew
one. All scalar zeta arguments avoid their pole on the residual lines.

Consequently the principal contribution has the form

```
P_eta(Z) = sum_(j=0,1,2) (log Z)^j/(2*pi*i)
             * integral_(beta_*+kappa)
                 Z^(x-41/75) a_j,eta(x)/L^S(x,eta) dx
           + O_eta(Z^(beta_*-41/75-1/200000)).
```

The functions a_j are holomorphic in `Re(x)>5/6` and rapidly decreasing
on fixed vertical strips after polynomial factors. Let `c_S` be the
positive residue of `zeta_F^S` at one, and let `H_eta` denote the
principal correction at `t1=t2=1/3,w=1`, including its finite bad-prime
frequency factors. The top coefficient is

```
a_2,eta(x) = c_S^5/[3 zeta_F^S(2)] * (1-a2)^2 * M[B](1)
            * M[U_1](1/3) M[U_2](1/3) exp((x-5/6)^2)
            * L^S(3x-3/2,eta^3*conjugate(alpha)^3) H_eta(x).
```

It is nonzero throughout `Re(x)>5/6`. The Fourier Mellin values and
label value are nonzero by the chosen profiles. The angular L-factor is
in absolute convergence. Each good-prime principal numerator is the
positive combination

```
(1-D)(1+Q^(-1)) + (1-R)(F0-1),
```

whose real part is positive, and all finite excluded-prime factors are
positive. Normal convergence makes the resulting product nonzero.

## Why the logarithmic terms cannot cancel the target zero

Assume the direct estimate. The row and frequency errors just proved
then bound the displayed logarithmic Mellin sum by
`Z^(beta_*-41/75-1/200000)`. Its small-Z part decreases faster than
every power, by shifting the reciprocal coordinate to any fixed line
farther right. Mellin transformation therefore continues

```
G_eta(s) = sum_(j=0,1,2) (-1)^j (d/ds)^j [a_j,eta(s)/L^S(s,eta)]
```

holomorphically into `Re(s)>beta_*-1/200000`, within `Re(s)>5/6`.
At a zero of order m of the target, its j=2 term has a pole of order
m+2 with nonzero leading coefficient. The other two terms have poles
of order at most m+1, so they cannot cancel it. This contradicts the
definition of beta_* when beta_*>21/25. A principal pole of the original
L-function gives a zero of its reciprocal and causes no exception.

This proves the stated conditional implication. It does not prove its
direct-estimate hypothesis.

## The direct estimate is a genuine missing arithmetic gain

The coprime `n=1` sector after one Poisson transform contains a signed
correlation between a normalized long `mu*gamma_4*eta` source and a shorter
ordinary `gamma_2` source. Its physical row has norm length
`Z^(73/50)`, its remaining dual frequency has length `Z^(1/100)`, and
its outside factor is `Z^(-11/10)`.

In this sector an optimistic diagonal mean for each Gauss factor followed
by separate Cauchy bounds would give correlation power `147/100`, hence
probe power `37/100`. That corresponds to theta `11/12` at these chosen
scales. Reaching the unreserved target needs a signed-correlation saving
`23/300` over that comparison. This comparison assumes the diagonal means
are uniform in the required twists; it is not a claim that the full direct
bound with that power has been proved.

The canonical hypothesis concerns the entire original J, not just this
coprime sector. A proof must sum the short completion and overlap divisors,
retain the fixed target character, preserve separate profiles and all zeros,
and bound the surviving polar component. Existing bounds for a prescribed
pole-subtracted remainder or for an untwisted natural Gauss mean do not
automatically provide it.

`scripts/verify_cubic_contour_box.py` replays the rational identities,
all-size decay inequalities, error margins and power comparison. It does
not independently check the analytic continuation argument or establish
the direct estimate.
