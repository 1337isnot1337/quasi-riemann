# Mixed moments on the actual detector fibre

Status: exact exponent-model obstruction for one fixed fibre and a new analytic
input contract. No new moment estimate or L-function theorem is proved.
Replay: `scripts/verify_mixed_fibre.py`.

## The two coefficient types must be distinguished

In upstream `Hecke/Dyadic.lean`, `polynomial chi false` has coefficients
`idealCoeff chi I`, whereas `polynomial chi true` multiplies those coefficients
by the ideal Möbius function. The numerator in `PhysicalDirect/Hybrid.lean` is
`polynomial (rowCharacter ...).inverse false`: the character is inverted, but
the Boolean is **false**. It is an ordinary polynomial of the inverse character,
not a Möbius polynomial. Earlier references here to reciprocal numerator
coefficients should be read with this distinction.

The detector has both coefficient types. `Hecke/DetectorFiberSpikes.lean`
provides, on a common witness fibre and ignoring positive losses,

```text
|I_i| >= U^(delta*r/2),     I: Möbius inverse detector,
|P_i| >= U^(delta*m/2),     P: ordinary detector,
r+m approximately t,      q=delta*p.
```

The real parts and frequencies in these polynomials come from the zero witness.
The numerator packet S has its own profile and frequency. Any analytic mixed
estimate must handle that difference uniformly. A polynomial convolution at
one common shift does not automatically apply.

## Why coupling the two ordinary polynomials alone does not help

Grant the optimistic source at B=1, Lambda=2, and even grant full profile and
row-frequency uniformity for a proposed mixed use. More generally write B,
Lambda and assume all the following capacities are positive and uncapped:

```text
s_P  = (B-2m)/Lambda,
s_S  = (B-2n)/Lambda,
s_PS = (B-m-n)/Lambda.
```

The separate ordinary detector count is

```text
R_P = 1-2*delta*m-2*q*s_P.
```

An inherited count R and the numerator fourth moment give a packet exponent

```text
F4 = (3R+1)/4-q*s_S/2.
```

A joint energy `sum |S_i P_i Q_i|^2 <= U` and the lower bound for P instead give

```text
FPS = (R+1-delta*m)/2-q*s_PS.
FPS-F4 = (R_P-R)/4.
```

Thus where R <= R_P, this mixed ordinary estimate cannot improve F4. At the
plain-count crossing it gives exactly the same answer. This identity includes
the extra selected width in the mixed product; omitting that width would give
the wrong comparison.

## A simultaneous extremizer, including every mixed ordinary pair

Put

```text
a(l) = (1-R-2qB/Lambda)/4+(q/Lambda)*l.
```

For a row set of size U^R and identical magnitudes U^a(l), every pair obeys

```text
R+2a(l1)+2a(l2)+2q*s
 = 1+(2q/Lambda)*(l1+l2+Lambda*s-B).
```

Consequently **every** source moment with budget
`l1+l2+Lambda*s <= B` holds simultaneously. If R=R_P, the detector spike
`a(m)=delta*m/2` and the desired numerator Hölder estimate both saturate.
Arbitrary nonnegative combinations and Hölder interpolations of these moment
bounds cannot exclude this array.

For the ideal B=1, Lambda=2 source, extend this construction to all nonnegative
lengths by replacing a(l) with

```text
min(a(l), l/2, (1-R)/4).
```

This preserves the budgeted bounds, enforces the trivial pointwise bound, and
also enforces every empty-slot two-polynomial bound, including long lengths.
At the two lengths below the minimum leaves a(l) unchanged.

A fully rational simultaneous witness is

```text
delta=3/7, p=1/2, t=26/23, r=52/69, m=26/69,
R=201/322, n=3/7, q=3/14,
|P|=U^(13/161), |I|=U^(26/161), |S|=U^(389/4508).
```

It also saturates the marked inverse second moment at width `(1-r)/2`.
Taking U to be a sufficiently divisible integer power makes U^R an integer;
the array is literal, although it is not a family of arithmetic characters.
The replay checks the same identities at the exact inherited radical contact.

The scope is one common detector fibre. This is not a proof that every possible
use of the detector, across all cutoffs or arithmetic identities, is obstructed.

## A mixed inverse estimate would add different information

A genuinely new theorem could bound, on the same rows,

```text
sum_i |S_i|^2 |I_i|^2 |Q_i|^2 <= U^(T+epsilon),
|I_i| >= U^(delta*r/2),  |Q_i| >= U^(q*s).
```

It would give the packet sum exponent

```text
FI = (R+T-delta*r)/2-q*s.
```

It improves the inherited fourth bound precisely when

```text
T < (R+1)/2+delta*r-q*s_S+2q*s.
```

At the inherited contact and s=0 the right-hand side is approximately
**1.1186541994** (the exact value is in `results/mixed-fibre.json`). The ordinary
numerator length plus inverse detector length is about **1.1805258013**.
This is a different target from pretending a unit-cost sixth moment exists:
it asks for a correlation estimate for the actual ordinary and Möbius factors.
No such estimate follows from the separate source moments above.

The coefficient identity `mu * 1 = identity` suggests testing complete scale
reconstruction before absolute values. It does not give cancellation for a
single pair of dyadic annuli, or for two unrelated shifts. A valid next step
must either preserve that reconstruction and its shifts, or prove a mixed
arithmetic estimate directly. Profile, conductor, height, amplitude-bin and
mesh uniformity remain required, as do positive loss budgets and a global
return certificate before any threshold can be claimed.
