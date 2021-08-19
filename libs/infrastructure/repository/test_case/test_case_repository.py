# Standard Libs
import pdb
from typing import (
  Final,
  Union,
  NoReturn,
  List)

# Third Party (Site) Libs
import toolz as T
from toolz import pipe as _

# Local Libs
from libs.utils.misc import MiscUtils as U
from libs.domain.entity.test_step import TestStep
from libs.domain.entity.test_case import TestCase
from libs.infrastructure.repository.repository_interface import RepositoryI
from libs.infrastructure.data_access_object.test_case import TestCaseDAO
from libs.infrastructure.data_access_object.test_step import TestStepDAO


@T.curry
def get_steps_from_ids(
    test_step_dao: TestStepDAO.TestStepDAO,
    test_step_ids: List[str]) -> List[TestStep.Model]:
  test_steps = []
  for id in test_step_ids:
    step_read_result = test_step_dao.read(id)
    step = TestStep.Model if step_read_result == None else step_read_result
    test_steps = [*steps, step]

  return test_steps


class TestCaseRepo(RepositoryI.RepositoryI):

  def __init__(
      self,
      test_case_dao: TestCaseDAO.TestCaseDAO,
      test_step_dao: TestStepDAO.TestStepDAO
      ):
    self.test_step_dao = test_step_dao
    self.test_case_dao = test_case_dao


  def get(self) -> List[TestCase.Model]:
    test_cases = self.test_case_dao.read()
    final_test_cases = []
    for test_case in test_cases:
      step_ids = TestCase.get_steps(test_case)
      test_steps = get_steps_from_ids(self.test_step_dao, step_ids)
      final_test_cases = [*final_test_cases, TestCase.set_steps(test_steps)]

    return final_test_cases
    

  # TODO!!!
  def get_by_id(self, id: str) -> Union[None, TestCase.Model]:
    pass


@T.curry
def create(
    test_case_dao: TestCaseDAO.TestCaseDAO,
    test_step_dao: TestStepDAO.TestStepDAO
    ) -> TestCaseRepo:
  return TestCaseRepo(test_case_dao, test_step_dao)

