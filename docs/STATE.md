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
   Six polynomials, certified with 27 rational Bernstein leaves, replay exactly,
   using conductor switch 7/10. The new count is unproved. The transport fork
   below admits the geometry; the original transport box does not.
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

8. The fork in `formal-transport/` broadens the transport box and tightens its
   geometric loss allowance. The generic high-transport assembly and the exact
   0.87 geometry compile in Lean 4.34.1 over a 3,078-module source closure.
   Of these, 2,923 matched the authenticated upstream cache; the remainder were
   compiled locally. Six audited declarations use only propext, Classical.choice
   and Quot.sound. The assembly remains conditional on its finite numerator input;
   this does not supply the unproved count or a new nonvanishing theorem.

9. The sextic principal-phase Euler projection of the full inverse/plain
   ratio cancels at identical twists. With independent twists its leading term
   is `(x1-y1)*(x2-y2)`, positive in the conjugate energy case. Removing four
   explicit zeta factors leaves a degree-four residual. Thus even this simpler
   Euler model retains a double pole at generic small fixed twist differences;
   same-shift cancellation is not uniform cancellation of the actual mean.
   The exact local identity is in `research/mixed-fibre.md`.

10. Using the published primitive sextic residue Type-I input, inherited 7/8
    nonvanishing saves on its actual Möbius main term. The two squared fixed
    pole-pairing exponents at the contact are 0.9321362872... and 0.9436340498...,
    both below 1. The general contour pairing still costs 1.1805258013...,
    exceeding the mixed target by 0.0618716019.... The external theorem has not
    been independently verified here; the full row space, growing labels and
    prime weights remain open. See `research/primitive-pole-pairing.md`.

The exact certificates and scoped Lean compilation are reproducible. No new
L-function theorem or independent-kernel replay is claimed. See
`results/transport-087-lean.json` and `results/transport-087-axioms.txt`.

## Active route

Trace the actual weighted packet estimate
`sum |S_i|^4 |Q_i|^2 <= U^(1+epsilon)` and seek a stronger joint moment for the
ordinary numerator, Möbius inverse detector and zero-selected rows. A sixth-moment replacement
must address three ordinary factors, rather than the two admitted by the existing
global source. At the inherited saddle the plain length is about 0.4277, making
the three-factor support exceed the source budget even with no marked slots.

The immediate transport obstacle is now closed through the generic high assembly,
with the full reconstruction and transfer still unchecked at the new constants.
The next task is a new joint count/moment argument on the actual rows in
`PhysicalDirect/PublicCount.lean`. The quantified target and downstream gap list
are in `research/conditional-087.md`. An alternative is a new off-diagonal or
factorization estimate for the long reciprocal polynomial, with conductor,
shifts, selected weights, uniformity, and loss budgets explicit. A generic change
of Holder exponent is insufficient.

A narrower analytic target is now the coefficient-sensitive regular primitive
Kubota pairing for the actual Möbius/plain convolution. The fixed primitive pole
pairing is below the unit contact budget using the imported Type-I theorem;
its continuous remainder and the complementary Gauss row space are not.
The pole calculation does not provide growing-label or selected-weight
uniformity, so those remain part of any source-to-physical-return argument.

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
