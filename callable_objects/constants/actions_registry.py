from typing import TypeAlias

from callable_objects.constants.actions import Actions
from callable_objects.handlers.some_handler_1 import SomeHandler1
from callable_objects.handlers.some_handler_2 import SomeHandler2
from callable_objects.handlers.some_handler_3 import SomeHandler3
from callable_objects.handlers_base.base_handler import BaseHandler

T_REGISTRY: TypeAlias = dict[Actions, type[BaseHandler]]

REGISTRY: T_REGISTRY = {
    Actions.ACTION_1: SomeHandler1,
    Actions.ACTION_2: SomeHandler2,
    Actions.ACTION_3: SomeHandler3,
}

# noinspection Assert
assert len(REGISTRY) == len(Actions), 'Not all actions in registry.'
