# A signed-correlation contract for the complete cubic contrast

Status: a written reduction of the full physical direct estimate to one
explicit uniform signed correlation. It includes every completion, overlap
and imprimitive lift. The correlation estimate itself is open. The final
zero-free implications also import the separate written high argument at
[9f30963](https://github.com/1337isnot1337/quasi-riemann/blob/9f309638642422757108c0690fb36b60f6810d69/research/cubic-direct-target-084.md),
which is not Lean formalized here. No improved bound is claimed.

Use X1=Y=Z^(73/100), X2=Z^(99/100), and the fixed contrast

```text
Delta J = J(4X1,X2/4)-2J(2X1,X2/2)+J(X1,X2).
```

Its high principal coefficient is the nonzero constant
`2*(log 2)^2*C_eta(x)`, by [cubic-aspect-contrast.md](cubic-aspect-contrast.md).

## The precise correlation

Use g,a,b,n,v and the real lifts from
[cubic-overlap-row-map.md](cubic-overlap-row-map.md). In particular
v|rad(g*n), l=g^2*n^3/v and h=l*k. Set

```text
C=Z/(q_g*q_n^3), B=Y/q_g, M=Y*X1, H=Z/X2, K=H/q_l.
```

Write B0 for the fixed label profile. The common four-variable profile is

```text
F(ra,rb,rm,rk)
 =ra^(-1/2)*V(ra)*B0(rb)*W1(rm/rb)*U2(rk/ra),
F_delta(ra,rb,rm,rk)
 =(1/4)*F(ra,rb,rm/4,rk/4)
   -F(ra,rb,rm/2,rk/2)+F(ra,rb,rm,rk).
```

The factors 1/4,-1,1 include the outside scale normalization of each
original probe. These are fixed joint profiles, common to all rows and
arithmetic tuples. They are never chosen separately for one row.

Let chi_a be the cubic symbol, with its literal zero extension. Define

```text
K_(a,b)(m,k;g,v)
 =chi_a(v*m)*conjugate(chi_a(g*k))
  *conjugate(chi_b(v*m))*chi_b(g*k).
```

On its nonzero support its row Kummer class is v*m/(g*k). The displayed
product defines it even when a character argument is a nonunit.

For a cutoff rho>0, let C_(g,n,v)(Z;rho) be

```text
sum_(a,b squarefree, (a,b)=1, (a*b,g*v)=1)
  mu(a)*eta(a)*gamma_4(a)*gamma_2(b)/sqrt(q_a*q_b)
  *sum_(m,k nonzero, (m,g*n)=1,
        N(core_3(v*m/(g^2*k)))>Z^rho)
     K_(a,b)(m,k;g,v)
     *F_delta(q_a/C,q_b/B,q_m/M,q_k/K).
```

The cutoff is the original geometric class m/h: the omitted n^3 is a
cube. It must stay in this form in a signed estimate. The column
coprimality condition also remains. Dropping either condition by positivity
would be an invalid inference for this signed sum.

## The open uniform estimate

For a fixed sigma>0, the sufficient hypothesis is, for every epsilon>0,

```text
|C_(g,n,v)(Z;rho)| <<_(eta,S,epsilon) M*max(1,K)*Z^(-sigma+epsilon).
                                                        (SC_sigma)
```

The constant must be uniform in g,n,v in the retained range
`q_l<=H*Z^epsilon`. It may depend on the fixed joint profiles and target.
The actual Mobius/Gauss coefficients, all zeros, fixed target eta, specified
core cutoff and shared m mask are required hypotheses. This is not a
claim for arbitrary bounded coefficients or arbitrary row selections.

The usual Gaussian/Schwartz truncation restricts to this range with an
arbitrary-power error, after smaller preliminary losses are chosen. There
g*n^2|l, so all the short-index and column-separation bounds of the overlap
note apply. The extracted primitive conductor is at least
`Z^(rho/2-1/100-O(epsilon))` on the core-cut sum.

## Why no completion power is lost

After the exact overlap identity and lift expansion, the coefficient of
this correlation is, apart from unit-modulus target and angular factors,

```text
sqrt(X2/X1)/Y
 *mu(g)*mu(v)*q_l/[q_g^(5/2)*q_n^4*sqrt(C)].
```

The extra ra^(-1/2) in F accounts exactly for converting 1/q_a to the
normalized 1/sqrt(q_a). Since

```text
1/[q_g^(5/2)*q_n^4*sqrt(C)]
 =Z^(-1/2)*q_g^(-2)*q_n^(-5/2),
q_l*K=H,
```

the lift size cancels against the shorter k range in (SC_sigma).
When K<1, the retained range gives max(1,K)<=K*Z^epsilon.
The remaining absolute scalar sum converges:

```text
sum_(g squarefree,n good) q_g^(-2)*q_n^(-5/2)
                          *#divisors(rad(g*n)) < infinity.
```

Its Euler factors are 1+O(q^(-2)+q^(-5/2)). Triangle over these summable
scalars preserves the signed cancellation inside each correlation. Hence

```text
|Delta J_(large core)| << Z^epsilon*sqrt(Z*X1/X2)*Z^(-sigma)
                       = Z^(37/100-sigma+epsilon).
```

The [small-core bound](cubic-principal-ratio-sector.md) contributes
`Z^(79/300+2*rho/3+epsilon)`. Thus (SC_sigma) yields the complete contrast
bound, including all original terms,

```text
|Delta J| << Z^(max(37/100-sigma,79/300+2*rho/3)+epsilon).
```

## Two exact benchmarks

| Signed saving sigma | Removed cores through Z^rho | Remaining good conductor | Full direct power | Conditional zero-free threshold |
| --- | --- | --- | --- | --- |
| 1/20 | rho=2/25 | Z^(3/100-O(epsilon)) | 8/25 | 13/15 |
| 2/25 | rho=1/25 | Z^(1/100-O(epsilon)) | 29/100 | 21/25 |

For the first row, the small-core power is 19/60, below 8/25 by 1/300.
Adding the high signal's 41/75 normalization to 8/25 gives 13/15.
The imported high box is valid above 21/25, so it covers this threshold.
For the second row, the direct power 29/100 lies below the reserved 0.84
target 8797/30000 by 97/30000. The earlier high argument therefore applies.
The constants of the correlation may depend on each fixed target; its
exponent and sigma must be as stated for every target.

Both conclusions are conditional. No published theorem has been shown to
prove (SC_sigma) for this complete correlation. The exact checker verifies
the normalization, support, convergent-weight exponents and table arithmetic;
it does not prove the signed saving or the imported analytic continuation.

## Two source-to-consumer controls

A diagonal asymptotic for the long Mobius/Gauss norm alone does not bound
this covariance. The positive Gram matrix `[[1,1],[1,1]]` has both diagonal
quadratic forms exactly one, zero error for either diagonal test, and cross
term one. Thus even two exact diagonal statements permit the full Cauchy
cross term. This is a black-box countermodel, not an assertion about actual
Hecke characters. Subtracting the known diagonal error exponent from a
cross-correlation bound would require an additional theorem.

The corrected-dispersion proposition in OpenAI's
[first-moment source at 4eaee875](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/dispersion.tex)
is a positive Gauss norm at one column scale. Its fixed-height corrected
version requires roughness and Siegel--Walfisz cancellation; above its 0.40
column fraction it also requires independent prime convolutions. Its
explicit power improvement is averaged over large norm heights. Neither
statement supplies this fixed-profile unequal-column signed covariance.
The source's exceptional-character moments retain their prime-convolution
class as well. Any decomposition of the present coefficients must prove
those hypotheses and keep the original masks before importing that gain.
