import traceback
import sys

try:
    1/0
except ZeroDivisionError:
    traceback.print_exc(file=sys.stdout)
