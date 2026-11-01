/- Copyright (c) 2026 1337isnot1337. Apache-2.0. -/
import Std

/-! An exact finite phase identity. No analytic or L-function claim.
Values 0,...,5 encode sixth roots of unity; 6 encodes zero.
-/
namespace CubicCompensation

abbrev Phase := Fin 7
def zero : Phase := 6
def mul (x y : Phase) : Phase :=
  if x = zero ∨ y = zero then zero
  else ⟨(x.val + y.val) % 6, by omega⟩
def power (x : Phase) (n : Nat) : Phase :=
  if n = 0 then 0 else if x = zero then zero
  else ⟨(n * x.val) % 6, by omega⟩

/-- A cubic lift, multiplied by its quadratic compensator, is a prime mask. -/
theorem compensated_cube : ∀ u a : Phase,
    mul (mul u (power a 3)) (power a 3) =
      if a = zero then zero else u := by decide

/-- The uncompensated cubic lift is not a prime-deletion mask. -/
theorem uncompensated_cube_fails :
    mul (0 : Phase) (power (1 : Phase) 3) ≠ (0 : Phase) := by decide

theorem cube_image {α : Type} [Mul α] (rho : α → Phase)
    (hmul : ∀ x y, rho (x*y) = mul (rho x) (rho y)) (a : α) :
    rho (a*a*a) = power (rho a) 3 := by
  rw [hmul, hmul]
  have finite_identity : ∀ b : Phase, mul (mul b b) b = power b 3 := by decide
  exact finite_identity (rho a)

/-- Universal coefficient identity for every multiplicative sextic-phase map. -/
theorem compensated_character {α : Type} [Mul α] (rho : α → Phase)
    (hmul : ∀ x y, rho (x*y) = mul (rho x) (rho y)) (u a : α) :
    mul (rho (u*(a*a*a))) (power (rho a) 3) =
      if rho a = zero then zero else rho u := by
  rw [hmul, cube_image rho hmul a]
  exact compensated_cube (rho u) (rho a)

end CubicCompensation
#print axioms CubicCompensation.compensated_cube
#print axioms CubicCompensation.uncompensated_cube_fails
#print axioms CubicCompensation.compensated_character
