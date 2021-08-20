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
from libs.domain.entity.test_case import TestCase


WORKSHEET_NAME: Final[str] = "Sheet1"


class TestCaseDAO(DataAccessObjectI.DataAccessObjectI):

  def __init__(self, dataWorkbook: workbook.Workbook):
    self.dataWorkbook = dataWorkbook


  # TODO!!!
  def read(
      self,
      id: Optional[str]=None
      ) -> Union[None, TestCase.Model, List[TestCase.Model]]:
    return [] if id == None else None


def create(dataWorkbook: workbook.Workbook) -> TestCaseDAO:
  return TestCaseDAO(dataWorkbook)