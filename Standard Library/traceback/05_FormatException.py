import traceback
import sys

try:
    1/0
except ZeroDivisionError:
    print(repr(traceback.format_exception(*sys.exc_info())))
