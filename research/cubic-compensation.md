# A compensated cubic lift for the long inverse detector

Status: exact coefficient algebra, a multiplicity lemma and an analytic input
contract. No improved inverse moment or L-function bound is established.

This changes the amplification map rather than retuning its parameters. It
targets the *Möbius inverse detector*. The final numerator's fourth moment
contains ordinary L-polynomials; these are separate objects.

## Where the inherited 5/6 comes from

In pinned OpenAI `Hecke/InverseAmplificationEndpoint.lean`, rows u of norm at
most U are lifted to `u*p^6`, for prime ideals of norm about V. The lifted rows
have norm at most U V^6. The raw inverse mean square is available once
D^(1+c) <= U V^6. There are V/log V amplifiers. Ignoring positive losses,
division by their count costs

```text
(U V^6)/V = U V^5.
V = (D/U)^(1/6) gives U^((1+5r)/6), when D=U^r and r>=1.
```

Thus the 5/6 in the long detector branch is an amplification-volume loss.
It need not be treated as an irreducible property of every sixth-free row
estimate, although improving it requires a new analytic input.

## The cubic coefficient identity

For each supported column ideal I, write rho_I(z) for its multiplicative
sextic row character, extended by zero on nonunits. Then

```text
rho_I(u*a^3) rho_I(a)^3
    = rho_I(u) rho_I(a)^6
    = rho_I(u) 1_(I coprime to a).
```

The compensating factor `rho_I(a)^3` is quadratic. For a prime amplifier a,
this is exactly the coefficient identity needed to delete its Euler factor.
The pointwise identity holds even on the zero-support cases. For a general
fixed character eta, multiply both sides by its column coefficient eta(I).

The uncompensated cubic lift fails: at a prime with sixth-character phase
rho(a)=exp(2 pi i/6), its cube is -1. This is why changing 6 to 3 in the old
proof is invalid. The compensator introduces a moving quadratic character.
The upstream `Character.product`, row-character completion and sixth-mask
identities supply the natural global definitions, but the resulting complete
Hecke construction has not been rebuilt here.

`lean/CubicCompensation.lean` verifies the finite phase identity, including
zero, and its consequence for every multiplicative map into these phases.
Lean 4.34.1 reports only the standard `propext` and `Quot.sound` axioms. This
is an algebra statement, not the analytic Hecke construction.
`scripts/verify_cubic_compensation.py` also replays it on finite
prime fields and checks the cost identities exactly.

## Collisions are a small cost

The original sixth lift is injective on sixth-free cores. A cubic lift of
those cores can collide. For a fixed image ideal J, a prime amplifier P must
satisfy v_P(J)>=3; after subtracting 3 at P, every valuation must be below 6.
For each P there is at most one remaining core ideal. Thus the number of
preimages is at most the number of prime divisors with valuation at least 3.
Their product of cubes divides J, so this number is at most
`log Norm(J)/(3 log 2)`. With a fixed generator for each amplifier ideal, the
element preimage is also determined. This logarithm is absorbed by an epsilon
loss. It does **not** remove the moving-character issue.

## The actual new estimate required

Let eta_P denote the quadratic compensator for the prime P. The relevant
graph family consists of pairs (u,P), evaluated at the row v=u*p^3, with
character `chi_v * eta_P` and the required smooth inverse-polynomial profiles.
Suppose a new joint estimate bounded its energy by

```text
sum_(u,P) |A_(u*p^3,eta_P)(D)|^2
    <= (U V^3) V^tau (U D V)^epsilon,
    D^(1+c) <= U V^3.
```

The exact Euler-factor removal and division by V/log V would yield, for r>=1,

```text
source exponent = 1 + (2+tau)(r-1)/3.
```

Consequently:

- tau=1 is the separate-family cost and gives exponent r, which loses.
- tau=1/2 reproduces the inherited exponent (1+5r)/6 exactly.
- **A strict gain requires tau<1/2.** A square-root saving in the moving-family
  variable alone merely recovers the existing result.
- tau=0 would replace the long-branch slope 5/6 by 2/3.

The old raw moment, even if uniform in the compensating character, cannot be
summed over primes for free. Nor can a bound for one fixed twisting character
be used when its conductor grows with V without proving its uniformity.
The new contract must handle the graph correlation, not an unrelated Cartesian
family of twists. Positive exponent fees, heights, both inverse profiles and
the rescaled D/Norm(P) column all remain to be included in a proof.

## Compensation also removes the apparent new oscillation

There is an important obstruction to a quick proof of the graph estimate.
For every column coprime to the amplifier, the combined phase is exactly
`rho_I(u)`, independent of P. Restricting the coefficient matrix to columns
coprime to all chosen amplifiers leaves identical rows in the amplifier
variable. That submatrix has rank one. In a prime field, with u=1, the sum
of these compensated phases over all nonzero amplifiers is p-1, not a
square-root-sized sum. The exact replay checks this as well.

Thus one cannot invoke quadratic-character cancellation in P after ignoring
its correlation with the cubic lift. That correlation cancels the quadratic
phase completely. The mixed graph theorem must obtain its saving from the
original arithmetic coefficients and the primitive u-average. The cubic
identity alone reorganizes the hard mean square; it does not establish a
new source estimate.

One way to see its strength is to keep U fixed large enough to contain u=1.
The compensated lifted polynomial is the original eta-twisted Möbius sum
with one Euler factor removed. With `D^(1+c) <= U V^3`, the hypothetical graph
bound, amplifier division and an arbitrarily small c would give

```text
sum mu(I) eta(I) W(Norm(I)/D) << D^((5+tau)/6+epsilon).
```

This would directly yield the zero-free threshold `(5+tau)/6`, subject to the
full uniform analytic theorem and the standard Mellin continuation argument.
In particular tau=0 would imply 5/6. This is a conditional implication, not a
claimed bound. It illustrates that the graph input already contains a deep
Möbius-cancellation assertion; treating it as free orthogonality would merely
hide the original problem.

## Why this is a research route rather than a new bound

The exact coefficient identity makes the changed map viable algebraically.
It exposes a concrete target for a joint quadratic/sextic mean-square theorem
and also proves why the compensator alone supplies no new cancellation.
The required saving beyond the square-root threshold is unproved, and may
require cancellation in the quadratic compensator together with sixth-free
support. The direct primitive-row inverse moment is a related alternative
which avoids introducing the compensator variable. Neither is established by
the current source estimates.
