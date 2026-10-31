# Research state

Updated: 2026-10-31. This is a research checkpoint, not a bound submission.

## Objective and baseline

Obtain a substantial unconditional improvement beyond all existing numbers and
candidates for the all-Dirichlet zero-free half-plane. The first structural
benchmark is theta = 0.87. It is not established.

Pinned tracker main: `fc2f46afbfda62351055d3c12fcacd4f6916cc63`.
Published leading threshold: 0.8733819666133 (PR #99).
Open PR #102 proposes 0.87338196661320751993; #100 and #101 also approach the
same contact. See the source lock for exact heads and rational bounds.

## Results

1. The inherited top-conductor exponent is independent of the Mellin contour
   real part when d = h. Changing that contour alone cannot cross its contact.
2. For any face 0<B<=1, Lambda>1 and Lambda>=2B, an admitted capped branch cannot improve
   the corresponding uncapped branch. The latter is dominated by the optimistic
   face B = 1, Lambda = 2. An exact identity proves this, with explicit signs.
3. At p = 1/2 and delta = (61 - sqrt(1081))/66, the optimistic uncapped return
   fails for every h once theta < (777 - sqrt(1081))/852. The saddle is at
   delta = 0.42608235688564859..., not at 3/8. The open PR #102 description's
   3/8 names a cover boundary; it is not the stationary point of these formulas.
4. A higher numerator moment offers a possible structural improvement, but the
   current fourth-moment input does not imply it at the same cost. Its support
   and selected-factor powers must be charged explicitly.
5. An exact conditional exponent certificate reaches theta=0.87 with reserve
   1/10000 over the entire density/amplitude domain and both conductor intervals,
   if a new count retains only 2/5 of the inherited correction to 1-delta.
   Six polynomials, certified with 12 rational Bernstein leaves, replay exactly.
   The new count is unproved, and the inherited transport box does not apply.
6. Joint ordinary-detector/numerator moments do not beat the inherited fourth
   bound on a fixed common fibre: the difference is exactly `(R_P-R)/4`.
   One abstract array simultaneously saturates all ideal budgeted ordinary
   pair moments and the relevant inverse second moment. A different mixed
   inverse/numerator energy would improve the contact if its unmarked exponent
   is below 1.11865419936482..., at total raw support 1.18052580125085....
   The new mixed energy is unproved. See `research/mixed-fibre.md`.
7. The actual inverse detector has squarefree ideal support. For any k>=2,
   writing its product with an ordinary ideal as a*b^k forces b^(k-1) to
   divide the ordinary ideal. At the contact the sixth-power-free core has
   exponent at least 0.6673232250.... This support fact is proved; a resulting
   analytic energy saving is not. See `research/inverse-dominant-support.md`.
8. A proposed two-transform cubic probe has an exact good-prime kernel retaining
   every cube-completion valuation and Ramanujan boundary. Its candidate target
   reciprocal survives locally above 5/6. The same scalar poles occur for other
   fixed rows, so the unmarked kernel does not isolate the principal row.
   A shared squarefree cubic label with an inverse squared Gauss compensator
   restores a good-prime ordinary selector on the same cubic row. Its CRT
   phases cancel for all valuations, including source/label overlaps. The global
   Poisson identity now has a written derivation, with exact local and unit checks.
   Its frequencies are divisible by `n^2*gcd(c,s)`, so a long second average
   forces short completion and overlap indices. The direct bound, continued row
   estimate and final principal asymptotic remain open. See
   `research/shared-label-cubic-identity.md`; no zero-free theorem is claimed.

These are model results, arithmetic identities and proof-obligation analysis. No new L-function theorem
and no independent replay of the upstream Lean dependency closure are claimed.

## Active route

Trace the actual weighted packet estimate
`sum |S_i|^4 |Q_i|^2 <= U^(1+epsilon)` and seek a stronger joint moment for the
ordinary numerator, Möbius inverse detector and zero-selected rows. A sixth-moment replacement
must address three ordinary factors, rather than the two admitted by the existing
global source. At the inherited saddle the plain length is about 0.4277, making
the three-factor support exceed the source budget even with no marked slots.

The next task is a new joint count/moment argument on the actual rows in
`PhysicalDirect/PublicCount.lean`. The quantified target and downstream gap list
are in `research/conditional-087.md`. An alternative is a new off-diagonal or
factorization estimate for the long reciprocal polynomial, with conductor,
shifts, selected weights, uniformity, and loss budgets explicit. A generic change
of Holder exponent is insufficient.

The immediate alternative is to examine the detector's complete inverse/plain
scale reconstruction before taking absolute values. A single dyadic mixed
ordinary product cannot help; a mixed inverse product would need arithmetic
cancellation, and its two shifts cannot be silently identified.

The actual row homomorphism is sextic. Recent cubic mixed-moment papers are
comparison sources and need a family reduction before use. The coefficient
support audit now retains the long squarefree inverse position under sixth-power
extraction. A new fixed profile with one vanishing Mellin moment does not remove
the polar term uniformly under independent norm twists.

## Parked routes

- Smaller positive source gaps/reserves: open PRs already exhaust this approach.
- More count windows or larger caps using the same face class: dominated by the
  exact model barrier above.
- Moving the Mellin line alone: cancels at the obstructing top scale.
- Replacing the fourth moment with a unit-cost sixth moment without proving it:
  omits the extra ordinary-factor support and changes the marked-factor saving.
- Pairing the numerator with the ordinary detector on one fibre, using only
  the same ideal pair source: the exact mixed-moment identity and simultaneous
  extremizer give no gain. A new inverse coupling or cross-cutoff input is needed.

Reopen a parked route only with a changed analytic estimate or a failure in the
stated model assumptions. Keep exact verification and the source map current.
