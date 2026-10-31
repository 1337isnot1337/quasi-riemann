# Retain the support of a long inverse factor

Status: an elementary ideal-support lemma and a route to investigate, not a
mixed moment estimate. The finite replay uses labelled primes, including two
distinct primes with the same norm. No improvement to an L-function bound is
claimed.

Let d be a squarefree ideal from the actual Möbius inverse polynomial and e
an arbitrary ideal from the ordinary numerator. For an integer k>=2 write uniquely

```text
d*e = a*b^k,   a k-th-power-free.
```

Then **b^(k-1) divides e**. To see this, at each prime write the valuation of e
as kt+j with 0<=j<k, and the valuation of d as epsilon in {0,1}. The valuation
of b is `t+floor((j+epsilon)/k)`. Subtracting k-1 times this valuation from the
valuation of e gives either t+j or, when j=k-1 and epsilon=1, t. Every case is
nonnegative. Thus this is an all-size valuation argument; the finite replay is
a supplementary check.

It follows that

```text
N(b) <= N(e)^(1/(k-1)),
N(a) >= N(d)/N(e)^(1/(k-1)).
```

In particular a pure k-th-power product would require `N(e) >= N(d)^(k-1)`.
This is sharp at d=p, e=p^(k-1). Squarefreeness of the inverse ideal is essential:
d=p^2, e=p^(k-2) is a counterexample without it. Ideal labels must be retained;
squarefreeness of a rational norm is a different property.

At the inherited contact the inverse length is r=0.7528569877... and the
ordinary length is n=0.4276688136.... The source's actual row homomorphism is
**sextic**, as defined by baseline `Eisenstein/CompactEnergyFamilies.lean` and
used in `PrimeRows/Character.lean`. Its sixth-power-free product core has
length at least r-n/5=0.6673232250..., up to fixed annular constants; the
sixth-root part has length at most n/5=0.0855337627.... There is no pure
sixth-power column. For a cubic sector the corresponding figures are
r-n/2=0.5390225809... and n/2=0.2138344068.... Independent Mellin shifts change
coefficients but do not change either support statement. A cubic character
estimate needs a reduction before it can apply to the general sextic rows.

This does not remove the generic large-sieve mixed term. Such terms are
present even for power-free columns. The next task is to retain the *single
long squarefree inverse position* through the reciprocal/source argument,
rather than replace its convolution by an arbitrary mixed coefficient or
infer a saving just from absence of cubes. The needed energy exponent at this
contact is below 1.1186541994, as derived in [mixed-fibre.md](mixed-fibre.md).
The estimate must also handle the actual detector labels, deletions, profiles
and independent row shifts before it can be used in the return.

Replay: `scripts/verify_inverse_support.py`. The local residue argument covers
all valuations; finite three-prime configurations for orders two through six and two negative controls
are retained in `results/inverse-support.json`.

The baseline no-slot exponent `max(1,(1+5r)/6)` comes from a different
use of sixth powers. `InverseAmplificationFamily.lean` replicates a row at
u*p^6, preserving its character with the prime deletion retained.
`InverseAmplificationEndpoint.lean` inflates the row scale to U*X^6, averages
over about X primes, and therefore pays U*X^5. This gives the slope 5/6.
Multiplication by a cube does not generally preserve the sextic character:
its remaining factor is quadratic. A lower-degree replication needs a new
argument, rather than a replacement of the number six in this calculation.
