import traceback
import sys


class InvalidAccessError(Exception):
    pass


def func1():
    print('func1() Started...')
    func2()
    print('func1() Ended...')


def func2():
    try:
        raise AttributeError
    except AttributeError as e:
        raise InvalidAccessError('Caution! Invalid access detected.') from None


try:
    func1()
except InvalidAccessError as e:
    for line in traceback.extract_tb(sys.exc_info()[2]):
        print(line)
