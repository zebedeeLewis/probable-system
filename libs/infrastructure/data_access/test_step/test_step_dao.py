# Standard Libs
import io
from typing import (
  Optional,
  Any,
  Final,
  Union,
  List)

# Third Party (Site) Libs
import openpyxl.workbook.workbook as workbook
from toolz import pipe as _

# Local Libs
from libs.infrastructure.data_access.dao_interface import DataAccessObjectI
from libs.domain.entity.test_step import TestStep


WORKSHEET_NAME      : Final[str] = "Sheet1"
STEP_ID_COL         : Final[str] = "A"
TEST_ID_COL         : Final[str] = "B"
NAME_COL            : Final[str] = "C"
DESCRIPTION_COL     : Final[str] = "D"
RUNNER_COL          : Final[str] = "E"
EXECUTION_STATE_COL : Final[str] = "F"
RESULT_COL          : Final[str] = "G"
DATA_COL            : Final[str] = "H"


class TestStepDAO(DataAccessObjectI.DataAccessObjectI):

  def __init__(self, dataWorkbook: workbook.Workbook):
    self.worksheet = dataWorkbook[WORKSHEET_NAME]


  def read_cell(self, row, cell) -> Any:
    return self.worksheet["{}{}".format(cell, str(row))].value


  def parse_row_to_model(self, row_index) -> TestStep.Model:
    return _( TestStep.RootModel
            , TestStep.set_id(self.read_cell(row_index, STEP_ID_COL))
            , TestStep.set_test_id(self.read_cell(row_index, TEST_ID_COL))
            , TestStep.set_name(self.read_cell(row_index, NAME_COL))
            , TestStep.set_description(self.read_cell(row_index, DESCRIPTION_COL))
            , TestStep.set_runner(self.read_cell(row_index, RUNNER_COL))
            , TestStep.set_execution_state(self.read_cell(row_index, EXECUTION_STATE_COL))
            , TestStep.set_result(self.read_cell(row_index, RESULT_COL))
            , TestStep.set_data(self.read_cell(row_index, DATA_COL)))


  def read_set(self) -> List[TestStep.Model]:
    test_steps = []
    for row_index in range(self.worksheet.min_row, self.worksheet.max_row+1):
      test_steps = [
        *test_steps,
        self.parse_row_to_model(row_index)
      ]

    return test_steps


  def read_single(self, id: str) -> Union[None, TestStep.Model]:
    steps = self.read_set()
    for step in steps:
      if TestStep.get_id(step) == id:
        return step

    return None


  def read(self, id: Optional[str]=None) -> Union[None, TestStep.Model, List[TestStep.Model]]:
    if id == None:
      return self.read_set()

    return self.read_single(id)


def create(dataWorkbook: workbook.Workbook) -> TestStepDAO:
  return TestStepDAO(dataWorkbook)


