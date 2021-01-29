import traceback
import sys

try:
    1/0
except Exception as e:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print(
        f'exc_type : {exc_type}  |  exc_value : {exc_value}  | exc_traceback : {exc_traceback}')
    traceback.print_tb(exc_traceback, file=sys.stdout)

print("Statements after Try.......")
