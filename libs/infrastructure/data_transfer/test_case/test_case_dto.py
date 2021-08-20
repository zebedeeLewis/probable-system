# Standard Libs
import io
from typing import (
  Any,
  Final)

# Third Party (Site) Libs
import openpyxl.worksheet.worksheet as worksheet
import toolz as T
from toolz import pipe as _

# Local Libs
from libs.domain.entity.test_case import TestCase
from libs.utils.misc import MiscUtils as U


ID_COL              : Final[str] = "A"
DESCRIPTION_COL     : Final[str] = "B"
EXECUTION_STATE_COL : Final[str] = "C"
TEST_STEPS_COL      : Final[str] = "D"


Model: Final = worksheet.Worksheet


@T.curry
def read_cell(row_index: int, cell: str, worksheet: Model) -> Any:
  return worksheet["{}{}".format(cell, str(row_index))].value


@T.curry
def parse_row_to_model(row_index: int, worksheet: Model) -> TestCase.Model:
  read_row_cell = read_cell(row_index)
  return _( TestCase.RootModel
          , TestCase.set_id(read_row_cell(ID_COL, worksheet))
          , TestCase.set_description(read_row_cell(DESCRIPTION_COL, worksheet))
          , TestCase.set_execution_state(read_row_cell(EXECUTION_STATE_COL, worksheet))
          , TestCase.set_steps(_( worksheet
                                , read_row_cell(TEST_STEPS_COL)
                                , U.split_by(",")
                                , U.filter(lambda x: x != "") )))


