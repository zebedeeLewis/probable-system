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
FIRST_COL_INDEX: T.Final[int] = 1


class TestStepDAO(ExcelDatabaseDAO.ExcelDatabaseDAO):

  def __init__(self, dataWorkbook: workbook.Workbook):
    super().__init__(dataWorkbook, WORKSHEET_NAME)


  def parse(self, row_index: int) -> dict:
    return TestStepDTO.from_tuple(next(self.worksheet.iter_rows(
      row_index,
      row_index,
      FIRST_COL_INDEX,
      self.worksheet.max_column,
      True )))


  def get_model_id(self, step: dict) -> str:
    return TestStep.get_id(step)


def create(dataWorkbook: workbook.Workbook) -> TestStepDAO:
  return TestStepDAO(dataWorkbook)


