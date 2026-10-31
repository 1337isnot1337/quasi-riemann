# Quasi-Riemann bound research

Research toward a substantial improvement in the zero-free half-plane threshold
for all Dirichlet L-functions. This repository consolidates source pins,
structural arguments, reproducible experiments, and explicit proof gaps.

**No improved L-function bound is established here.** The initial result is an
exact obstruction for the inherited return/count model, including arbitrary
admissible capped branches and a variable Mellin contour. It explains why a
structural change is needed to pass the current cluster of candidates.

The Big O Speedrun page lists `0.8733819666133` as its leading human-verified
threshold at the 2026-10-31 snapshot. Open tracker PRs #100, #101 and #102 approach
`0.873381966613207519929...`. These are external results, not this project's work.
The exact pinned sources and open-PR heads are in [sources.lock.json](sources.lock.json).

- [Current state and next proof obligation](docs/STATE.md)
- [Exact return-model obstruction](research/return-model-barrier.md)
- [Higher-moment route and its actual support cost](research/moment-lift.md)
- [Mixed detector/numerator moments and the missing inverse input](research/mixed-fibre.md)
- [Support of a long Möbius inverse factor](research/inverse-dominant-support.md)
- [A cubic probe with a shared ordinary selector](research/shared-label-cubic-identity.md)
- [The cubic probe's unproved direct target for 0.84](research/cubic-direct-target-084.md)
- [Targeted comparison with recent analytic sources](research/literature-intake.md)
- [Exact conditional return target at 0.87](research/conditional-087.md)
- [Source and credit map](docs/SOURCES.md)

The research target is a structural jump beyond all preexisting candidates.
`0.87` is an initial benchmark for proposed analytic improvements, not a claimed
bound. The changed cubic probe has a separate 0.84 target conditional on a
complete, unproved direct estimate. Another decimal retuning of the inherited
return is out of scope.

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
The 0.87 certificate assumes an explicitly unproved stronger count, and covers
the whole exponent-model domain by exact rational Bernstein bounds.
The mixed-fibre replay proves that the ideal two-ordinary-factor source still
saturates when detector and numerator are coupled. It quantifies a different,
unproved mixed estimate involving the Möbius inverse detector. It also clarifies
that the numerator itself has ordinary character coefficients.
The changed cubic probe has exact local and unit checks and a written global
Poisson identity. Its direct estimate and final zero-free argument remain open.
`make diagnostics` separately checks its normalization by direct finite Fourier
sums; that numerical check is not a proof of the analytic identity.
`make sources` downloads only pinned public source files into ignored `.sources/`
and checks their SHA-256 hashes. No entire upstream tree is vendored.

New material is Apache-2.0. Upstream work remains credited to its authors and
retains its original licenses. See [NOTICE](NOTICE).
