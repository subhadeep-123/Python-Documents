from struct import Struct

struct1 = Struct('@i13sf')
sendBytes = b'\x7f\x00\x00\x00Hello Struct!\x00\x00\x00\xc3\xf5H@\x80\x00\x00\x00Hello Python!\x00\x00\x00\x85\xebQ@'

print(struct1.unpack_from(sendBytes, 24))
