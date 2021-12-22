import pytest

pytest.main(["--cov", "src", "./unit_tests", "--cov-report",  "term-missing"])
