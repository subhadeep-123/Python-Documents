def do_stuff(num=0):
    try:
        if int(num) < 0:
            raise ValueError("Cannot be less than zero")
        else:
            return int(num) + 5
    except Exception as err:
        return err


if __name__ == '__main__':
    a = do_stuff()
    print(a)
