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
2. For any face B <= 1 and Lambda >= 2, an admitted capped branch cannot improve
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
7. A cubic lift admits an exact quadratic compensator which restores the
   prime-deletion mask. The phase-character lemma is checked in Lean 4.34.1
   with standard axioms only. The new graph-family moment would give source
   exponent `1+(2+tau)(r-1)/3`; a strict gain over sextic amplification requires
   `tau<1/2`. Its analytic bound is unproved. See `research/cubic-compensation.md`.

These are model results, an algebraic character lemma and proof-obligation
analysis. No new L-function theorem and no independent replay of the upstream
Lean dependency closure are claimed.

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

The inverse detector also has a distinct amplification bottleneck: extending its
raw moment uses the full ambient range of `u*p^6`. Investigate a direct long
moment on sixth-free cores or the compensated cubic graph family. The cubic
algebra is valid, but averaging its moving quadratic characters must save
strictly more than a square root relative to the separate-family cost.

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
