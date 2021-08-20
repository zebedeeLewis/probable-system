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
from libs.domain.entity.test_step import TestStep


STEP_ID_COL         : Final[str] = "A"
TEST_ID_COL         : Final[str] = "B"
NAME_COL            : Final[str] = "C"
DESCRIPTION_COL     : Final[str] = "D"
RUNNER_COL          : Final[str] = "E"
EXECUTION_STATE_COL : Final[str] = "F"
RESULT_COL          : Final[str] = "G"
DATA_COL            : Final[str] = "H"


Model: Final = worksheet.Worksheet


@T.curry
def read_cell(row_index: int, cell: str, worksheet: Model) -> Any:
  return worksheet["{}{}".format(cell, str(row_index))].value


@T.curry
def parse_row_to_model(row_index: int, worksheet: Model) -> TestStep.Model:
  read_row_cell = read_cell(row_index)
  return _( TestStep.RootModel
          , TestStep.set_id(read_row_cell(STEP_ID_COL, worksheet))
          , TestStep.set_test_id(read_row_cell(TEST_ID_COL, worksheet))
          , TestStep.set_name(read_row_cell(NAME_COL, worksheet))
          , TestStep.set_description(read_row_cell(DESCRIPTION_COL, worksheet))
          , TestStep.set_execution_state(read_row_cell(EXECUTION_STATE_COL, worksheet))
          , TestStep.set_result(read_row_cell(RESULT_COL, worksheet))
          , TestStep.set_data(read_row_cell(DATA_COL, worksheet))
          # TODO: replace default runner with
          #, TestStep.set_runner(read_row_cell(RUNNER_COL, worksheet)) )
          , TestStep.set_runner(TestStep.default_runner) )


