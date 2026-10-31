# The generic low-side budget for the shared-label cubic probe

Status: an optimistic exponent-model obstruction for one Cauchy argument. This
is not a bound for the full new probe. The construction belongs to the separate
[shared-label checkpoint](https://github.com/1337isnot1337/quasi-riemann/blob/297a7efac59ea6f8f801b027d3f4f03872716a68/research/shared-label-cubic-identity.md).
The cubic phase configuration and global representation are not new claims here.

Consider its short second-dual regime X2=Z^(1-epsilon). First audit the favorable
coprime branch with completion n=1, and grant free summation of the short second
frequency h. These grants only help this proposed estimate. Write

```text
X1=Z^a, Y=Z^b, M=Y*X1.
```

One cubic Poisson transformation on the second physical average contributes
`sqrt(X2/Nc)*gamma_2(c)*gamma_4(s)`. Combining with the source and its compensator
uses `gamma_2(c)^3=mu(c)*alpha(c)` and `gamma_4(s)=conjugate(gamma_2(s))`.
Ignoring unit phases of absolute value one, the two column families for a
Cauchy split in m have coefficients

```text
c column: mu(c)*eta(c)*conjugate(gamma_2(c))/Nc,   Nc~Z,
s column: gamma_2(s)/sqrt(Ns),                    Ns~Y.
```

The remaining prefactor is `sqrt(X2/X1)/Y`, and the m range has norm M.
Thus the squared coefficient norms are O(Z^(-1)) and O(1), respectively.
This bookkeeping retains the square-root normalization of each physical
average and the original source factor 1/sqrt(Nc).

For the purpose of testing the generic Cauchy route, grant the cubic comparator

```text
Psi3(R,C)=R+C+(R*C)^(2/3)
```

on all relevant m rows, including common masks and profile separation at no
power cost. A squarefree-row theorem by itself does not justify this extension;
it is an additional optimistic grant in this model. The resulting Cauchy bound
would have exponent

```text
L(a,b) = (1-a)/2-b
       + (1/2) max(b+a,b,2(2b+a)/3)
       + (1/2) [max(b+a,1,2(b+a+1)/3)-1].
```

Both mixed terms occur in the two generic comparators. Consequently, for every
a,b, without any optimization or grid argument,

```text
L(a,b) >= -a/2-b + (2b+a)/3 + (b+a+1)/3
        = 1/3+a/6.
```

The candidate signal in the shared-label construction is
`Z^(theta-5/6)*(X1*X2)^(1/6)`, giving exponent
`theta-2/3+a/6+O(epsilon)` in this regime. Hence

```text
L(a,b) - signal(theta,a) >= 1-theta+O(epsilon).
```

At theta=0.87 the missing low-side saving is at least 0.13, before charging
completion, overlaps, dual-frequency summation or other loss budgets. Merely
changing the character order to three and inserting two generic cubic sieve
bounds cannot establish a nontrivial threshold by this route.

This does not rule out the changed probe. The actual c column has the coupled
Möbius/Gauss coefficient shown above. A bound exploiting it, a different joint
estimate before Cauchy, or a different scale regime could change this budget.
The calculation identifies the size of the needed improvement; it supplies no
such arithmetic cancellation estimate.
