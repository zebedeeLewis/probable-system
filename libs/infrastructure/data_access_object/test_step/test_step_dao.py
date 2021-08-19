# Standard Libs
import io
from typing import (
  Optional,
  Union,
  List)

# Third Party (Site) Libs

# Local Libs
from libs.infrastructure.data_access_object.dao_interface import DataAccessObjectI
from libs.domain.entity.test_step import TestStep


class TestStepDAO(DataAccessObjectI.DataAccessObjectI):

  def __init__(self, f: io.StringIO):
    self.file = f


  # TODO!!!
  def read(
      self,
      id: Optional[str]=None
      ) -> Union[None, TestStep.Model, List[TestStep.Model]]:
    return None


# TODO!!!
def create(f: io.StringIO) -> TestStepDAO:
  pass


