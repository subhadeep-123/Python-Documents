from logging import Logger
from typing import NewType, Type, TypeVar, Generic, Optional
from collections.abc import Sequence, Callable, Mapping, Iterable, Sized

def greetig(name: str) -> str:
    return f"Hello {name}"


# Type aliases
Vector = list[float]
def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


# complex aliases
ConnectionOption = dict[str,str]
Address = tuple[str, int]
Server = tuple[Address, ConnectionOption]
def broadcastMessage(message: str, servers: Sequence[Server]) -> None:
    ...
# This above function is same as
def static_broadcastMessage(
    message: str,
    servers: Sequence[tuple[tuple[str, str], dict[str,str]]]) -> None:
    ...


# NewType
UserId = NewType('UserId', int)
some_id = UserId(612621)
print(type(some_id), some_id)
def test_new_Type(userid: UserId) -> str:
    return f"User id is - {userid}"

print(test_new_Type(UserId(2045)))
print(test_new_Type(UserId(204554)))



# Callback Function
def feeder(get_next_item: Callable[[], str]) -> None:
    ...
def async_query(on_success: Callable[[int], None], on_error: Callable[[int, Exception], None]) -> None:
    ...



# Generics
class Employee:
    pass
def notity_by_email(employee: Sequence[Employee], overrides: Mapping[str, str]) -> None: ...

# Parameterized Generics with TypeVar
T = TypeVar('T')
def first(l: Sequence[T]) -> T:
    return l[0]

# Userdefined Generics
class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info("%s %s", self.name, message)

def zero_all_vars(vars: Iterable[LoggedVar[int]]) -> None:
    for var in vars:
        var.set(0)

# Generic with multiple typevars
S = TypeVar('S', int, str)
class StragePair(Generic[T, S]):
    ...

# Multiple Inheritance
class LinkedList(Sized, Generic[T]):
    ...