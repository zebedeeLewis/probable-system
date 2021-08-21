# Standard Libs
import io
import typing as T

# Third Party (Site) Libs
import openpyxl.worksheet.worksheet as worksheet
import toolz as Z
from toolz import pipe as _

# Local Libs
from libs.domain.entity.test_case import TestCase
from libs.utils.misc import MiscUtils as U


ID_COL              : T.Final[int] = 0
DESCRIPTION_COL     : T.Final[int] = 1
EXECUTION_STATE_COL : T.Final[int] = 2
TEST_STEPS_COL      : T.Final[int] = 3


Model: T.Final = T.Tuple[str, str, str, str]


@Z.curry
def read_cell(row_index: int, cell: str, worksheet: Model) -> T.Any:
  return worksheet["{}{}".format(cell, str(row_index))].value


@Z.curry
def parse(row: Model) -> TestCase.Model:
  return _( TestCase.RootModel
          , TestCase.set_id(row[ID_COL])
          , TestCase.set_description(row[DESCRIPTION_COL])
          , TestCase.set_execution_state(row[EXECUTION_STATE_COL])
          , TestCase.set_steps(_( row[TEST_STEPS_COL]
                                , U.split_by(",")
                                , U.filter(lambda x: x != "") )))


