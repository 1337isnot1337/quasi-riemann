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
   compiled locally. Nine audited declarations use only propext, Classical.choice
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

11. A candidate coupled Euler derivative has exact Mellin multiplier x+w-1.
    It removes the exposed diagonal scalar pole while multiplying the original
    principal signal by x. Its four profile terms are explicit, and Lean proves
    arbitrary-power tail bounds for the new logarithmic Gaussian term. The
    atomic chain rule is Lean checked as well. A written profile argument
    justifies physical differentiation and retains the original paper's balanced
    and compensated low exponents. The refined selected low estimate and
    coherent row-sum saving remain unproved. It changes no conductor exponent by
    itself. See `research/coupled-mellin-annihilator.md` and
    `research/derivative-low-stability.md`.

12. An optimistic low-side audit of the separate shared-label cubic probe
    shows that two generic cubic sieve bounds followed by Cauchy leave exponent
    gap at least 1-theta in the short-second-dual regime. Thus theta=0.87 needs
    at least 0.13 saving from its actual Gauss/Möbius coefficients or a different
    joint argument. This is a model limit for that Cauchy route, not a lower
    bound for the physical probe. See `research/binary-cubic-low-budget.md`.

13. An angular variant of the shared-label cubic probe has physical orders
    (2,-4), source order 1 and label compensator order 2. Its partial Gauss
    column matches the published j=2 cubic mean; the radial probe instead has
    the excluded j=0 mode. Only the pole 2*t1+t2=1 remains untwisted, with
    coupled scales X2^2=Z*X1. The order and scale identities are certified;
    the initial note does not prove a global identity or estimate. Result 22
    below supplies the absolute-line identity and fixed-row signal family;
    the full asymptotic and frequency estimates remain open.
    See `research/angular-cubic-probe.md`.

14. A second fixed-product aspect difference of the radial cubic probe has
    multiplier `(kappa^(t2-t1)-1)^2`. It removes both logarithmic signal powers
    but retains a nonzero constant reciprocal signal. The local iterated residue
    is certified. The complete contrast direct bound at exponent 8797/30000
    would give the separate 0.84 reduction; that bound and its identification
    with any published centered source estimate are unproved. See
    `research/cubic-aspect-contrast.md`.

15. Even granting the newer cubic Mobius/Gauss norm all required target and
    second-frequency twists, separate Cauchy estimates have limiting threshold
    49/54. The exact envelope argument quantifies a further signed saving
    101/2700 for 0.87 or 91/1350 for 0.84. At the fixed 0.84 high geometry the
    reserved saving is 2303/30000. These are model gaps; no such cancellation is
    proved. The literal substitution into Paper 58's centered theorem also
    fails its coefficient and row-orientation conditions. See
    `research/cubic-signed-budget.md` and `research/cubic-aspect-contrast.md`.

16. A written elementary estimate bounds the full physical cube-ratio sector
    of the cubic probe at Z^(79/300) in the fixed 0.84 geometry. It retains
    every completion and source/label overlap through a uniform imprimitive
    Gauss bound. The margin below the reserved direct target is 299/10000.
    The direct problem can therefore be restricted to the complementary
    physical ratios. This is a bound for a sector, not for the whole probe;
    the high principal frequency product is a different condition. See
    `research/cubic-principal-ratio-sector.md`.
    The same counting argument now covers every physical cubic core of norm
    at most Z^(1/25), at total power 29/100+epsilon. Its margin below the
    reserved target is 97/30000. The Kummer characters attached to the remaining
    geometric ratios have conductors above Z^(1/50). The exact overlap phase
    changes the row to g*m/h, where g=gcd(c,s) divides h. Its primitive
    conductor remains above Z^(1/100-epsilon) after the usual truncation.
    Real lift factors and all zero masks remain; no external norm estimate
    has been mapped to this signed sum. See `research/cubic-overlap-row-map.md`.

17. Expanding the real lifts before applying a signed estimate cancels each
    lift size against its shorter frequency range. The remaining scalar weights
    are g^(-2)*n^(-5/2), summable even after divisor choices. Thus one explicit
    common-profile correlation contract SC_sigma controls the complete cubic
    contrast with no extra completion exponent. Sigma=1/20 would give physical
    power 8/25 and the conditional threshold 13/15; sigma=2/25 would give power
    29/100 and the conditional 0.84 threshold. Neither signed estimate is proved.
    The imported high argument remains a written proof. See
    `research/cubic-signed-correlation-contract.md`.

