# Standard Libs
import pdb

# Third Party (Site) Libs
import pytest
from toolz import pipe as _

# Local Libs
from libs.domain.entity.test_case import TestCase
from libs.test_case_source import TestCaseSource
from libs.constants import Constants as C


def pytest_generate_tests(metafunc):
  if "test_case" in metafunc.fixturenames:
    metafunc.parametrize(
      "test_case",
      _( C.TEST_CASE_FILE
       , TestCaseSource.load
       , TestCaseSource.to_test_cases)
    )


def test_runner(test_case):
  TestCase.run(test_case)


if __name__ == "__main__":
  pytest.main([__file__+"::"+test_runner.__name__])
