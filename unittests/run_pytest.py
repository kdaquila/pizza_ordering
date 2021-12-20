import pytest

pytest.main(["--cov", "src", ".", "--cov-report",  "term-missing"])
