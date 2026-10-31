PYTHON ?= python3

.PHONY: verify sources
verify:
	$(PYTHON) scripts/verify_barrier.py
	$(PYTHON) scripts/verify_moment_model.py
	$(PYTHON) scripts/verify_mixed_fibre.py
	$(PYTHON) scripts/verify_inverse_support.py
	$(PYTHON) scripts/verify_conditional_rows.py
	$(PYTHON) scripts/verify_mellin_annihilator.py
	$(PYTHON) scripts/verify_jacobi_detector.py

sources:
	$(PYTHON) scripts/check_sources.py
