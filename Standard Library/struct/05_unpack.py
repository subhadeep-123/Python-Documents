from struct import Struct

FORMAT = '@i13sf'
struct1 = Struct(FORMAT)
sendBytes = b'\x7f\x00\x00\x00Hello Struct!\x00\x00\x00\xc3\xf5H@'
org = struct1.unpack(sendBytes)
print(org)

