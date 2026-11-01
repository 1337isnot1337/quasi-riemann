# Fourier-coupled prototype preserved at the pause

Status: an experimental phase calculation, not a bound or a completed
source-to-consumer proof. Research was paused at the user's request. The
existing analytic obligations in `docs/STATE.md` remain open.

The purpose is to change the physical operator so that its partial Fourier
transform has the same Gauss orientation in both columns. The earlier probe
has opposite orientations and cannot be identified with the signed Kubota
remainder merely by applying a norm theorem.

Use the self-dual Eisenstein additive character and cubic symbol kappa of
the other notes. Write G(c)=gamma_2(c). For squarefree coprime c,s and a
nonzero row m, put c'=c/(c,m), using the squarefree gcd. The finite phase
calculation is

```text
[G(c)^2*bar(alpha(c))/G(c')]*kappa_c'(m)*kappa_c(s)
 *g_(kappa_c'*bar(kappa_s))(c'*s,m)/sqrt(Nc'*Ns)
 =mu(c)*bar(G(c))*bar(G(s))*kappa_s(c*m).              (A)
```

Here g is the actual additive Gauss sum for the displayed product
character, including its zeros. Gauss multiplicativity and cubic
reciprocity give the normalized product
`G(c')*bar(G(s))*bar(kappa_c'(m))*kappa_s(m)`.
The row is a unit at c', so its c' characters cancel. Then
`G(c)^2*bar(alpha(c))=mu(c)*bar(G(c))` gives (A).
This also retains rows sharing primes with c: it is c', not c, in the
character and Gauss modulus on the left.

The proposed physical realization inserts the bilinear phase
`e(m*n/(c'*s))` into the second lattice sum. A bandlimited radial Fourier
profile, with X2 larger than the supported source norm, should force its
Fourier frequency to equal m. The physical source multiplier would be

```text
sqrt(Nc'/X2)*G(c)^2*bar(alpha(c))/G(c'),
```

with first factor kappa_c'(m), cross factor kappa_c(s), and label weight
`u(s)*Ns^(-1/6)`. At the phase level, (A) then gives a sum with outer
`mu(c)*bar(G(c))` and inner conjugate cubic Gauss sum with numerator c*m.
This is closer to a conjugate signed Kubota remainder than the old probe.

The matched Euler weight u, complete polar subtraction, additive-character
conventions, and any fixed target twist still need a complete source map.
In particular, a theorem with its prescribed untwisted outer coefficient
does not automatically apply to every finite eta(c). Even an exact
realization of that remainder would leave the independent bound for the
new complete physical probe to prove. No new numerical threshold is
attached to this prototype.

`python3 scripts/check_coupled_fourier.py` reproduces 36 numerical phase
checks in actual Eisenstein residue rings, including 11 source/row overlap
cases. The observed maximum absolute error is below 1e-10. This is a
normalization diagnostic, not a certificate for the proposed global
Poisson identity or an analytic estimate.
