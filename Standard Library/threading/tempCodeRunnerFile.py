it(do_something, 1)
    f2 = executer.submit(do_something, 1)
    print(f1.result())
    print(f2.result())