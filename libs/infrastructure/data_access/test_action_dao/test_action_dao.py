# Standard Libs
import typing as T

# Third Party (Site) Libs
import openpyxl.workbook.workbook as workbook

# Local Libs
from libs.infrastructure.data_access.excel_db import ExcelDatabaseDAO
from libs.infrastructure.data_transfer.test_action import TestActionDTO
from libs.domain.entity.test_action_entity import TestAction


WORKSHEET_NAME: T.Final[str] = "test_action_table"
FIRST_COL_INDEX: T.Final[str] = 1


class TestActionDAO(ExcelDatabaseDAO.ExcelDatabaseDAO):

  def __init__(self, dataWorkbook: workbook.Workbook):
    super().__init__(dataWorkbook, WORKSHEET_NAME)


  def parse(self, row_index: int) -> TestActionDTO.DTO:
    return TestActionDTO.from_tuple(next(self.worksheet.iter_rows(
      row_index,
      row_index,
      FIRST_COL_INDEX,
      self.worksheet.max_column,
      True)))


  def get_model_id(self, action: dict) -> str:
    return TestAction.get_id(action)


def create(dataWorkbook: workbook.Workbook) -> TestActionDAO:
  return TestActionDAO(dataWorkbook)
