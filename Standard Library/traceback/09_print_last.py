import traceback
import sys


print(1/0)

# Run it after raising exception in console
traceback.print_last(file=sys.stdout)
