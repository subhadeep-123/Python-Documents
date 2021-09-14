from typing import Callable


def do_twice(func: Callable[[str], str], arguments: str) -> None:
    print(func(arguments))
    print(func(arguments))

def create_greetings(name: str) -> str:
    return f"Hello {name}"

do_twice(create_greetings, "Jekyll")
