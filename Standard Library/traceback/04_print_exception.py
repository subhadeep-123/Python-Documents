import traceback
import sys

try:
    1/0
except ZeroDivisionError:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_exception(
        exc_type, exc_value, exc_traceback, file=sys.stdout)
