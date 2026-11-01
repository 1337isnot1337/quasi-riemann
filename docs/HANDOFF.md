# Research handoff at the requested pause

Paused at the user's request on 2026-10-31. **No improved all-Dirichlet
zero-free bound was proved.** The confirmed tracker threshold remains
0.8733819666133; the open candidates approach 0.873381966613207519929...
The tracker main and PR heads 100--102 were refreshed at this pause and
still match `sources.lock.json`.

## What is concrete

- The inherited return-model contact has an exact obstruction. Retuning
  its existing parameters cannot supply the requested structural jump.
- The cubic route now has full completion and overlap accounting and a
  precisely normalized signed-correlation contract. Its required saving
  remains unproved; the 13/15 and 0.84 implications are conditional.
- The sextic Jacobi route has a written direct-side rapid-decay argument,
  exact local factorizations, and a complete finite-mean subtraction.
  The remaining all-modulus trace bound is open; 0.8 is conditional.
- [PR #8](https://github.com/1337isnot1337/quasi-riemann/pull/8) gives a
  written proof that the exact cubic Pell Picard factor is nonzero for
  real x>=2 and Re(s)>1/2. Using the imported Goldfeld--Hinkle theorems,
  this removes their extra possible poles from zeros of that factor.
  It does not identify the Pell series with the required trace.
- [PR #9](https://github.com/1337isnot1337/quasi-riemann/pull/9) derives
  a cubic Airy/Gauss representation of the squarefree Jacobi trace,
  including every frequency gcd. Its Mellin identity keeps the reciprocal
  L-factor visible. Non-squarefree branches and the full centered
  estimate remain open.

The last [Fourier-coupled prototype](../research/fourier-coupled-prototype.md)
is preserved as a scratch calculation. Its finite phase diagnostic passes,
including source/row overlaps. The complete physical identity, published
theorem mapping for arbitrary finite targets, and an independent direct
estimate are not certified. It is not another claimed improvement.

## Reproduce and interpretation

```sh
make verify PYTHON=/path/to/python-with-sympy
make sources PYTHON=/path/to/python-with-sympy
make diagnostics PYTHON=/path/to/python-with-sympy
```

The final tree has 15 exact research checkers and separately labeled
numerical diagnostics. Source verification covers 55 tracker files and
15 external downloads. The Airy checker includes 640 unit identities and
706 Gauss/overlap identities, including 64 composite cases. The optional
Picard quadrature diagnostic is
`python scripts/verify_picard_factor.py --numerical`.

The analytic arguments are written, not Lean formalized. Earlier scoped
Lean checks concern algebra and conditional transport; they do not prove
the missing estimates. No bound was submitted to the leaderboard.

## Exact stopping point

To resume the main goal, prove OPEN6o in
[the sextic Jacobi note](../research/sextic-jacobi-detector.md), or SC_sigma
in [the complete cubic correlation note](../research/cubic-signed-correlation-contract.md).
Any alternate operator must first preserve an explicit reciprocal signal
and supply an independent analytic bound for its complete physical sum.
The new special-function proof and finite transforms alone do neither.
