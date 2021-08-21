# Standard Libs
import pdb
import typing as T
from pprint import PrettyPrinter
from functools import reduce as _reduce
from operator import concat as _concat

# Third Party (Site) Libs
import toolz as Z


concat = Z.curry(_concat)
_map = Z.curry(map)


@Z.curry
def _filter(fn: T.Callable, lst: T.List[T.Any]) -> T.List[T.Any]:
  return list(filter(fn, lst))


@Z.curry
def split_by(separator: str, data_str: str) -> T.List[str]:
  return data_str.split(separator)


@Z.curry
def reduce(fn, init_value, iterable):
  return _reduce(fn, iterable, init_value)


@Z.curry
def append_to(lst: T.List, x: T.Any) -> T.List:
  return [*lst, x]


@Z.curry
def append(x: T.Any, lst: T.List) -> T.List:
  return append_to(lst, x)


@Z.curry
def log_pipe(msg, x):
  pp = PrettyPrinter(indent=2)
  print("DEBUG: {}: ".format(msg))
  pp.pprint(x)
  return x


@Z.curry
def debug_pipe(x):
  pdb.set_trace()
  return x


@Z.curry
def apply_to(x: T.Any, fn: T.Callable) -> T.Any:
  return fn(x)


on: T.Final[T.Callable] = apply_to


@Z.curry
def apply(fn: T.Callable, arg: T.Any) -> T.Any:
  return apply_to(arg, fn)
