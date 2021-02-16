def add(a, b):
    """
    >>> add(2, 3)
    5
    >>> add(100,200)
    300
    """
    return a + b


def double(values):
    """ double the values in a list

    >>> double([1,2,3,4])
    [2, 4, 6, 8]

    >>> double([])
    []

    >>> double(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> double([True, None])
    Traceback (most recent call last):
            ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * element for element in values]

# Doctests can only compare to single quoted strings


def say_hi():
    """
    >>> say_hi()
    'hi'
    """
    return "hi"

# Watch out for whitespace!
# (There's a trailing space on line 42)


def true_that():
    """
    >>> true_that()
    True
    """
    return True

# Order of keys in dicts matters in doctests


def make_dict(keys):
    """
    >>> make_dict(['a','b'])
    {'b': True, 'a': True}
    """
    return {key: True for key in keys}
