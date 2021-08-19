# Standard Libs
import io
from typing import (
  Optional,
  Final,
  Union,
  List)

# Third Party (Site) Libs
import openpyxl.workbook.workbook as workbook

# Local Libs
from libs.infrastructure.data_access_object.dao_interface import DataAccessObjectI
from libs.domain.entity.test_step import TestStep


WORKSHEET_NAME: Final[str] = "Sheet1"


class TestStepDAO(DataAccessObjectI.DataAccessObjectI):

  def __init__(self, dataWorkbook: workbook.Workbook):
    self.dataWorkbook = dataWorkbook


  # TODO!!!
  def read(
      self,
      id: Optional[str]=None
      ) -> Union[None, TestStep.Model, List[TestStep.Model]]:
    return None


def create(dataWorkbook: workbook.Workbook) -> TestStepDAO:
  return TestStepDAO(dataWorkbook)


