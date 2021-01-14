import logging

a = 5
b = 0

try:
    c = a / b
except Exception as e:
    logging.exception(f"Exception occured {e} ")
# If exc_info was not set to true that the output would be like normal
# Exception catching.
