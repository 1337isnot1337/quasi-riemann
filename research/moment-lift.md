# What a higher numerator moment would actually need

Status: exact Holder accounting, a sharp finite black-box obstruction, and a
source-budget obstruction for direct product realization. No new analytic
estimate or L-function bound is proved.

## The actual current input

The pinned `PhysicalDirect/PacketBound.lean` assumes, for each normalized
dilation bin and every admissible coefficient choice,

```text
sum_i |S_i|^4 |Q_i|^2 <= Cmoment U^(1+epsilon).
```

Here S_i is the ordinary polynomial packet of the inverse character, Q_i is the selected
marked-prime product, and the same rows satisfy a cardinality bound U^R.
The selected lower bound is |Q_i| >= U^(q C), with q=delta*p and capacity C
measured in U units. Ignore epsilon and constant losses for the model below.
The packet estimate contributes

```text
(3R+1)/4 - q C/2.
```

It is essential to retain the selected factor and its power. The PR #93 sextic
norm and its later adapters concern a different selected-source object; the
source map does not supply an automatic sixth moment for this S_i packet.

## Correct accounting for a proposed m-th moment

If a new analytic theorem supplied

```text
sum_i |S_i|^m |Q_i|^2 <= U^T,
```

Holder would instead give the exponent

```text
(1-1/m)R + T/m - 2qC/m.
```

The count weight improves as m increases when R<1, but the selected-capacity
saving weakens from qC/2 to qC/3 for m=6. Keeping the original saving would
require changing the selected-factor power as well, and proving that input.

There is also an ordinary support cost. The existing physical source bounds
the squared product of two ordinary polynomials and one marked-prime product,
with budget n1+n2+Lambda*s <= B. Its plain length is n=1-y/d. Realizing a sixth
moment directly would replace two copies by three and require

```text
3n + Lambda*s <= B,
```

even assuming the needed three-factor analytic theorem existed. At the inherited
contact d=h*, the exact values are

```text
n* = (-1081 + 44 sqrt(1081))/855 = 0.42766881357201928994...
2n* = 0.85533762714403857988...
3n* = 1.28300644071605786982...
```

Thus B<=1 leaves no room for even the unmarked direct sixth product. This
invalidates that direct use of the existing source budget. It is not a proof
that a sixth-moment theorem exploiting arithmetic cancellation is impossible.

## A black-box promotion cannot help

The fourth moment and cardinality alone permit the extremal configuration

```text
number of rows = U^R,
Q_i = U^(qC),
|S_i| = U^((1-R)/4-qC/2),
```

with every row identical. The fourth bound is an equality. Any m-th moment
inferred from this information must allow the exponent

```text
Tsharp = m/4 + (1-m/4)R + (2-m/2)qC.
```

Substituting Tsharp into the correct Holder formula returns exactly
`(3R+1)/4-qC/2`. There is no gain. A literal example is U=64, four rows S_i=2,
and Q_i=1: the fourth moment is 64, the sixth is 256, and the fourth-moment
Holder inequality is sharp. The example is about arrays, not Hecke characters;
its purpose is to rule out deduction from the stated black-box data alone.

## Remaining structural approaches

A useful new theorem must exploit information absent from that extremizer:
actual ordinary numerator and Möbius inverse-detector coefficients, shared zero selection, incompatible heavy-row
events, or off-diagonal arithmetic cancellation. Plausible targets are:

1. A joint count/moment inequality on zero-selected rows, improving the product
   of row cardinality and weighted energy without separately bounding each.
2. A long reciprocal-polynomial sixth moment with a genuine saving over the
   direct three-factor support cost, uniform in the conductor and selected weights.
3. A factorization argument which handles the rough-ideal remainder as well as
   factorable ideals. Splitting only smooth ideals does not address prime ideals
   whose norms already exceed the proposed short-factor scale.

The exact conditional return certificate in `research/conditional-087.md`
quantifies a sufficient new row-count input. It is a target for these approaches,
not evidence that the new count is true. A complete result would also need the
analytic reconstruction, uniformity and positive loss budget checked.

The fixed-fibre analysis in [mixed-fibre.md](mixed-fibre.md) distinguishes the
two coefficient types and tests joint ordinary moments. Those moments still
saturate at the inherited crossing; a mixed inverse/numerator estimate is a
separate, explicitly quantified analytic target.
