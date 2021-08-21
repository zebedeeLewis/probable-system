# Standard Libs
import pdb
import abc
import typing as T

# Third Party (Site) Libs

# Local Libs
from libs.utils.misc import MiscUtils as U


class DataAccessObjectI(abc.ABC):

  @abc.abstractmethod
  def read(self, id: T.Optional[str]=None):
    pass
