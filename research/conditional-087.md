# A full-domain exponent target at theta = 0.87

**Conditional model result only.** The row-count improvement below is unproved.
This note does not assert Dirichlet nonvanishing at 0.87. It gives an exact,
global test for a proposed new analytic estimate, rather than another retuning
at the inherited contact.

## Explicit new input

Let V=5/6-delta and

```text
J = V(3-3p) + delta(1-p)(2-2p).
```

The new input would bound the actual zero-selected, amplitude-binned row count
by `U^(R_new+epsilon)`, with

```text
R_new <= 1-delta + (2/5) V delta (1-p)^2 / J
```

uniformly for 0<=delta<=3/4, 0<=p<=1/2. This removes three fifths of the
correction to 1-delta in the ideal inherited count. It is a saving in the
**exponent**, not a constant factor in the number of rows.

The real object is the canonical source count with error in pinned
`PhysicalDirect/PublicCount.lean`: delta=2a-1, p=q/delta, U=Z^d, and the rows
are simultaneously detector-zero selected and sorted by prime-slot amplitudes.
The proposed estimate must retain its conductor, character, height, mesh,
coefficient, bin and error uniformity. An estimate on arbitrary unrelated rows,
or on a different selected source norm, would not establish this contract.

## Exact geometry and certificate

Take

```text
theta=87/100, c=13/100, h=391/500,
ell=14/75, x=607/1500, y=613/1500,
kappa=37/50, conductor switch=7/10, numerator cap=3/40, reserve=1/10000.
```

These satisfy the basic signal geometry, including ell<x<y<1/2,
2x-y-ell>0, and the negative tuple exponent. The central floor-source exponent
has more than the stated reserve at d=h+10^(-22).

Use the inherited old count on d in [0,7/10], with capacity
`min(d,2y-d)/(6kappa)`. On d in [7/10,h], use the proposed improved count and capacity

```text
C(d) = min(3d/40, (2y-d)/2).
```

The row exponent has exactly the inherited fourth-moment form

```text
E(d,C,delta,p) = 1/2+13h/75-y/2-ell/2-9d/100
                +delta/2+delta*p*(ell-C/2)+3d R/4.
```

After multiplying by the positive count denominator, the six polynomials in
`results/conditional-087.json` certify the denominators and these four endpoints:

1. Old interval, d=0.
2. Old interval, d=7/10, C=(2y-7/10)/(6kappa).
3. New interval, d=7/10, C=3(7/10)/40. The old count is a conservative upper bound here.
4. New interval, d=h, C=(2y-h)/2, using the **unproved** improved count.

Every endpoint has E <= 0.87-0.0001 on the entire density/amplitude rectangle.
On each interval the exponent is the maximum of two affine functions of d,
hence is convex. Endpoint bounds therefore cover both full conductor intervals.
The switch is above 2/3, retaining the d>1/2 requirement of the source-selection
lemmas while extending the inherited schedule's stronger d>3/4 restriction.

The proof certificate uses rational Bernstein coefficients on a partition of
the rectangle. There are 27 leaves total across the six polynomials; the
conditional top polynomial uses 7. The weakest certified Bernstein lower bound
for that numerator is 2501/2560000. These are exact rational bounds, not a grid
scan. A replay also checks that retaining half of the count correction is
insufficient at the explicit witness delta=11/20, p=1/2 for these constants.

Run `scripts/verify_conditional_rows.py` to regenerate and compare every leaf
against the stored certificate. `--write` deliberately regenerates the receipt.

## Additional gaps before an L-function theorem

Besides the unproved count estimate, this remains an ideal-source model.
The following work is not supplied by the polynomial certificate:

- Realize a source face at B<1, Lambda>2 with all positive fees, inside the
  rational margin. Its existence at the required parameters must be proved.
- Complete the downstream use of the broadened transport. The original
  `BoundsN` fails at these constants. The [nine-module fork](../formal-transport/README.md)
  now admits the exact geometry and checks the generic high-transport assembly.
  It lowers the small-saving cutoff to 6/125 and the geometric loss allowance
  to 1/25; the actual small-saving quantity is 3659/75000, about 0.0487867.
  The final count/reconstruction/feedback chain is still unchecked here.
- Rebuild the physical reconstruction, old/small/central/tail contributions,
  actual-supremum feedback, and the Hecke-to-Dirichlet transfer with no additional
  analytic premises. Admit the final proof through the independent verifiers.

The current analytic bottleneck is the count contract. The downstream exact
calculation is now concrete and reproducible if a route to it is found.
