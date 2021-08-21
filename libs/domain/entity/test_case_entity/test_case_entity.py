# Standard Libs
import pdb
import typing as T
from enum import Enum

# Third Party (Site) Libs
import toolz as Z
from toolz.itertoolz import last
from toolz import pipe as _

# Local Libs
from libs.utils.misc import MiscUtils as U
from libs.domain.entity.test_step import TestStep


ListOfSteps = T.List[TestStep.Model]


class ExecutionState(Enum):
  PENDING    = 'PENDING'
  RUNNING    = 'RUNNING'
  SUCCESSFUL = 'SUCCESSFUL'
  FAILED     = 'FAILED'


class Model(T.TypedDict):
  id               : str
  description      : str
  steps            : T.Union[T.List[str], T.List[TestStep.Model]]
  execution_state  : ExecutionState


RootModel: T.Final[Model] = {
  "id"               : "default-test-id",
  "description"      : "this is the default test",
  "execution_state"  : ExecutionState.PENDING,
  "steps"            : [TestStep.RootModel],
}


@Z.curry
def set_execution_state(
    execution_state: ExecutionState,
    test_case: Model) -> Model:
  return Z.assoc(test_case, 'execution_state', execution_state)


def get_execution_state(model: Model) -> ExecutionState:
  return model.get('execution_state')


@Z.curry
def set_steps(steps: ListOfSteps, test_case: Model) -> Model:
  return Z.assoc(test_case, 'steps', steps)


def get_steps(model: Model) -> ListOfSteps:
  return model.get('steps')


@Z.curry
def set_description(description: str, test_case: Model) -> Model:
  return Z.assoc(test_case, 'description', description)


def get_description(model: Model) -> str:
  return model.get('description')


@Z.curry
def set_id(id: str, test_case: Model) -> Model:
  return Z.assoc(test_case, 'id', id)


def get_id(model: Model) -> str:
  return model.get('id')


@Z.curry
def append_step(step: TestStep.Model, test_case: Model) -> Model:
  return _( test_case
          , get_steps
          , U.append(step)
          , set_steps
          , U.on(test_case))


@Z.curry
def to_applied_steps(
    steps: ListOfSteps,
    current_step: TestStep.Model
    ) -> ListOfSteps:
  if len(steps) < 1:
    return _( current_step
            , TestStep.set_data(None)
            , TestStep.apply
            , U.append_to(steps))
  else:
    return _( steps
            , last
            , TestStep.pipe_data_to_result
            , U.on(current_step)
            , TestStep.apply
            , U.append_to(steps))


def apply_steps(test_case: Model) -> Model:
  return _( test_case
          , get_steps
          , U.reduce(to_applied_steps, [])
          , set_steps
          , U.on(test_case))


def take_last_step_execution_state(test_case: Model) -> Model:
  return _( test_case
          , get_steps
          , last
          , TestStep.get_execution_state
          , set_execution_state
          , U.on(test_case))


def has_steps(test_case: Model) -> bool:
  return _(test_case, get_steps, len) < 1


def run(test_case: Model) -> Model:
  return  (test_case if has_steps(test_case)
    else _( test_case
          , apply_steps
          , take_last_step_execution_state))

