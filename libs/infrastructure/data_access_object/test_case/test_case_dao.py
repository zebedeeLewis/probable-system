# Standard Libs
import io
from typing import (
  Optional,
  Union,
  List)

# Third Party (Site) Libs

# Local Libs
from libs.infrastructure.data_access_object.dao_interface import DataAccessObjectI
from libs.domain.entity.test_case import TestCase


class TestCaseDAO(DataAccessObjectI.DataAccessObjectI):

  def __init__(self, f: io.StringIO):
    self.file = f


  # TODO!!!
  def read(
      self,
      id: Optional[str]=None
      ) -> Union[None, TestCase.Model, List[TestCase.Model]]:
    return [] if id == None else None



def create(f: io.StringIO) -> TestCaseDAO:
  return TestCaseDAO(f)
