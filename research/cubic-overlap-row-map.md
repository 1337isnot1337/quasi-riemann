# The cubic row after overlap extraction

Status: a written exact phase identity for the complete one-Poisson cubic
probe and a conductor-support consequence. It retains completion and overlap
variables. It supplies no signed correlation estimate or zero-free theorem.
The finite phase and valuation bookkeeping is checked by
`scripts/verify_cubic_signed_budget.py`; the character identities and analytic
truncation are not formalized in Lean.

The opt-in numerical diagnostic `make diagnostics` also evaluates the
one-Poisson identity directly in Eisenstein quotient rings at norms 7 and
13. Its 128 cases include both Ramanujan boundary and full-divisibility
overlap lifts, with maximum relative error 1.77e-14. This supports the row
normalization separately from the exact symbolic bookkeeping; it is not
an exact arithmetic proof or an analytic estimate.

Use the radial probe, additive convention and Gauss identities of the
[shared-label checkpoint](https://github.com/1337isnot1337/quasi-riemann/blob/297a7efac59ea6f8f801b027d3f4f03872716a68/research/shared-label-cubic-identity.md).
Write chi for the cubic symbol, so G=gamma_2 and gamma_4=conjugate(G).
All ideals are good primary ideals. The finite bad-prime/unit packets are
retained in the same fixed S data.

## 1. Separate the actual overlap

Put

```text
c=g*a, s=g*b, g=gcd(c,s), f=a*b, d=g^2*n^3.
```

Here g,a,b are squarefree and pairwise coprime. The completion n may share
primes with any of them. The second physical character, on modulus f*d,
is induced from the primitive cubic character

```text
phi_f = chi_a * conjugate(chi_b),
```

with its extra nonunit zeros at g*n. The first physical factor has the
same character and retains the mask `(m,f*d)=1`.

## 2. Induction of the Gauss sum, with every lift

Let E be the radical of d with primes dividing f removed. For v|E set
l=d/v. On the support where `v_p(h)=v_p(d)` at every p|f, define

```text
Lambda_(f,d)(h) = sum_(v|E, l=d/v divides h) mu(v)*N(l).
```

Off that support the Gauss sum is zero. On it, d/h is a unit at f and
the exact induced Gauss formula is

```text
g_(phi_f, induced to f*d)(h)
 =g_(phi_f)(1) * phi_f(d/h) * Lambda_(f,d)(h).
```

To derive it, expand the extra zero mask as `sum_(v|(x,E)) mu(v)` in the
finite Gauss sum, then set x=v*y. The y sum on modulus f*l vanishes
unless l|h, in which case it is
`N(l)*g_(phi_f)(1)*conjugate(phi_f(h/l))`.
Its extra factor phi_f(v) makes the combined character phi_f(d/h),
independent of v. These are finite equalities. If h/l is not a unit at f,
that summand is zero; since v is prime to f this gives exactly the support
condition already stated.

At each prime, the exponent of l=d/v is at least
`2*v_p(n)+v_p(g)`. If p divides f, v has exponent zero; otherwise it has
exponent at most one. Hence every nonzero lift forces `g*n^2|h`. This
does not require g to be disjoint from n. In particular g|h.

## 3. The surviving row class is g*m/h

Cubic reciprocity gives

```text
g_(phi_f)(1)=sqrt(Nf)*G(a)*gamma_4(b).
```

Combine this with the original source G(g*a), label compensator
`gamma_4(g*b)^(-2)=G(g*b)^2`, source angle
`conjugate(alpha(g*a*n^3))`, and first character phi_f(m).
Gauss multiplicativity and G(g)^3=mu(g)*alpha(g) give, on the original
nonzero support, the exact product

```text
mu(g)*mu(a)*gamma_4(a)*G(b)*conjugate(alpha(n))^3
 *sqrt(Nf)*Lambda_(f,d)(h)*phi_f(n^3*g*m/h).
```

The target eta(g*a*n^3), all norm factors, profiles and the mask
`(m,f*d)=1` remain outside this displayed phase identity unchanged.

For clarity about the overlap phase, the cross factors from the source and
compensator are `chi_a(g)^2*chi_b(g)`. The induced Gauss factor initially
has row argument g^2*n^3*m/h. Combining these factors modulo cubic order
changes its g exponent from two to one in both orientations. Thus the
argument is n^3*g*m/h, as displayed, rather than m/h alone.

On the nonzero support this argument is a unit at f, so it may be evaluated
in the finite character. Its Kummer class is g*m/h because n^3 is a cube.
This step never takes the reciprocal of a zero-extended character at a
nonunit h. The arithmetic lift and original masks must still be preserved
in any norm estimate.

## 4. The complete one-Poisson expression

For sufficiently large Y, the annular B excludes the unit label and the
original mask removes m=0. With the same unchanged profiles, the full J is
therefore exactly

```text
sqrt(X2/X1)/Y
 *sum_(g,a,b squarefree pairwise coprime; n good)
   mu(g)*mu(a)*gamma_4(a)*gamma_2(b)*bar(alpha(n))^3
   *eta(g*a*n^3) / [q_g^(5/2)*q_a*sqrt(q_b)*q_n^4]
   *B(q_g*q_b/Y)*V(q_g*q_a*q_n^3/Z)
   *sum_(m,h nonzero, (m,f*d)=1,
         v_p(h)=v_p(d) for p|f)
      Lambda_(f,d)(h)*phi_f(n^3*g*m/h)
      *W1(q_m/(q_g*q_b*X1))*U2(X2*q_h/(q_g*q_a*q_n^3)).
```

The inner finite character is evaluated only at its stated unit argument.
This is a rearrangement of the original absolutely convergent physical
sum, rather than a sum of unbounded meromorphic rows. The real Lambda can
have either sign. Its universal majorant is
`|Lambda_(f,d)(h)|<=sqrt(q_d)*sqrt(q_h)`, by the imprimitive Gauss bound
and the primitive Gauss norm sqrt(q_f).

The denominator follows from dividing
`sqrt(q_c)*q_n*q_A*q_s` by sqrt(q_f). At g=n=1 it reduces to the familiar
`q_a*sqrt(q_b)`, retaining the same outside normalization.

## 5. All completion and overlap variables are short

In the usual truncated range at the 0.84 scales, q_h<=Z^(1/100+epsilon).
The support `g*n^2|h` gives

```text
q_g <= Z^(1/100+epsilon), q_n <= Z^(1/200+epsilon),
q_g*q_n^3 <= q_h^(3/2).
```

Together with q_A=Z^(1+O(epsilon)) and q_s=Z^(73/100+O(epsilon)), this
implies

```text
q_a >= Z^(197/200-O(epsilon)),
q_b >= Z^(18/25-O(epsilon)),
q_a/q_b >= Z^(51/200-O(epsilon)).
```

In particular the extracted long and short column supports remain separated.
These inequalities keep the coupled g,n restriction; independently paying
both upper bounds would give an unnecessarily weaker long-column estimate.

## 6. The positive conductor margin survives

For any Kummer class r, let u=core_3(r) outside S. If g is squarefree,
prime-by-prime reduction modulo three proves

```text
N(core_3(g*r)) >= N(u)/N(g)^2.
```

At a prime of g an old core exponent 0,1,2 becomes 1,2,0. The largest
possible decrease is the factor q^2. No other prime changes.

At the 0.84 scales, the standard Schwartz/Gaussian truncation permits
`N(h)<=Z^(1/100+epsilon)` after discarding an arbitrary-power tail.
It is applied to the original sums with polynomial absolute majorants,
before any rowwise analytic estimate. Since g|h, N(g) has the same bound.
After removing the already bounded geometric cores `N(u)<=Z^(1/25)`,
the extracted row consequently satisfies

```text
N(core_3(g*m/h)) > Z^(1/50-2*epsilon),
N(good primitive cubic conductor) > Z^(1/100-epsilon).
```

The second inequality uses `N(rad u')>=sqrt(N(u'))` for a cube-free u'.
Fixed S factors and the finite target twist do not cancel these good
ramified primes. This closes the row-parameter support check, with a
smaller positive margin than for the unextracted geometric class.

The remaining problem is still a signed sum with the prescribed
Mobius/Gauss coefficients, the real lift Lambda, masks and common profiles.
This identity does not turn it into the single-Gauss mixed source of a
published theorem; coefficient, length and profile hypotheses still need
a separate source-to-consumer argument.