18. A one-variable Jacobi detector replaces the Gauss source by ordinary
    character coefficients, over all good ideals. Its full physical sum has
    arbitrary-power decay for X=Z^a, a<1/2, by ordinary lattice Poisson.
    Its zero Fourier frequency retains 1/L(x,eta), with an explicitly nonzero
    coefficient for Re(x)>5/6. The remaining trace is a sextic Kloosterman
    trace, as checked in 107 exact finite-field cases. Bounding its complete
    nonzero-frequency sum by Z^(399/10000) at X=Z^(2/5) would give 0.84;
    that estimate is open. See `research/jacobi-detector.md`.

19. Using a sextic Jacobi character instead makes the output Kloosterman
    character cubic. On squarefree sources its dressed coefficient is exactly
    mu(c)*eta(c)*gamma_4(c). The all-prime-power signal correction converges
    and is nonzero for Re(x)>3/4, with local numerator bound 107/252.
    The same direct-side decay holds. A subpower bound for the complete
    nonzero-frequency sum at X=Z^(2/5) would give 0.8, but is unproved. The fixed-modulus
    cubic theorem does not establish this varying-modulus correlation.
    Its exact complete frequency mean can be removed with arbitrary-power
    error, retaining all prime powers; the remaining covariance is unproved.
    A positive local resolvent proves nonvanishing for Re(x)>1/2, and three
    further inverse Euler factors give a normally convergent nonzero correction
    there. A lower zero-supremum bootstrap requires an unproved trace estimate
    over an explicitly enlarged angular family.
    See `research/sextic-jacobi-detector.md`.
    The squarefree unit-frequency trace also has a classical cubic
    exponential-sum representation. Its moving Gauss coefficient and
    diagonal restriction remain, so existing unweighted or bilinear
    estimates do not imply the required cancellation. Two sets of 107
    exact finite-field checks support this map; see
    `research/cubic-airy-trace.md`.

20. The compensated cubic lift has an exact character identity, checked in
    Std Lean 4.34.1. Its compensated phase matrix has rank one, so an ordinary
    graph lift does not supply the required amplifier cost below one half.
    The analytic graph moment is open. See `research/cubic-compensation.md`.

21. Three scalar Euler extractions continue the inherited correction across
    a neighborhood of x+w=1, with explicit retained poles and ramified-row
    growth. The remaining product is normally convergent there; no infinite
    signed row-sum continuation or saving follows. The exact certificate is
    in `research/euler-diagonal-regularization.md`.

22. The radial shared-label cubic identity is derived on absolute lines with
    all unit classes, completion valuations and source/label overlaps. Its
    written conditional 0.84 reduction closes the stated high contour budget,
    assuming the complete direct estimate Z^(8797/30000). That direct estimate
    is open. See `research/shared-label-cubic-identity.md` and
    `research/cubic-direct-target-084.md`; neither analytic argument is Lean
    formalized. The exact kernel checks and numerical diagnostics are separate.

23. The angular variant's absolute-line identity has unit multiplier omega^r
    and completion character alpha^3. Its principal local numerator is bounded
    away from zero by 1647/7840 for Re(x)>5/6. Rational fixed scale ratios in
    [1,2] separate every possible target zero there by Mellin uniqueness.
    The full row-sum asymptotic and direct estimate remain open. See
    `research/angular-signal-family.md`.

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

The shared-label cubic construction is a separate structural route. The new
angular variant matches a coefficient-specific cubic mean while changing the
frequency-pole geometry. Its absolute-line identity and fixed-row signal
family are derived; the full asymptotic and frequency bounds need proof.
The radial low-budget note rules out the simpler generic Cauchy route in the
short-second-dual regime.
For the radial 0.84 direct target, all physical cubic cores through Z^(1/25)
are below budget by absolute values. The unresolved signed estimate is the
remaining geometric ratio classes, whose attached Kummer conductors exceed
Z^(1/50). The verified overlap extraction retains a Z^(1/100-epsilon)
primitive-conductor margin. A further transform must retain the original
profiles, target, real lifts and masks and verify additional parameter changes.
For this radial route, the full correlation contract SC_(1/20), with the explicit joint contrast
profile and original core cutoff, is the narrower next target. It includes
all completions and overlaps through summable weights; proving only the
completion-free coprime case would not establish that contract.

The preferred Jacobi variant has a proved direct-side rapid-decay argument
and an exact centered cubic Kloosterman kernel on squarefree sources. Its
remaining input is the full mean-zero trace average (OPEN6o) in
`research/sextic-jacobi-detector.md`, at squared frequencies and varying
moduli. The complete finite frequency mean is removed with arbitrary-power
error. The current fixed-modulus short-window theorem does not meet the
remaining contract, and every prime power stays in the source.

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
