import sys
try:
    1/0
except Exception as e:
    print(f"Exception : {e.__class__}")
    print(f"Value     : {e.args[0]}")
    print(f"Traceback : {e.__traceback__}, type : {type(e.__traceback__)}")
    print(
        f"Frame     : {e.__traceback__.tb_frame} type : {type(e.__traceback__.tb_frame)}")

    print("Using sys to extract info about last exception")
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print(f"exc_type      : {exc_type}, type {type(exc_type)}")
    print(f"exc_value     : {exc_value}, type {type(exc_value)}")
    print(f"exc_traceback : {exc_traceback}, type {type(exc_traceback)}")
