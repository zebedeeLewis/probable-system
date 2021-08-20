# Standard Libs
import io
from typing import (
  Optional,
  Union,
  Final,
  List)

# Third Party (Site) Libs
import openpyxl.workbook.workbook as workbook

# Local Libs
from libs.infrastructure.data_access.dao_interface import DataAccessObjectI
from libs.infrastructure.data_transfer.test_case import TestCaseDTO
from libs.domain.entity.test_case import TestCase


WORKSHEET_NAME: Final[str] = "test_case_table"


class TestCaseDAO(DataAccessObjectI.DataAccessObjectI):

  def __init__(self, dataWorkbook: workbook.Workbook):
    self.worksheet = dataWorkbook[WORKSHEET_NAME]


  def read_set(self) -> List[TestCase.Model]:
    return [ TestCaseDTO.parse_row_to_model(row_index, self.worksheet)
             for row_index in range(self.worksheet.min_row, self.worksheet.max_row+1)]


  def read_single(self, id: str) -> Union[None, TestCase.Model]:
    test_cases = self.read_set()
    for test_case in test_cases:
      if TestCase.get_id(test_case) == id:
        return test_case

    return None


  def read(self, id: Optional[str]=None) -> Union[None, TestCase.Model, List[TestCase.Model]]:
    return (self.read_set() if id == None
             else self.read_single(id))


def create(dataWorkbook: workbook.Workbook) -> TestCaseDAO:
  return TestCaseDAO(dataWorkbook)
