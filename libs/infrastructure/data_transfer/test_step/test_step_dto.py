# Standard Libs
import io
import typing as T

# Third Party (Site) Libs
import openpyxl.worksheet.worksheet as worksheet
import toolz as Z
from toolz import pipe as _

# Local Libs
from libs.domain.entity.test_step_entity import TestStep
from libs.domain.entity.test_action_entity import TestAction
from libs.utils.misc import MiscUtils as U


ID_COL          : T.Final[int] = 0
TEST_ID_COL     : T.Final[int] = 1
ACTION_ID_COL   : T.Final[int] = 2
DESCRIPTION_COL : T.Final[int] = 3
DATA_COL        : T.Final[int] = 4


class DTO(T.TypedDict):
  id          : str
  test_id     : str
  action_id   : str
  description : str
  data        : T.Union[None, str]


RootDTO: T.Final[DTO] = {
  "id"          : "default-step-id",
  "test_id"     : "default-test-id",
  "action_id"   : "default-action-id",
  "description" : "default step does nothing",
  "data"        : None,
}


@Z.curry
def set_data(data: str, dto: DTO) -> DTO:
  return Z.assoc(dto, 'data', data)


def get_data(dto: DTO) -> str:
  return dto.get('data')


@Z.curry
def set_description(description: str, dto: DTO) -> DTO:
  return Z.assoc(dto, 'description', description)


def get_description(dto: DTO) -> str:
  return dto.get('description')


@Z.curry
def set_action_id(action_id: str, dto: DTO) -> DTO:
  return Z.assoc(dto, 'action_id', action_id)


def get_action_id(dto: DTO) -> str:
  return dto.get('action_id')


@Z.curry
def set_test_id(test_id: str, dto: DTO) -> DTO:
  return Z.assoc(dto, 'test_id', test_id)


def get_test_id(dto: DTO) -> str:
  return dto.get('test_id')


@Z.curry
def set_id(id: str, dto: DTO) -> DTO:
  return Z.assoc(dto, 'id', id)


def get_id(dto: DTO) -> str:
  return dto.get('id')


@Z.curry
def from_tuple(
    row: T.Final = T.Tuple[str, str, str, str, T.Union[None, str]]
    ) -> DTO:
  return _( RootDTO
          , set_id(row[ID_COL])
          , set_test_id(row[TEST_ID_COL])
          , set_action_id(row[ACTION_ID_COL])
          , set_description(row[DESCRIPTION_COL])
          , set_data(row[DATA_COL]))


@Z.curry
def to_model(action: TestAction.Model, dto: DTO) -> TestStep.Model:
  return _( TestStep.RootModel
          , _(dto, get_id, TestStep.set_id)
          , _(dto, get_description, TestStep.set_description)
          , _(dto, get_data, TestStep.set_data)
          , _(dto, get_test_id, TestStep.set_test_id)
          , TestStep.set_action(action))


