from struct import Struct

struct1 = Struct('@i13sf')
buffer = bytearray(56)

struct1.pack_into(buffer, 0, 129, b'Hello World', 4.69)
struct1.pack_into(buffer, 24, 130, b'Yoo Python!', 3.28)
print(f"Butter : {buffer}")
