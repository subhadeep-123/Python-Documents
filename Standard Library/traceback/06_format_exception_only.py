import traceback
import sys

try:
    1/0
except ZeroDivisionError:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print(repr(traceback.format_exception_only(exc_type, exc_value)))
