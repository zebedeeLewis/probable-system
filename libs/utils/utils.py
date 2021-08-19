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
from toolz import curry, apply as _apply


concat = curry(_concat)
cmap = curry(map)


@curry
def reduce(fn, init_value, iterable):
  return _reduce(fn, iterable, init_value)


@curry
def append_to(lst: List, x: Any) -> List:
  return [*lst, x]


@curry
def append(x: Any, lst: List) -> List:
  return append_to(lst, x)


@curry
def log_pipe(msg, x):
  pp = PrettyPrinter(indent=2)
  print("DEBUG: {}: ".format(msg))
  pp.pprint(x)
  return x


@curry
def debug_pipe(x):
  pdb.set_trace()
  return x


@curry
def apply_to(x: Any, fn: Callable) -> Any:
  return fn(x)


on: Final[Callable] = apply_to


@curry
def apply(fn: Callable, arg: Any) -> Any:
  return apply_to(arg, fn)
