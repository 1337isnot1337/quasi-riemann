PYTHON ?= python3
LEAN ?= lean

.PHONY: verify verify-lean sources
verify:
	$(PYTHON) scripts/verify_barrier.py
	$(PYTHON) scripts/verify_moment_model.py
	$(PYTHON) scripts/verify_mixed_fibre.py
	$(PYTHON) scripts/verify_cubic_compensation.py
	$(PYTHON) scripts/verify_conditional_rows.py

sources:
	$(PYTHON) scripts/check_sources.py

verify-lean:
	$(LEAN) lean/CubicCompensation.lean
