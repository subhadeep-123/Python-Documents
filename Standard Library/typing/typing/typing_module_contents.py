from typing import Any, NoReturn


def test_type_any(variable: Any) -> None:
    print(variable*variable)


def test_no_return() -> NoReturn:
    raise RuntimeError('Nope, No Way')
# test_no_return()
