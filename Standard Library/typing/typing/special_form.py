from typing import Any, AnyStr, Callable, ClassVar, Final, List, Literal, Optional, Tuple, Union


# This a tuple defined with variable lenght
def print_tuple(data: Tuple[Any, ...]) -> None:
    print(data)


def test_union(a: Union[int, float], b: Union[int, float]) -> Union[bool, int, str]:
    try:
        if a == b:
            return True
        elif a < b:
            return -1
        elif a > b:
            return +1
        else:
            return False
    except Exception as err:
        return f"Error - {err}"


def test_optional(name: Optional[str] = None) -> Optional[str]:
    if name is None:
        return None
    return f"Hello {name}"


def test_callable(func: Callable, name: str) -> None:
    print(func(name))


test_callable(test_optional, name="Matrix")


def test_literals(file: str, mode: Literal['r', 'w', 'rb', 'wb']):
    if mode == 'r':
        with open(file, mode) as fp:
            print(fp.read())
    elif mode == 'w':
        with open(file, mode) as fp:
            fp.write("Hey, this is a text")


# class WithoutClassVars:
#     vardict = {}
#     print(vardict)
# obj = WithoutClassVars()
# obj.vardict = {"name": "matrix"}
# WithoutClassVars.vardict = {"val": 10}

class WithClassVars:
    vardict: ClassVar[dict[str, int]] = {}
    print(vardict)


obj = WithClassVars()
# obj.vardict = {"name": "matrix"}
WithClassVars.vardict = {"val": 10}


# Testing typing.Final
# MAX_SIZE: Final = 9000
# MAX_SIZE += 1
# print(MAX_SIZE)


# class Connection:
#     TIMEOUT: Final[List[int]] = [1,2,3,4,5,6]

# class FastConnector(Connection):
#     TIMEOUT = [50,30,40]

def concat(a: AnyStr, b: AnyStr) -> AnyStr:
    return a + b


concat(f"foo ", u"bar ")
concat(b"foo ", b"bar ")
concat(u"foo ", b"bar ")
