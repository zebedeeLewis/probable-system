# Standard Libs
import pdb
from typing import (
  TypedDict,
  Final,
  List,
  Callable)
from enum import Enum

# Third Party (Site) Libs
from toolz import (
  curry,
  pipe as _,
  assoc)

# Local Libs
from libs.utils import Utils as U
from libs.test_case import TestCase


# TODO!!!
class Model(TypedDict):
  pass


RootModel: Final[Model] = {}


# TODO!!!
def load(file_name: str) -> Model:
  return RootModel


# TODO!!!
def to_test_cases(source: Model) -> List[TestCase.Model]:
  return [TestCase.RootModel]
