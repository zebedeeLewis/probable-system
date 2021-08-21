# Standard Libs
import io
import typing as T

# Third Party (Site) Libs
import openpyxl.worksheet.worksheet as worksheet
import toolz as Z
from toolz import pipe as _

# Local Libs
from libs.domain.entity.test_step_entity import TestStep


STEP_ID_COL         : T.Final[str] = "A"
TEST_ID_COL         : T.Final[str] = "B"
NAME_COL            : T.Final[str] = "C"
DESCRIPTION_COL     : T.Final[str] = "D"
RUNNER_COL          : T.Final[str] = "E"
EXECUTION_STATE_COL : T.Final[str] = "F"
RESULT_COL          : T.Final[str] = "G"
DATA_COL            : T.Final[str] = "H"


Model: T.Final = worksheet.Worksheet


@Z.curry
def read_cell(row_index: int, cell: str, worksheet: Model) -> T.Any:
  return worksheet["{}{}".format(cell, str(row_index))].value


@Z.curry
def parse(row_index: int, worksheet: Model) -> TestStep.Model:
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


