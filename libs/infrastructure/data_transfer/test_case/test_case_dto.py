# Standard Libs
import io
import typing as T

# Third Party (Site) Libs
import openpyxl.worksheet.worksheet as worksheet
import toolz as Z
from toolz import pipe as _

# Local Libs
from libs.domain.entity.test_case_entity import TestCase
from libs.domain.entity.test_step_entity import TestStep
from libs.utils.misc import MiscUtils as U


ID_COL              : T.Final[int] = 0
DESCRIPTION_COL     : T.Final[int] = 1


class DTO(T.TypedDict):
  id          : str
  description : str


RootDTO: T.Final[DTO] = {
  "id"          : "default-test-id",
  "description" : "this is the default test",
}


@Z.curry
def set_id(id: str, dto: DTO) -> DTO:
  return Z.assoc(dto, 'id', id)


def get_id(dto: DTO) -> str:
  return dto.get('id')


@Z.curry
def set_description(description: str, dto: DTO) -> DTO:
  return Z.assoc(dto, 'description', description)


def get_description(dto: DTO) -> str:
  return dto.get('description')


@Z.curry
def from_tuple(row: T.Final = T.Tuple[str, str]) -> DTO:
  return _( RootDTO
          , set_id(row[ID_COL])
          , set_description(row[DESCRIPTION_COL]))


@Z.curry
def to_model(steps: T.List[TestStep.Model], dto: DTO) -> TestCase.Model:
  return _( TestCase.RootModel
          , _(dto, get_id, TestCase.set_id)
          , _(dto, get_description, TestCase.set_description)
          , TestCase.set_steps(steps) )


