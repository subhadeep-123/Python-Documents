import tempfile


def one():
    file = tempfile.mkstemp()
    with open(file[1], 'w+') as f:
        f.write("This is a test")
        f.seek(0)
        print(f.read())


print(tempfile.gettempdir())
print(tempfile.gettempdirb())
print(tempfile.gettempprefix())
print(tempfile.gettempprefixb())
print(tempfile.tempdir)
