import os


class FilePlay(object):

    def __init__(self, fname, lname, age):
        self.first = fname
        self.last = lname
        self.age = age
        self.filename = input("Enter the filename: ")
        self.folder = input("Enter the Folder name: ")
        self.folder = f"C:\\Users\\{os.getlogin()}\\{self.folder}"
        self.path = os.path.join(self.folder, self.filename)

    def __str__(self):
        return f"{self.first} {self.last} - {self.age}"

    def onlyRead(self):
        if os.path.exists(self.path):
            if os.path.isfile(os.path.join(self.folder, self.filename)):
                path = os.path.join(self.folder, self.filename)
                with open(path, 'r') as f:
                    print(f.read())

    def dataEntry(self):
        data_dir = {
            "First Name": self.first,
            "Last Name": self.last,
            "Age": self.age
        }
        return str(data_dir)

    def doWrite(self):
        if os.path.exists(self.path) and os.path.isfile(self.path) and (os.path.getsize(self.path) > 0):
            with open(self.path, 'a') as f:
                f.write(self.dataEntry())
                f.write('\n')
                print("The text in the file")
                self.onlyRead()
        else:
            path = os.path.join(self.folder, self.filename)
            with open(path, 'w') as f:
                f.write(self.dataEntry())
                print("The text in the file")
                self.onlyRead()


if __name__ == '__main__':
    obj = FilePlay("Iam", "Matrix", 21)
    obj.doWrite()
