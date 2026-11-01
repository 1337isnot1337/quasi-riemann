# Sources and credit

The authoritative external objects at this checkpoint are:

- [Big O Speedrun quasi-Riemann page](https://bigospeedrun.com/other/quasi-riemann):
  the requested leaderboard and its distinction between claimed and human-verified results.
- [GTimG/QuasiRiemannTracker](https://github.com/GTimG/QuasiRiemannTracker):
  all-moduli Dirichlet target, exact proof sources, admission records and licenses.
- [Joseph Bebel's PR #99](https://github.com/GTimG/QuasiRiemannTracker/pull/99):
  reserve-parametric fourth-power seed, selected energy above one half, two finite
  source lines and the five-window physical return. This is the pinned leading
  admitted construction, with predecessors credited in its notices.
- [PR #100](https://github.com/GTimG/QuasiRiemannTracker/pull/100),
  [PR #101](https://github.com/GTimG/QuasiRiemannTracker/pull/101), and
  [PR #102](https://github.com/GTimG/QuasiRiemannTracker/pull/102):
  preexisting open refinements toward the same limiting contact. Their numbers
  and contact expression are prior work and are not claimed as new here.

Exact source pins and file hashes are in `sources.lock.json`. The principal
modules reconstructed in the research notes are:

| Module suffix in PR #99 | Role |
| --- | --- |
| `PR98Improvement/Return/Formulas.lean` | Counts, admissions, row exponents |
| `PR98Improvement/Return/Constants.lean` | Geometry and capacities |
| `PR98Improvement/Return/Tuning/Guards.lean` | Parametric source-face guards |
| `BoundaryPhysical/GenericScalar.lean` | Physical numerator and kernel exponents |
| `BoundaryPhysical/PhysicalDirect/PacketBound.lean` | Actual fourth-moment packet hypothesis |
| Baseline `Hecke/Primitive.lean` and `Hecke/DyadicReflection.lean` | Primitive functional equation and its explicit quotient factor |
| Baseline `Hecke/ReciprocalGrowth.lean` | Polynomial reciprocal growth above the inherited supremum |
| Baseline `Detector/GaussianMellin.lean` | Exact Gaussian profile, Mellin inversion and power bounds |
| Baseline `Hecke/Dyadic.lean` | Ordinary versus Möbius coefficient definitions |
| Baseline `Hecke/InverseAmplificationEndpoint.lean` | Ambient sextic lift and the 5/6 volume loss |
| Baseline `Hecke/InverseAmplificationRows.lean` | Sixth-free cores and injective sixth-power decomposition |
| Baseline `Hecke/InverseAmplificationMask.lean` | Prime deletion via the sixth mask |
| Baseline `Hecke/Operations.lean` | Product and inverse characters |
| Baseline `Hecke/DetectorFiberSpikes.lean` | Both spikes on one actual detector fibre |
| Collet `Record1252270103Return/CountFromMoments.lean` | Inverse and ordinary moment count inputs |
| Collet `Cycle25/Energy/Physical/CertifiedZero.lean` | Empty-slot ordinary pair moment for long lengths |
| Baseline `Eisenstein/CompactEnergyFamilies.lean` | Sextic local row character definition |
| Baseline `PrimeRows/Character.lean` | Actual numerator row and prime coefficients |
| Baseline `Hecke/InverseAmplificationFamily.lean` | Sixth-power row replication and its deletion mask |
| Baseline `Hecke/InverseAmplificationBudget.lean` | Origin of the no-slot 5/6 slope |
| Baseline `Detector/EulerCoordinates.lean` | Actual unramified Euler coordinates and phases |
| Baseline `Detector/HighEulerRational.lean` | Rational form of the complete local correction |
| Baseline `Detector/HighRowsUnramified.lean` | Unramified closed correction in actual rows |
| Baseline `Detector/CorrectionBounds.lean` | Original correction's convergence region |
| Baseline `Arithmetic/IdealMobius.lean` | Multiplicative angular phase on primary ideal generators |
| Baseline `PrimeRows/ActiveGaussFactorization.lean` | Normalized embedding defining the angular factor |
| Baseline `Hecke/DyadicReflection.lean` | Numerator functional equation, conductor and Gauss phase |
| Baseline `GaussSum/CubicNormalization.lean` | Cubic Gauss cube and primary angular normalization |
| Baseline `GaussSum/SexticNormalization.lean` | Actual ideal CRT and normalized Gauss identities |
| Baseline `Hecke/LogarithmicActual.lean` | Euler logarithm and primitive reciprocal strip estimate |
| Baseline `Hecke/Primitive.lean` | Primitive functional equation for conductor convexity |
| Baseline `Hecke/StripActual.lean` | Strip growth and its functional-equation input |
| Baseline `Hecke/ZeroSupremum.lean` | All-character zero supremum and uniform-margin principle |
| `BoundaryPhysical/PhysicalDirect/Hybrid.lean` | Two-ordinary-factor source budget |
| `BoundaryPhysical/PhysicalDirect/Geometry.lean` | Plain scale and shifted capacity |
| `BoundaryPhysical/TransportGeometry.lean` | Coarse box and floor constraints |
| `BoundaryPhysical/Schedule.lean` | Conductor switch restrictions |
| `BoundaryPhysical/Transport/TransportParameters.lean` | Positive loss budgets and constructors |
| `BoundaryPhysical/Transport/Transport/PrincipalRemainderRegion.lean` | Local Euler-factor transport estimates |
| `BoundaryPhysical/Transport/Transport/{NormalizedTransportSaving,NonfloorTransport,SharedNonfloor,HighApproximation}.lean` | Transport saving and propagation interfaces |
| `BoundaryPhysical/Transport/FinalFixedHigh.lean` | High-source approximation from a finite numerator bound |

The current proof builds on OpenAI, Hailey Collet, Sil, ArviFoxy, Joseph Bebel,
Jacob Sussman and other credited upstream contributors. This repository's new
contribution is the explicit source-general cap-dominance identity, the contour
cancellation and universal-h saddle obstruction in this model, and an auditable
analysis of the missing higher-moment input. The Euler audit additionally
extracts three scalar factors and proves local continuation near the functional
diagonal, with explicit row growth and retained poles. The contact value itself predates
this repository. No priority claim beyond these reconstructed arguments is made.

The scoped transport fork retains every inherited notice. Its exact nine-file
patch, fresh geometry admission and reproducible build driver are in
`formal-transport/`; it does not modify the pinned tracker checkout. The signed
cache is credited solely as an authenticated compilation cache, not as an
independent proof checker. The checked transport implications retain their
explicit finite numerator premise.

The [Jacobi detector](../research/jacobi-detector.md) uses the prime Jacobi
evaluation from OpenAI's September 30 TeX at commit `fd4aeeb2`, and explicitly
credits span_of_dilates's Paper 40 v5 for the observation that Jacobi sums
already carry a Mobius sign. Papers 13 v1 and 15 v1 are comparison sources;
neither estimates the required complete trace average across all moduli.
These four exact downloads are hash pinned in `external_files` and checked
by `make sources`. The finite-field Kummer calculation is derived in the
notes and checked by exact cyclotomic arithmetic. The cubic-input control
and sextic-input variant keep their different output character orders.

The newer cubic norm comparisons credit bramble_trace's Papers 70 v1 and
77 v1. Their exact downloaded Markdown hashes and versioned URLs are in the
external portion of `sources.lock.json`. The latter retains its stated
external zero-free hypothesis. Our separate-mean optimization grants missing
twist uniformities and proves no new analytic mean or zero-free theorem.
The same external lock pins the OpenAI paper's exact fd4aeeb TeX source used
for the derivative-profile stability argument and its original low estimates.
The shared-label probe definition is pinned at this repository's separate
297a7ef checkpoint. The full physical cube-ratio estimate uses its one-Poisson
normalization, elementary tame Gauss lifts and ideal counting; it imports no
new moment theorem. Its source text is included in the external hash lock.
The separate 9f30963 cubic high checkpoint is also hash pinned. The complete
signed-correlation contract imports its written analytic continuation, while
keeping the new direct estimate explicitly open.

The binary cubic probe also credits span_of_dilates,
[Structural ceilings, v5](https://rstation.ai/problems/riemann_hypothesis/papers/40),
for the previously suggested conjugate-dual Gauss configuration. The shared-label
kernel, completed overlap calculation and global representation are presented
as this repository's written derivation. Their exact local and unit checks do
not independently verify the analytic Poisson argument in a proof assistant.

The [Picard-factor proof](../research/picard-factor-nonvanishing.md) uses the
exact factor in Goldfeld--Hinkle, *The cubic Pell equation L-function*,
arXiv:2209.11874v3, p. 2. Its PDF is hash pinned. Their Theorems 1.1 and
1.3 supply the spectral continuation and growth in the stated corollary;
those theorems are imported, not independently verified here. The
hyperbolic differential equation and endpoint energy argument are derived
in the note. DLMF 14.12.4 provides the classical associated-Legendre
normalization check. The ratio-character support mismatch is checked
against Definition 3.2 and the conjugation against Definition 5.1 in the
rendered source. This auxiliary nonvanishing statement does not supply
the open quasi-Riemann trace estimate.

The [Airy/Gauss representation](../research/airy-jacobi-trace.md) credits
Duke--Iwaniec (1993) for the finite-field cubic exponential/Kloosterman
identity. It uses equation (7.4) of Friedberg--Offen, *On the cubic Shimura
lift to PGL(3): The fundamental lemma*, JEMS 28 (2026), as its pinned primary
comparison source; printed p. 1726 was rendered to check the constants and
character orientation. The present gcd extraction and squarefree Mellin
identity are written derivations. That paper supplies a local fundamental
lemma, not the required global trace bound. Its higher-conductor cubic
identity is not silently applied to the different prime-power branches of
the sextic Jacobi input.

The corrected-dispersion comparison uses OpenAI's first-moment TeX at commit
4eaee87548250b2682affda7d05d947c05554bae. Its paper, dispersion section and
exceptional-moment section are separately hash pinned. Their coefficient
classes and height averaging do not supply SC_sigma as currently stated.
