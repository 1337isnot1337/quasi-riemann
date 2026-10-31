# An obstruction for the inherited count/return model

Status: exact algebraic argument about the specified model. This is not a
zero-free-region theorem. The limiting number was already identified in the
preexisting PRs; the results here make the obstruction uniform in the geometry
parameter h, the Mellin line and the available face choices.

All formulas refer to the source-pinned PR #99 modules in `docs/SOURCES.md`.
The calculations replay with `scripts/verify_barrier.py`.

## 1. Optimistic source class and cap dominance

Let 0 <= delta <= 3/4, 0 <= p <= 1/2, V = 5/6 - delta. Consider every face
with B <= 1 and Lambda >= 2. For its uncapped branch define

```text
D = 3-p-4p/Lambda,  A = 2-4p/Lambda,
U = (1-p)(1-2pB/Lambda),
J = V D + delta(1-p)A,
N = (1-delta)J + V delta U,
T = J + delta U,
MN = D T - [A T + (2pB/Lambda-p)J].
```

Its admitted row count is R = N/J. For a capped branch replace D by 3-p,
A by 2, and B/Lambda by its actual selected width z, including any reserve
already subtracted. Write these quantities as Jc, Nc and MNc, and Dc = 3-p.
The upper plain-length admission guard implies

```text
G := ((B-Lambda*z)/2) Dc Jc - MNc >= 0.
```

The exact identity is

```text
(Nc J - N Jc) Dc Lambda = 4 delta p V (1-p) G.
```

All denominators are positive: V >= 1/12, Dc >= 5/2, D >= 3-3p,
A >= 2-2p, hence J,Jc > 0. Therefore every admitted capped count is at least
the corresponding uncapped count. Other admission guards can only restrict
the available branches further.

Next,

```text
dR/dB = -2 p V delta(1-p)/(Lambda J) <= 0,
(dR/dLambda)|B=1 = 2 delta p V^2(1-p)^2/(Lambda^2 J^2) >= 0.
```

Thus the optimistic uncapped B=1, Lambda=2 branch is at least as strong as
every uncapped or admitted capped branch in this face class. For the old count
with kappa >= 1/3, direct subtraction also gives

```text
No J - N Jo = delta p V^2 (3kappa-1)(1-p)^2/(3kappa) >= 0,
```

where J,N now denote that ideal branch. This includes the old branch used by
the inherited return. Arbitrarily many windows of these types cannot improve
the optimistic count. This is a domination argument, not a finite window search.

## 2. The contour disappears at the endpoint

Put theta=1-c, ell=4c-1/3, y=h-2ell. At conductor d, use the optimistic
physical capacity C(d)=(2y-d)/2. Actual clipping or weaker faces reduce this
capacity and increase the row exponent.

If a is the real part of the external Mellin line, the reconstructed exponent is

```text
E = 1/2 + (a-1/6)h - y/2 - ell/2 + (1/4-a)d
    + delta/2 + delta*p*(ell-C(d)/2) + 3d R/4.
```

At d=h the terms containing a cancel identically. This is an algebraic
invariance: even assuming every Mellin line were analytically available,
moving it cannot fix the obstructing endpoint. It does not assert such
availability in the actual analytic proof.

## 3. A witness independent of h

On p=1/2 let F=J(theta-E) at d=h. Direct simplification gives

```text
48 F = 192c delta^2 - 96c delta - 180c
       - 33 delta^2 h + 8 delta^2 + 61 delta h - 42 delta - 20h + 40.
```

Set

```text
delta* = (61-sqrt(1081))/66 = 0.42608235688564859...
c*     = (75+sqrt(1081))/852,
theta* = 1-c* = (777-sqrt(1081))/852
       = 0.8733819666132075199290267786...
A*     = 5179/4356 + 89 sqrt(1081)/1089 > 0.
```

The crucial identity, for **every real h**, is

```text
F(delta*,1/2;c,h) = A* (c*-c).
```

Therefore c>c* makes the necessary row margin negative, irrespective of h.
The ideal branch already dominates all the inherited count choices above,
and the capacity used here is optimistic. This rules out a uniform return
certificate below theta* within this specific model. Adapting h to the row
cannot remove this particular witness either.

At the limiting stationary choice,

```text
h* = 32/71 + 838 sqrt(1081)/76751
   = 0.809686349433473801659303...
```

both F and its delta derivative vanish. The exact contact lies inside the
rectangle whose left edge is delta=3/8. Delta=3/8 itself is not the stationary
point: substituting it gives a positive margin at the limiting constants.

## What this rules out and what it leaves open

This argument rules out source-gap retuning, more windows from the same face
class, cap retuning, changing h, and moving the Mellin line as mechanisms for a
substantial jump while retaining the specified row exponent and count formulas.
It is not a barrier for all possible implementations of the paper's method.

Possible exits include a new row count below this envelope, a stronger weighted
numerator moment, a different physical capacity relation, or a new signal/geometry.
Every exit requires an analytic argument; replacing its exponent in a numerical
model does not supply that argument.
