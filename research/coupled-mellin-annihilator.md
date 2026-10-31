# A coupled multiplier removes the diagonal pole

Status: an exact candidate-probe identity. It does not improve the return
exponent, bound a coherent row sum, or establish nonvanishing. The physical
probe and its low estimate have not been reassembled for this modification.

The source is OpenAI's [pinned high Mellin identity](https://raw.githubusercontent.com/openai/math/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
`eq:probe-poisson-identity` and `eq:compensated-poisson-identity`. Its scale factor is

```text
X^(1/2-z) Z^(x+z-1) Y^(w-1).
```

Treat X,Y,Z as independent scales. Every selected-prime slot scale P_i is held
fixed during differentiation, before eventually substituting P_i=Z^(ell_i).
Define E_X=X*d/dX, and similarly E_Y,E_Z. The operator

```text
D = E_X+E_Y+E_Z+1/2
```

multiplies the high Mellin integrand by

```text
(1/2-z)+(w-1)+(x+z-1)+1/2 = x+w-1.
```

Differentiation under the absolute starting integrals is justified by the
fixed smooth annular profiles and rapid vertical decay. This gives an exact
identity for D applied to the original physical probe. It is not the total
derivative of the one-variable expression obtained after imposing the geometry.
That derivative would also differentiate the slot scales and has a different
multiplier.

## The known pole and the signal

The correction extraction in the separate [coherent-log checkpoint](https://github.com/1337isnot1337/quasi-riemann/blob/bd4ba73c25fb11994b1888d157960a8c7dd0fc6b/research/euler-diagonal-regularization.md)
is

```text
H_eta,u = L^S(6x+6z-4,psi_eta)
          L^S(x+w,eta)/L^S(x+w+6z-1,eta) * K3_eta,u.
```

It was proved there at the local Euler-product level, without controlling the
infinite u sum. For a principal target eta, the exposed L^S(x+w,eta) has its
simple pole on x+w=1. Multiplication by x+w-1 removes that polar divisor.
It does not remove independent divisors from either reciprocal L-function.
For nonprincipal eta this scalar factor has no pole at one.

The original principal signal takes w=1 and z=1/6. On that locus the new
multiplier equals x. Thus the operation preserves the formal reciprocal signal
with an additional holomorphic factor x, nonzero throughout Re(x)>869/1000.
This is why a coupled derivative differs from demanding that one fixed
profile's Mellin transform vanish at every norm-twisted pole height.

## Required integration checks

Euler derivatives replace the physical profiles by fixed derivatives and add
a polynomial Mellin weight. These have the expected support and decay classes,
but that observation is not a completed low-bound proof. In particular:

- Construct the signed combination within the actual selected physical probe,
  with one common excluded set and the slot scales held fixed as above.
- Re-establish the low estimate and the nonzero signal normalization. Existing
  positivity arguments for individual profiles cannot simply be reused for a
  signed derivative without proof.
- Control the coherent row sum and every other crossed polar divisor. Rowwise
  Euler continuation does not justify summing or moving its row series.
- Exhibit an exponent saving beyond the inherited model barrier. A fixed
  polynomial Mellin multiplier alone changes no length or conductor exponent.

Replay the exact multiplier and signal identities using
`scripts/verify_mellin_annihilator.py`. Its receipt explicitly leaves these
integration and analytic steps unproved.
