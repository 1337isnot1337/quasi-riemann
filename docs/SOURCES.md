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
| Baseline `Hecke/InverseAmplificationEndpoint.lean` | Raw moment to amplified inverse mean |
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
analysis of the missing higher-moment input. The contact value itself predates
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
note and checked by exact cyclotomic arithmetic, without importing a
cubic-character theorem for its sextic twist.

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
