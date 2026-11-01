# Quasi-Riemann bound research

Research toward a substantial improvement in the zero-free half-plane threshold
for all Dirichlet L-functions. This repository consolidates source pins,
structural arguments, reproducible experiments, and explicit proof gaps.

**No improved L-function bound is established here.** The initial result is an
exact obstruction for the inherited return/count model, including arbitrary
admissible capped branches and a variable Mellin contour. It explains why a
structural change is needed to pass the current cluster of candidates.

The active cubic route now has a written full-probe reduction to one precise
signed-correlation estimate. Small physical cubic cores are below budget, and
the completion and overlap terms have summable weights after exact Gauss-lift
expansion. A saving of 1/20 in the remaining correlation would give the
conditional threshold 13/15. That signed estimate remains unproved; the
arithmetic certificates and the stated sector bounds do not establish it.

The Big O Speedrun page lists `0.8733819666133` as its leading human-verified
threshold at the 2026-10-31 snapshot. Open tracker PRs #100, #101 and #102 approach
`0.873381966613207519929...`. These are external results, not this project's work.
The exact pinned sources and open-PR heads are in [sources.lock.json](sources.lock.json).

- [Current state and next proof obligation](docs/STATE.md)
- [Exact return-model obstruction](research/return-model-barrier.md)
- [Higher-moment route and its actual support cost](research/moment-lift.md)
- [A compensated cubic lift and its remaining amplifier cost](research/cubic-compensation.md)
- [Mixed detector/numerator moments and the missing inverse input](research/mixed-fibre.md)
- [A fixed primitive pole pairing and its remaining contour gap](research/primitive-pole-pairing.md)
- [Support of a long Möbius inverse factor](research/inverse-dominant-support.md)
- [Euler continuation to the functional diagonal](research/euler-diagonal-regularization.md)
- [Targeted comparison with recent analytic sources](research/literature-intake.md)
- [Exact conditional return target at 0.87](research/conditional-087.md)
- [Lean transport fork admitting the 0.87 geometry](formal-transport/README.md)
- [The shared-label cubic identity with all completion and overlap terms](research/shared-label-cubic-identity.md)
- [The complete direct estimate required by the radial 0.84 reduction](research/cubic-direct-target-084.md)
- [A fixed-product cubic contrast that preserves the reciprocal signal](research/cubic-aspect-contrast.md)
- [The signed-correlation gap after newer cubic Gauss norm estimates](research/cubic-signed-budget.md)
- [Small physical cubic cores below the 0.84 direct target](research/cubic-principal-ratio-sector.md)
- [The exact cubic row and conductor margin after overlap extraction](research/cubic-overlap-row-map.md)
- [A complete signed-correlation contract for conditional 13/15 and 0.84 thresholds](research/cubic-signed-correlation-contract.md)
- [An angular cubic-probe candidate and its changed signal](research/angular-cubic-probe.md)
- [A Jacobi detector with a proved direct bound and an open trace estimate](research/jacobi-detector.md)
- [A sextic Jacobi variant with a cubic trace and a conditional 0.8 target](research/sextic-jacobi-detector.md)
- [A written nonvanishing proof for the cubic Pell Picard factor and its remaining source-map gap](research/picard-factor-nonvanishing.md)
- [The classical cubic exponential-sum form and its retained Gauss weight](research/cubic-airy-trace.md)
- [Its global identity and a separating family of candidate residues](research/angular-signal-family.md)
- [A coupled derivative for the exposed diagonal pole](research/coupled-mellin-annihilator.md)
- [Physical differentiation and stability of the baseline low estimates](research/derivative-low-stability.md)
- [Source and credit map](docs/SOURCES.md)

The research target is a structural jump beyond all preexisting candidates.
`0.87` is an initial benchmark for proposed analytic improvements, not a claimed
bound. Another decimal retuning of the inherited return is out of scope.

## Reproduce

Python 3.11 or later and SymPy are sufficient for the symbolic checks:

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
make verify PYTHON=.venv/bin/python
make sources PYTHON=.venv/bin/python
```

`make verify` checks exact algebra and the explicitly labeled exponent models.
It does not build the upstream Lean proof or verify a new zero-free region.
`make diagnostics` separately runs the numerical finite-Fourier checks, including
the sixteen two-prime source/label configurations and 128 one-Poisson overlap
cases. The optional `make verify-lean`
checks the compensated-cubic character identity with Lean 4.34.1 and Std only;
it proves no analytic amplifier estimate.
The 0.87 certificate assumes an explicitly unproved stronger count, and covers
the whole exponent-model domain by 27 exact rational Bernstein leaves. The
separate [transport replay](formal-transport/README.md) checks a broadened generic
high-transport assembly over 3,078 Lean modules, with 2,923 compatible modules
from the authenticated upstream cache. Its exact 0.87 geometry and the three
transport statements audited use only the standard Lean axioms. The stronger
count and complete nonvanishing reconstruction remain unproved.
The mixed-fibre replay proves that the ideal two-ordinary-factor source still
saturates when detector and numerator are coupled. It quantifies a different,
unproved mixed estimate involving the Möbius inverse detector. It also clarifies
that the numerator itself has ordinary character coefficients.
`make sources` downloads only pinned public source files into ignored `.sources/`
and checks their SHA-256 hashes. No entire upstream tree is vendored.

New material is Apache-2.0. Upstream work remains credited to its authors and
retains its original licenses. See [NOTICE](NOTICE).
