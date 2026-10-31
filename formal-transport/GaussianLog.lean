import Submissions.openai_baseline.OAI.NumberTheory.DirichletL.Detector.GaussianMellin

namespace Transport087

theorem abs_mul_gaussian_le_one (u : ℝ) :
    |u| * Real.exp (-u^2) ≤ 1 := by
  have hquad : |u| ≤ u^2+1 := by nlinarith [sq_nonneg (|u|-1), sq_abs u]
  have he : |u| ≤ Real.exp (u^2) := hquad.trans (Real.add_one_le_exp (u^2))
  calc
    _ ≤ Real.exp (u^2)*Real.exp (-u^2) :=
      mul_le_mul_of_nonneg_right he (Real.exp_pos _).le
    _ = 1 := by rw [←Real.exp_add]; simp

theorem log_half_gaussian_power_bound (y a : ℝ) (hy : 0<y) :
    |Real.log y/2| *Real.exp (-(Real.log y)^2/4) ≤
      (1+|a|)*Real.exp (a^2)*y^(-a) := by
  let u := Real.log y/2-a
  have hid : Real.log y/2 = u+a := by dsimp [u]; ring
  have hb : |Real.log y/2| *Real.exp (-u^2) ≤ 1+|a| := by
    have h : |u+a| ≤ |u|+|a| := by
      simpa only [Real.norm_eq_abs] using norm_add_le u a
    rw [←hid] at h
    have hexp : Real.exp (-u^2) ≤ 1 := by
      simpa using Real.exp_le_exp.mpr (neg_nonpos.mpr (sq_nonneg u))
    calc
      _ ≤ (|u|+|a|)*Real.exp (-u^2) :=
        mul_le_mul_of_nonneg_right h (Real.exp_pos _).le
      _ = |u| *Real.exp (-u^2)+|a| *Real.exp (-u^2) := by ring
      _ ≤ 1+|a| := add_le_add (abs_mul_gaussian_le_one u)
        (by simpa using mul_le_mul_of_nonneg_left hexp (abs_nonneg a))
  have hexponent : -(Real.log y)^2/4 = a^2+(-a)*Real.log y-u^2 := by
    dsimp [u]; ring
  have hfactor : Real.exp (-(Real.log y)^2/4) =
      Real.exp (-u^2)*(Real.exp (a^2)*y^(-a)) := by
    rw [Real.rpow_def_of_pos hy]
    rw [←Real.exp_add,←Real.exp_add,hexponent]
    congr 1
    ring
  rw [hfactor,←mul_assoc]
  have hpos : 0 ≤ Real.exp (a^2)*y^(-a) := by positivity
  have hfinal := mul_le_mul_of_nonneg_right hb hpos
  convert hfinal using 1
  ring

theorem gaussianMellinProfile_log_power_bound (y a : ℝ) (hy : 0<y) :
    ‖((Real.log y/2 : ℝ) : ℂ)*OAI.SevenEighths.ProbePhysical.gaussianMellinProfile y‖ ≤
      ‖((1/(2*Real.pi):ℝ):ℂ)*(Real.pi:ℂ)^(1/2:ℂ)‖ *
        (1+|a|)*Real.exp (a^2)*y^(-a) := by
  rw [norm_mul, Complex.norm_real, Real.norm_eq_abs,
    OAI.SevenEighths.ProbePhysical.gaussianMellinProfile_norm y hy]
  have hb := mul_le_mul_of_nonneg_left (log_half_gaussian_power_bound y a hy)
    (norm_nonneg (((1/(2*Real.pi):ℝ):ℂ)*(Real.pi:ℂ)^(1/2:ℂ)))
  convert hb using 1 <;> ring

theorem realGaussian_hasDerivAt (y : ℝ) (hy : 0<y) :
    HasDerivAt (fun r : ℝ => Real.exp (-(Real.log r)^2/4))
      (-(Real.log y/(2*y))*Real.exp (-(Real.log y)^2/4)) y := by
  convert (((Real.hasDerivAt_log hy.ne').pow 2).neg.div_const 4).exp using 1
  dsimp
  ring

theorem coupled_gaussian_atom (f g : ℝ → ℝ) (r s y fp gp : ℝ)
    (hf : HasDerivAt f fp r) (hg : HasDerivAt g gp s) (hy : 0<y) :
    deriv (fun t : ℝ => Real.exp ((-3/2)*t)*f (r*Real.exp (-t))*
      g (s*Real.exp (-t))*Real.exp (-(Real.log (y*Real.exp (-t)))^2/4)) 0
      +(1/2)*f r*g s*Real.exp (-(Real.log y)^2/4) =
    -f r*g s*Real.exp (-(Real.log y)^2/4)
      -r*fp*g s*Real.exp (-(Real.log y)^2/4)
      -s*f r*gp*Real.exp (-(Real.log y)^2/4)
      +f r*g s*(Real.log y/2)*Real.exp (-(Real.log y)^2/4) := by
  have he : HasDerivAt (fun t : ℝ => Real.exp (-t)) (-1) 0 := by
    simpa using (hasDerivAt_neg (0:ℝ)).exp
  have hn : HasDerivAt (fun t : ℝ => Real.exp ((-3/2)*t)) (-3/2) 0 := by
    simpa using ((hasDerivAt_id (0:ℝ)).const_mul (-3/2)).exp
  have hfr := hf.comp_of_eq 0 (he.const_mul r) (by simp)
  have hgs := hg.comp_of_eq 0 (he.const_mul s) (by simp)
  have hgy := (realGaussian_hasDerivAt y hy).comp_of_eq 0
    (he.const_mul y) (by simp)
  have h := (((hn.mul hfr).mul hgs).mul hgy).deriv
  simp only [Pi.mul_def, Function.comp_def, neg_zero, Real.exp_zero, mul_one, mul_zero] at h
  rw [h]
  field_simp [hy.ne']
  ring

#print axioms abs_mul_gaussian_le_one
#print axioms log_half_gaussian_power_bound
#print axioms gaussianMellinProfile_log_power_bound
#print axioms realGaussian_hasDerivAt
#print axioms coupled_gaussian_atom
end Transport087
