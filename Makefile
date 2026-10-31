PYTHON ?= python3

.PHONY: verify sources diagnostics
verify:
	$(PYTHON) scripts/verify_barrier.py
	$(PYTHON) scripts/verify_moment_model.py
	$(PYTHON) scripts/verify_mixed_fibre.py
	$(PYTHON) scripts/verify_inverse_support.py
	$(PYTHON) scripts/verify_binary_cubic_kernel.py
	$(PYTHON) scripts/verify_cubic_contour_box.py
	$(PYTHON) scripts/verify_conditional_rows.py

sources:
	$(PYTHON) scripts/check_sources.py

diagnostics:
	$(PYTHON) scripts/check_binary_fourier.py
