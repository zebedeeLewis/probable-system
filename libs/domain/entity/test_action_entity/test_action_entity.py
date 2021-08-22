# Standard Libs
import pdb
import typing as T

# Third Party (Site) Libs
import toolz as Z
from toolz import pipe as _

# Local Libs


ActionRunner = T.Callable[[T.Optional[T.Any]], T.Union[None, T.Any]]


class Model(T.TypedDict):
  id          : str
  name        : str
  description : str
  runner      : ActionRunner


def default_runner(data: T.Optional[T.Any]) -> T.Union[None, T.Any]:
  assert False
  return None


RootModel: T.Final[Model] = {
  "id"          : "default-action-id",
  "name"        : "default action",
  "description" : "default action does nothing",
  "runner"      : default_runner,
}


@Z.curry
def set_id(id: str, test_action: Model) -> Model:
  return Z.assoc(test_action, 'id', id)


def get_id(model: Model) -> str:
  return model.get('id')


@Z.curry
def set_name(name: str, test_action: Model) -> Model:
  return Z.assoc(test_action, 'name', name)


def get_name(model: Model) -> str:
  return model.get('name')


@Z.curry
def set_description(description: str, test_action: Model) -> Model:
  return Z.assoc(test_action, 'description', description)


def get_description(model: Model) -> str:
  return model.get('description')


@Z.curry
def set_runner(runner: T.Callable, test_action: Model) -> Model:
  return Z.assoc(test_action, 'runner', runner)


def get_runner(model: Model) -> T.Callable:
  return model.get('runner')

