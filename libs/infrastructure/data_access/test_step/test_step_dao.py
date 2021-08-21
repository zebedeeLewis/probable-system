# Standard Libs
import typing as T

# Third Party (Site) Libs
import openpyxl.workbook.workbook as workbook
from toolz import pipe as _

# Local Libs
from libs.infrastructure.data_access.excel_db import ExcelDatabaseDAO
from libs.infrastructure.data_transfer.test_step import TestStepDTO
from libs.domain.entity.test_step_entity import TestStep


WORKSHEET_NAME: T.Final[str] = "test_step_table"


class TestStepDAO(ExcelDatabaseDAO.ExcelDatabaseDAO):

  def __init__(self, dataWorkbook: workbook.Workbook):
    super().__init__(dataWorkbook, WORKSHEET_NAME)


  def parse(self, row_index: int) -> dict:
    return TestStepDTO.parse(row_index, self.worksheet)


  def get_model_id(self, step: dict) -> str:
    return TestStep.get_id(step)


def create(dataWorkbook: workbook.Workbook) -> TestStepDAO:
  return TestStepDAO(dataWorkbook)


