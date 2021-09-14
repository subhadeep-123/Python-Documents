class TestMethod:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        return f"{self.name} - {self.email}"

    def __str__(self) -> str:
        return f"{self.email} - {self.name}"


test_method = TestMethod("Subhadeep", "subhadeep762@gmail.com")
print(str(test_method), repr(test_method))