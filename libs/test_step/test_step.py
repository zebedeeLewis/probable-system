# Standard Libs
import pdb
from typing import (
  Any,
  Final,
  Optional,
  TypedDict,
  Callable)
from enum import Enum

# Third Party (Site) Libs
from toolz.functoolz import apply
from toolz import (
  curry,
  pipe as _,
  assoc)

# Local Libs
from libs.utils import Utils as U


StepRunner = Callable[[Optional[Any]], Optional[Any]]


class ExecutionState(Enum):
  PENDING    = 'PENDING'
  RUNNING    = 'RUNNING'
  SUCCESSFUL = 'SUCCESSFUL'
  FAILED     = 'FAILED'


class Model(TypedDict):
  id               : str
  test_id          : str
  name             : str
  description      : str
  runner           : StepRunner
  execution_state  : ExecutionState
  result           : Optional[Any]
  data             : Optional[Any]


def default_runner(data: Any):
  assert False
  return None


RootModel: Final[Model] = {
  "id"               : "default-step-id",
  "test_id"          : "default-test-id",
  "name"             : "default step",
  "description"      : "default step does nothing",
  "execution_state"  : ExecutionState.PENDING,
  "runner"           : default_runner,
  "result"           : None,
  "data"             : "random data",
}


@curry
def set_name(name: str, test_step: Model) -> Model:
  return assoc(test_step, 'name', name)


def get_name(model: Model) -> str:
  return model.get('name')


@curry
def set_execution_state(
    execution_state: ExecutionState,
    test_step: Model
    ) -> Model:
  return assoc(test_step, 'execution_state', execution_state)


def get_execution_state(model: Model) -> ExecutionState:
  return model.get('execution_state')


@curry
def set_result(result: Any, test_step: Model) -> Model:
  return assoc(test_step, 'result', result)


def get_result(model: Model) -> Any:
  return model.get('result')


@curry
def set_data(data: Any, test_step: Model) -> Model:
  return assoc(test_step, 'data', data)


def get_data(model: Model) -> Any:
  return model.get('data')


def set_description(description: str, test_step: Model) -> Model:
  return assoc(test_step, 'description', description)


def get_description(model: Model) -> str:
  return model.get('description')


@curry
def set_id(id: str, test_step: Model) -> Model:
  return assoc(test_step, 'id', id)


def get_id(model: Model) -> str:
  return model.get('id')


@curry
def set_test_id(test_id: str, test_step: Model) -> Model:
  return assoc(test_step, 'test_id', test_id)


def get_test_id(model: Model) -> str:
  return model.get('test_id')


@curry
def set_runner(runner: Callable, test_step: Model) -> Model:
  return assoc(test_step, 'runner', runner)


def get_runner(model: Model) -> Callable:
  return model.get('runner')


def apply_runner_to_data(test_step: Model) -> Any:
  return U.apply(
    get_runner(test_step), 
    get_data(test_step),
  )


def apply_runner_and_set_result(test_step: Model) -> Model:
  return _( test_step
          , apply_runner_to_data
          , set_result
          , U.on(test_step))


def apply(test_step: Model) -> Model:
  try:
    return _( test_step
            , set_execution_state(ExecutionState.RUNNING)
            , apply_runner_and_set_result
            , set_execution_state(ExecutionState.SUCCESSFUL))

  except Exception as err:
    # TODO: have some kind of flag to determine if test failure
    # should throw or just mark test as failed.
    if (True):
      raise err

    return set_execution_state(ExecutionState.FAILED, test_step)


def has_data(test_step: Model) -> bool:
  return True if get_data(test_step) != None else False


@curry
def pipe_data_to_result(
    stepA: Model,
    stepB: Model
    ) -> Model:
  return (stepB if _(stepB, has_data)
    else _( stepA
          , get_result
          , set_data
          , U.on(stepB)))

