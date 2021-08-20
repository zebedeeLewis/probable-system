# Standard Libs
from typing import (
  Final)

# Third Party (Site) Libs
import openpyxl.workbook.workbook as workbook

# Local Libs
from libs.infrastructure.data_access.excel_db import ExcelDatabaseDAO
from libs.infrastructure.data_transfer.test_case import TestCaseDTO
from libs.domain.entity.test_case import TestCase


WORKSHEET_NAME: Final[str] = "test_case_table"


class TestCaseDAO(ExcelDatabaseDAO.ExcelDatabaseDAO):

  def __init__(self, dataWorkbook: workbook.Workbook):
    super().__init__(dataWorkbook, WORKSHEET_NAME)


  def parse_row_to_model(self, row_index: int) -> dict:
    return TestCaseDTO.parse_row_to_model(row_index, self.worksheet)


  def get_model_id(self, step: dict) -> str:
    return TestCase.get_id(step)


def create(dataWorkbook: workbook.Workbook) -> TestCaseDAO:
  return TestCaseDAO(dataWorkbook)
