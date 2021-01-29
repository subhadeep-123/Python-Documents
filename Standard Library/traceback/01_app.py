try:
    1/0
except Exception as e:
    print('e : ', e)
    print(f"repr(e) : {repr(e)}")
