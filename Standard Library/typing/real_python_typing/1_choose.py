import random
from typing import Sequence, TypeVar, Any

T = TypeVar("T")


def choose(items: Sequence[T]) -> T:
    return random.choice(items)

# def choose(items: Sequence[Any]) -> Any:
#     return random.choice(items)


names = ["Guido", "Jukka", "Ivan"]
reveal_type(names)

name = choose(names)
reveal_type(name)

reveal_type(choose(["Guido", "Jukka", "Ivan"]))
reveal_type(choose([1, 2, 3]))
reveal_type(choose([True, 42, 3.14]))
reveal_type(choose(["Python", 3, 7]))
