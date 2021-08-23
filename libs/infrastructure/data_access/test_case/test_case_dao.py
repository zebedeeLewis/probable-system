# Standard Libs
import typing as T

# Third Party (Site) Libs
import openpyxl.workbook.workbook as workbook

# Local Libs
from libs.infrastructure.data_access.excel_db import ExcelDatabaseDAO
from libs.infrastructure.data_transfer.test_case import TestCaseDTO
from libs.domain.entity.test_case_entity import TestCase


WORKSHEET_NAME: T.Final[str] = "test_case_table"
FIRST_COL_INDEX: T.Final[str] = 1



class TestCaseDAO(ExcelDatabaseDAO.ExcelDatabaseDAO):

  def __init__(self, dataWorkbook: workbook.Workbook):
    super().__init__(dataWorkbook, WORKSHEET_NAME)


  def parse(self, row_index: int) -> dict:
    return TestCaseDTO.from_tuple(next(
      self.worksheet.iter_rows(
        row_index,
        row_index,
        FIRST_COL_INDEX,
        self.worksheet.max_column,
        True) ))


  def get_model_id(self, step: dict) -> str:
    return TestCase.get_id(step)


def create(dataWorkbook: workbook.Workbook) -> TestCaseDAO:
  return TestCaseDAO(dataWorkbook)
