# Standard Libs
import pdb
import abc
from typing import (
  Optional,
  List)

# Third Party (Site) Libs
import toolz as T
from toolz.itertoolz import last
from toolz import pipe as _

# Local Libs
from libs.utils.misc import MiscUtils as U


class DataAccessObjectI(abc.ABC):

  @abc.abstractmethod
  def read(self, id: Optional[str]=None):
    pass
