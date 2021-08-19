# Standard Libs
import pdb
from pprint import PrettyPrinter
from functools import reduce as _reduce
from operator import concat as _concat
from typing import (
  List,
  Any,
  Final,
  Callable)

# Third Party (Site) Libs
import toolz as T


concat = T.curry(_concat)
cmap = T.curry(map)


@T.curry
def reduce(fn, init_value, iterable):
  return _reduce(fn, iterable, init_value)


@T.curry
def append_to(lst: List, x: Any) -> List:
  return [*lst, x]


@T.curry
def append(x: Any, lst: List) -> List:
  return append_to(lst, x)


@T.curry
def log_pipe(msg, x):
  pp = PrettyPrinter(indent=2)
  print("DEBUG: {}: ".format(msg))
  pp.pprint(x)
  return x


@T.curry
def debug_pipe(x):
  pdb.set_trace()
  return x


@T.curry
def apply_to(x: Any, fn: Callable) -> Any:
  return fn(x)


on: Final[Callable] = apply_to


@T.curry
def apply(fn: Callable, arg: Any) -> Any:
  return apply_to(arg, fn)
