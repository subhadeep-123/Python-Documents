import traceback

try:
    1/0
except ZeroDivisionError:
    print(traceback.format_exc())
