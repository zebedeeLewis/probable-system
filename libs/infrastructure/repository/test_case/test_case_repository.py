# Standard Libs
import pdb
import typing as T

# Third Party (Site) Libs
import toolz as Z
from toolz import pipe as _

# Local Libs
from libs.utils.misc import MiscUtils as U
from libs.domain.entity.test_step_entity import TestStep
from libs.domain.entity.test_case_entity import TestCase
from libs.domain.entity.test_action_entity import TestAction
from libs.infrastructure.data_transfer.test_case import TestCaseDTO
from libs.infrastructure.data_transfer.test_step import TestStepDTO
from libs.infrastructure.data_transfer.test_action_dto import TestActionDTO
from libs.infrastructure.data_access.test_case import TestCaseDAO
from libs.infrastructure.data_access.test_step import TestStepDAO
from libs.infrastructure.data_access.test_action_dao import TestActionDAO
from libs.infrastructure.repository.repository_interface import RepositoryI


class TestCaseRepo(RepositoryI.RepositoryI):

  def __init__(
      self,
      test_case_dao: TestCaseDAO.TestCaseDAO,
      test_step_dao: TestStepDAO.TestStepDAO,
      test_action_dao: TestActionDAO.TestActionDAO
      ):
    self.test_action_dao = test_action_dao
    self.test_step_dao = test_step_dao
    self.test_case_dao = test_case_dao


  def fetch_action(self, action_id: str) -> TestAction.Model:
    return _( self.test_action_dao.read(action_id)
            , TestActionDTO.to_model(TestAction.default_runner) )


  def fetch_steps(self, test_id: str) -> T.List[TestStep.Model]:
    return [_( step_dto
             , TestStepDTO.get_action_id
             , self.fetch_action
             , TestStepDTO.to_model
             , U.apply_to(step_dto)
             ) for step_dto
                 in self.test_step_dao.read()
                 if TestStepDTO.get_test_id(step_dto) == test_id ]


  def get(self) -> T.List[TestCase.Model]:
    return [_( test_case_dto
             , TestCaseDTO.get_id
             , self.fetch_steps
             , TestCaseDTO.to_model
             , U.apply_to(test_case_dto)
             ) for test_case_dto
                 in self.test_case_dao.read() ]


  # TODO!!!
  def get_by_id(self, id: str) -> T.Union[None, TestCase.Model]:
    pass


@Z.curry
def create(
    test_case_dao: TestCaseDAO.TestCaseDAO,
    test_step_dao: TestStepDAO.TestStepDAO,
    test_action_dao: TestActionDAO.TestActionDAO
    ) -> TestCaseRepo:
  return TestCaseRepo(test_case_dao, test_step_dao, test_action_dao)

