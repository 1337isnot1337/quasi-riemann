# A centered cubic probe retains a constant reciprocal signal

Status: an exact principal-residue calculation and a new conditional direct
target. It does not prove the direct estimate or a zero-free region. It uses
the written high expansion of the separate
[0.84 cubic checkpoint](https://github.com/1337isnot1337/quasi-riemann/blob/9f309638642422757108c0690fb36b60f6810d69/research/cubic-direct-target-084.md),
which is not Lean formalized here.

## Three complete probes

Use the original radial shared-label probe J_eta, with the fixed profiles and
scales in that checkpoint. For a fixed positive kappa different from one, set

```text
Delta2 J = J_eta(kappa^2 X1,X2/kappa^2,Y,Z)
           -2 J_eta(kappa X1,X2/kappa,Y,Z)
           +J_eta(X1,X2,Y,Z).
```

All three copies retain their full completion, overlaps, target character and
zero masks. Their product X1*X2 is identical. The multiplier in the exact high
Mellin representation is

```text
(kappa^(t2-t1)-1)^2.
```

This is a fixed finite combination of the original probes, not a bound on a
selected pole-subtracted portion.

## The principal signal survives

The four frequency poles meet at t1=t2=1/3. Put u=t1-1/3, v=t2-1/3 and
l=log(kappa). Their local polar denominator, with the zeta residues removed, is

```text
9*u*v*(u+2v)*(2u+v).
```

The contrast multiplier has leading jet l^2*(v-u)^2. In the iterated extraction
used by the high checkpoint, an analytic coefficient H with value H0 at the
intersection therefore contributes

```text
Res_(v=0) Res_(u=0)
  l^2*(v-u)^2*H(u,v)/[9*u*v*(u+2v)*(2u+v)] = l^2*H0/18.
```

Higher jets of H cannot contribute: the contrast already consumes the full
available degree two. The residue is nonzero when H0 is nonzero.

Equivalently, the original top signal is C_eta(x)*(log Z-log X2)^2, times its
common power of Z. A constant aspect shift replaces log X2 by log X2-l. Its
second difference is exactly

```text
(log Z-log X2+2l)^2-2(log Z-log X2+l)^2+(log Z-log X2)^2 = 2l^2.
```

All terms of total logarithmic degree at most one vanish. Thus, using the
nonvanishing C_eta established in the cited high expansion, the contrast has
a constant principal reciprocal signal with coefficient
`2 log(kappa)^2 C_eta(x)`. It has no logarithmic loss of the target signal.
The common scale power remains Z^(x-41/75).

## The conditional target and the actual gap

Use X1=Z^(73/100), X2=Z^(99/100), Y=Z^(73/100). Fixed rescalings change constants,
not the strict exponent margins in the high errors. The same written high
argument would therefore give nonvanishing for Re(s)>21/25 if one proved

```text
|Delta2 J| <<_(eta,S,kappa) Z^(8797/30000).
```

The target lies 1/10000 below the principal exponent 22/75. For the contrast,
the resulting Mellin transform contains a nonzero holomorphic coefficient
times 1/L^S(s,eta), without the earlier logarithmic derivatives. A zero of the
target still produces a pole and gives the same continuation contradiction.
This is a conditional implication; the displayed direct estimate is open.

A constant or linear aspect-dependent bad polar component would cancel in
Delta2. That is a reason to test centered correlation estimates. It is not a
proof that the actual direct-side polar component has that form. Before using
any published centered or pole-subtracted estimate, identify its exact
coefficient, orientations, profiles, labels and polar subtraction with this
complete three-probe expression. No such source-to-consumer map is supplied
here, and no published estimate is being claimed to prove the target.

### The literal centered-source substitution fails

Write chi for the cubic symbol and G=gamma_2. Already on the coprime,
completion-free partial-transform branch, the two column phases are
`mu(c)*conjugate(G(c))*chi_c(m)` and `G(s)*conjugate(chi_s(m))`, with
additional common profiles, target twist and frequency factors. Their row
orientations are opposite. The same-product centering of
[Paper 58 v3, Section 10](https://rstation.ai/problems/riemann_hypothesis/papers/58/v3)
instead keeps one common G(n) and one common cubic orientation on the whole
convolution. Its two ordinary positions have a common height. Its inverse
positions do not have this probe's Gauss phases.

Even the Gauss phases alone do not join into its prescribed coefficient.
For coprime c,s, cubic Gauss multiplication gives exactly

```text
conjugate(G(c*s)) = conjugate(G(c))*conjugate(G(s))*chi_c(s),
mu(c)*conjugate(G(c))*G(s)
 = mu(c)*conjugate(G(c*s))*G(s)^2*conjugate(chi_c(s)).
```

The residual G(s)^2 is a prescribed nonordinary Gauss coefficient, and the
cross-character also remains. In addition, no single row power matches both
chi_c(m) and conjugate(chi_s(m)). These exact discrepancies rule out the
literal substitution into that centered theorem. They do not exclude a new
transform or a stronger theorem with this different coefficient class.

`scripts/verify_mellin_annihilator.py` checks the local iterated residue and the
finite-difference algebra exactly. It does not check the imported high
continuation or the unproved direct estimate.
