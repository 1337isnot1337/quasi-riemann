PYTHON ?= python3
LEAN ?= lean

.PHONY: verify verify-lean sources diagnostics
verify:
	$(PYTHON) scripts/verify_barrier.py
	$(PYTHON) scripts/verify_moment_model.py
	$(PYTHON) scripts/verify_cubic_compensation.py
	$(PYTHON) scripts/verify_mixed_fibre.py
	$(PYTHON) scripts/verify_inverse_support.py
	$(PYTHON) scripts/verify_euler_regularization.py
	$(PYTHON) scripts/verify_binary_cubic_kernel.py
	$(PYTHON) scripts/verify_conditional_rows.py
	$(PYTHON) scripts/verify_mellin_annihilator.py
	$(PYTHON) scripts/verify_cubic_signed_budget.py
	$(PYTHON) scripts/verify_jacobi_detector.py

sources:
	$(PYTHON) scripts/check_sources.py

verify-lean:
	$(LEAN) lean/CubicCompensation.lean
diagnostics:
	$(PYTHON) scripts/check_binary_fourier.py
