# Standard Libs
import io
from typing import (
  Optional,
  Final,
  Union,
  List)

# Third Party (Site) Libs
import openpyxl.workbook.workbook as workbook
from toolz import pipe as _

# Local Libs
from libs.infrastructure.data_access.dao_interface import DataAccessObjectI
from libs.infrastructure.data_transfer.test_step import TestStepDTO
from libs.domain.entity.test_step import TestStep


WORKSHEET_NAME: Final[str] = "test_step_table"


class TestStepDAO(DataAccessObjectI.DataAccessObjectI):

  def __init__(self, dataWorkbook: workbook.Workbook):
    self.worksheet = dataWorkbook[WORKSHEET_NAME]


  def read_set(self) -> List[TestStep.Model]:
    return [ TestStepDTO.parse_row_to_model(row_index, self.worksheet)
        for row_index in range(self.worksheet.min_row, self.worksheet.max_row+1)]


  def read_single(self, id: str) -> Union[None, TestStep.Model]:
    steps = self.read_set()
    for step in steps:
      if TestStep.get_id(step) == id:
        return step

    return None


  def read(self, id: Optional[str]=None) -> Union[None, TestStep.Model, List[TestStep.Model]]:
      return (self.read_set() if id == None
        else self.read_single(id))


def create(dataWorkbook: workbook.Workbook) -> TestStepDAO:
  return TestStepDAO(dataWorkbook)


