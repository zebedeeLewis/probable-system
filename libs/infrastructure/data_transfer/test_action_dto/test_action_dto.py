# Standard Libs
import typing as T

# Third Party (Site) Libs
import toolz as Z
from toolz import pipe as _

# Local Libs
from libs.domain.entity.test_action_entity import TestAction


ID_COL          : T.Final[int] = 0
NAME_COL        : T.Final[str] = 1
DESCRIPTION_COL : T.Final[int] = 2
RUNNER_NAME_COL : T.Final[str] = 3


class DTO(T.TypedDict):
  id          : str
  name        : str
  description : str
  runner_name : str


Root_DTO: T.Final[DTO] = {
  "id"          : "default-step-id",
  "name"        : "default step",
  "description" : "default step does nothing",
  "runner_name" : "default_runner",
}


@Z.curry
def set_id(id: str, dto: DTO) -> DTO:
  return Z.assoc(dto, 'id', id)


def get_id(dto: DTO) -> str:
  return dto.get('id')


@Z.curry
def set_name(name: str, dto: DTO) -> DTO:
  return Z.assoc(dto, 'name', name)


def get_name(dto: DTO) -> str:
  return dto.get('name')


@Z.curry
def set_description(description: str, dto: DTO) -> DTO:
  return Z.assoc(dto, 'description', description)


def get_description(dto: DTO) -> str:
  return dto.get('description')


@Z.curry
def set_runner_name(name: str, dto: DTO) -> DTO:
  return Z.assoc(dto, 'runner_name', name)


def get_runner_name(dto: DTO) -> str:
  return dto.get('runner_name')


@Z.curry
def from_tuple(
    row: T.Final = T.Tuple[str, str, str, str]
    ) -> DTO:
  return _( Root_DTO
          , set_id(row[ID_COL])
          , set_name(row[NAME_COL])
          , set_description(row[DESCRIPTION_COL])
          , set_runner_name(row[RUNNER_NAME_COL]))


@Z.curry
def to_model(runner: TestAction.Action_Runner, dto: DTO) -> TestAction.Model:
  return _( TestAction.RootModel
          , _(dto, get_id, TestAction.set_id)
          , _(dto, get_name, TestAction.set_name)
          , _(dto, get_description, TestAction.set_description)
          , TestAction.set_runner(runner))


