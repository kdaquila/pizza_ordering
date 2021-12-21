import pytest

pytest.main(["--cov", "src", "./unittests", "--cov-report",  "term-missing"])
