# Standard Libs
import pdb

# Third Party (Site) Libs
import pytest
from toolz import pipe as _
import openpyxl
import openpyxl.workbook.workbook as workbook

# Local Libs
from libs.utils.constants import Constants as C
from libs.domain.entity.test_case import TestCase
from libs.infrastructure.repository.test_case import TestCaseRepo
from libs.infrastructure.data_access_object.test_case import TestCaseDAO
from libs.infrastructure.data_access_object.test_step import TestStepDAO


def pytest_generate_tests(metafunc):
  if "test_case" in metafunc.fixturenames:
    data_source = openpyxl.load_workbook(C.TEST_CASE_FILE)
    test_case_dao = TestCaseDAO.create(data_source)
    test_step_dao = TestStepDAO.create(data_source)

    test_cases = (
      TestCaseRepo
        .create(test_case_dao, test_step_dao)
        .get())

    metafunc.parametrize(
      "test_case",
      test_cases,
    )

    data_source.close()


def test_runner(test_case):
  TestCase.run(test_case)


if __name__ == "__main__":
  pytest.main([__file__+"::"+test_runner.__name__])
