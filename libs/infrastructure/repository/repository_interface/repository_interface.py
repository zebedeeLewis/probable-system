# Standard Libs
import pdb
import abc
from typing import (
  Final,
  NoReturn,
  List)

# Third Party (Site) Libs
import toolz as T
from toolz.itertoolz import last
from toolz import pipe as _

# Local Libs
from libs.utils.misc import MiscUtils as U


#TODO!!!
class RepositoryI(abc.ABC):

  @abc.abstractmethod
  def get(self):
    pass
