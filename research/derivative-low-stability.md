# The coupled derivative retains the original low estimates

Status: a written analytic implication of the pinned paper's reflection and
energy lemmas. The Gaussian derivative and the single-term differentiation
are checked in Lean. The infinite physical-probe identity and low estimates
are not formalized here. This gives no exponent saving or new zero-free bound.

Use the [OpenAI paper at fd4aeeb](https://raw.githubusercontent.com/openai/math/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
specifically `prop:completed-reflection`, `lem:unmarked-completed-moment`,
`eq:low-separated`, `prop:balanced-low`, `lem:probe-row-norm` and
`prop:probe-low`. These source results are imported, rather than independently
proved by this note.

## Physical identity on independent scales

Write I[W0,W1,V] for its physical probe after Mellin inversion. Its scale
normalization is X^(-1/2)Y^(-1), and its three profile arguments are

```text
q_m/(q_b*q_s*X), q_s/Y, q_(c*n^3)/Z.
```

Every arithmetic coefficient and zero mask is independent of the three
scales. In the compensated probe, first regard the slot scales P_i and
their prime windows as independent external data. All finite prime
rescalings are constants during the differentiation. With E=r*d/dr and
D=X*d/dX+Y*d/dY+Z*d/dZ+1/2, termwise differentiation gives

```text
D I[W0,W1,V] = -I[W0,W1,V] - I[E W0,W1,V]
               - I[W0,E W1,V] - I[W0,W1,E V].
```

This identity holds for the complete compensated finite sum as well.
Only afterwards set the slots to their prescribed powers of Z.

Here is a convergence justification. Restrict the independent scales to a
compact neighborhood of a positive triple. The annular s,m supports then
lie in one finite set. The completed c,n sum converges locally uniformly,
together with each fixed scale derivative, because V and its Euler
derivatives have arbitrarily large power decay at zero and infinity.
Coefficient majorants and ideal counting give a summable bound after fixing
a sufficiently large decay order. The same argument applies to every
marked summand; the external prime set is finite. Smooth compact supports
introduce no boundary terms. These facts justify differentiating the
physical expression before reimposing the geometry.

For the Gaussian `G(y)=C*exp(-(log y)^2/4)`, the exact chain rule is
`-E G=(log y/2)*G=:G_log`. Thus this is precisely the four-term identity
in [coupled-mellin-annihilator.md](coupled-mellin-annihilator.md).
The Lean single-term check uses common logarithmic dilation: its normalization
is exp(-3t/2), each profile argument is multiplied by exp(-t), and adding
half the undifferentiated term gives the four coefficients above.

## The new profile has every required seminorm

Put u=log y. For each j>=0,

```text
E^j G_log(y) = C*P_j(u)*exp(-u^2/4),
P_0(u)=u/2, P_(j+1)(u)=P_j'(u)-(u/2)*P_j(u).
```

Induction proves this formula, with P_j a polynomial of degree j+1. For
each fixed power A and each j, multiplication by y^A or y^(-A) still
leaves a polynomial times a Gaussian with a bounded translation. It is
bounded and integrable in log y. Therefore G_log satisfies every profile
hypothesis of `prop:completed-reflection`, with finite weighted Mellin
seminorms. Integration by parts also gives the exact transform
`M[G_log](t)=t*exp(t^2)` in the paper's normalization.

For the compensated row lemma, its joint annular profile w_(k,J) changes
by the explicit factor

```text
(k+log x-sum_i log rho_i)/2.
```

All variables except k lie in fixed compact logarithmic boxes. Every
fixed profile seminorm is consequently bounded by C_j*(1+|k|) times a
finite set of the original Gaussian seminorms. The factor 1+|k| is
absorbed by increasing the exponential annular weight by any fixed
positive amount. Both weighted annular summability and arbitrary-power
tail estimates in `lem:probe-row-norm` remain valid. The common profile
still precedes all arithmetic row and tuple sums. No moving profile is
selected for an individual row.

## The two low estimates

For the balanced unmarked probe, the paper's completed-row lemma now
applies to G_log and gives the same Z^(1+epsilon) squared row norm. The
additive factor is unchanged. Replacing W0 or W1 by its Euler derivative
also preserves its compact support, finite Mellin/Fourier norms and
coefficient-mass estimate. The Cauchy calculation in `prop:balanced-low`
therefore gives, for each of the four terms,

```text
|I_term(Z^(1/2),Z^(1/2),Z)| << Z^(1/4+epsilon).
```

In the original compensated geometry, the preceding joint-profile argument
gives exactly the same marked-row norm as `lem:probe-row-norm`. The additive
Gram proof accepts complex annular profiles through homogeneous derivative
norms and squared coefficient masses. Euler derivatives of W0,W1 therefore
leave its exponents unchanged. The tuple factor remains
`d-3d/2-d/2=-d<=0`. Repeating `prop:probe-low` proves for each term

```text
|I_modified,term(Z)| << Z^(3/16+epsilon).
```

The triangle inequality over four terms proves these same estimates for
D I and D I_modified. Positivity of a differentiated profile is unnecessary
in either norm argument. Where an initial statement chooses nonnegative
annular weights, a real compactly supported smooth test can alternatively
be written as the difference of two nonnegative smooth tests by adding a
sufficiently large fixed bump. This extends the bilinear probe by finite
linearity, with fixed constants.

These are the original paper's geometries and exponents. This proof does
not supply the stronger selected count for 0.87, the full refined physical
return, a coherent infinite row continuation, or a new power saving. The
coupled multiplier's value at the old principal signal is x; that local
nonvanishing calculation is separate from those unresolved steps.
