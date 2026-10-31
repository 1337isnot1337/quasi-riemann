/- Copyright (c) 2026 1337isnot1337. Apache-2.0. -/
import Candidate.Local.Qrh.JointDetector.BoundaryPhysical.TransportGeometry

/-! Geometry admission only. No improved row count or nonvanishing claim. -/
namespace Transport087
open QRH.Record1252270103Return

noncomputable instance geometry : Geometry.Parameters where
  theta := 87/100
  ell := 14/75
  x := 607/1500
  y := 613/1500
  ell_pos := by norm_num
  sixth_lt_ell := by norm_num
  ell_lt_fifth := by norm_num
  ell_lt_x := by norm_num
  x_lt_y := by norm_num
  y_lt_half := by norm_num
  x_add_y := by norm_num
  dilation_gap := by norm_num
  tuple_margin_neg := by norm_num
  signal_boundary := by norm_num

noncomputable instance bounds :
    Qrh.JointDetector.BoundaryPhysical.Return.Geometry.BoundsN where
  theta_bounds := by
    change (869/1000 : ℝ) < 87/100 ∧ (87/100 : ℝ) < 7/8
    norm_num
  h_interval := by
    change (781/1000 : ℝ) < 1+14/75-607/1500 ∧
      (1+14/75-607/1500 : ℝ) < 813/1000
    norm_num
  ly_coarse := by
    change (408/1000 : ℝ) < 613/1500 ∧ (613/1500 : ℝ) < 473/1000
    norm_num
  ell_interval := by
    change (1672/10000 : ℝ) < 14/75 ∧ (14/75 : ℝ) < 187/1000
    norm_num
  small_saving := by
    change (6/125 : ℝ) < 613/1500/2-(1+14/75-607/1500)*(17/50-1/6)-1/50
    norm_num
  floor_margin := by
    change (4/25 : ℝ)*(607/1500)-3/20-(51/100)*(613/1500)+
      (67/100)*(1+14/75-607/1500+1/10000000000000000000000)-(3/20)*(14/75) ≤
      (87/100 : ℝ)+(-(4+613/1500-607/1500)/6)-1/10000
    norm_num

theorem geometry_value : Geometry.theta = (87/100 : ℝ) ∧
    Geometry.h = (391/500 : ℝ) := by
  change (87/100 : ℝ) = 87/100 ∧ (1+14/75-607/1500 : ℝ) = 391/500
  norm_num

end Transport087

#print axioms Transport087.geometry
#print axioms Transport087.bounds
#print axioms Transport087.geometry_value
