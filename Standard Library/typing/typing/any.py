from typing import Any, List

a = None    # type: Any
a = []      # OK
a = 2       # OK

s = ''      # type: str
s = a       # OK


def foo(item: Any) -> str:
    item.bar()
    return "Hello"
