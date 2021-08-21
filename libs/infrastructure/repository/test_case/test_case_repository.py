# Standard Libs
import pdb
import typing as T

# Third Party (Site) Libs
import toolz as Z
from toolz import pipe as _

# Local Libs
from libs.utils.misc import MiscUtils as U
from libs.domain.entity.test_step import TestStep
from libs.domain.entity.test_case import TestCase
from libs.infrastructure.repository.repository_interface import RepositoryI
from libs.infrastructure.data_access.test_case import TestCaseDAO
from libs.infrastructure.data_access.test_step import TestStepDAO


def flag_non_existent_step(test_step: T.Union[None, TestStep.Model]) -> TestStep.Model:
  # TODO: create a step model that should be used when a given step id is not found
  # that way the UI could display some kind of information indicating a reference
  # to a missing/non-existent step.
  return TestStep.RootModel if test_step is None else test_step


@Z.curry
def get_steps_from_ids(
    test_step_dao: TestStepDAO.TestStepDAO,
    test_step_ids: T.List[str]
    ) -> T.List[TestStep.Model]:
  return [_( step_id
           , test_step_dao.read
           , flag_non_existent_step
           ) for step_id in test_step_ids]


class TestCaseRepo(RepositoryI.RepositoryI):

  def __init__(
      self,
      test_case_dao: TestCaseDAO.TestCaseDAO,
      test_step_dao: TestStepDAO.TestStepDAO
      ):
    self.test_step_dao = test_step_dao
    self.test_case_dao = test_case_dao


  def get(self) -> T.List[TestCase.Model]:
    return [_( test_case
             , TestCase.get_steps
             , get_steps_from_ids(self.test_step_dao)
             , TestCase.set_steps
             , U.on(test_case)
             ) for test_case in self.test_case_dao.read()]
    

  # TODO!!!
  def get_by_id(self, id: str) -> T.Union[None, TestCase.Model]:
    pass


@Z.curry
def create(
    test_case_dao: TestCaseDAO.TestCaseDAO,
    test_step_dao: TestStepDAO.TestStepDAO
    ) -> TestCaseRepo:
  return TestCaseRepo(test_case_dao, test_step_dao)

