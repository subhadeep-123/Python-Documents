import traceback
import sys


def division():
    try:
        1/0
    except ZeroDivisionError:
        traceback.print_stack(file=sys.stdout)


division()
