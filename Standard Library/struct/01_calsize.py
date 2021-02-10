import struct
print(f"calsize('i13sf') : {struct.calcsize('i13sf')}")
print(f"calsize('13si): {struct.calcsize('13si')}")
print(struct.pack('13si', b'Hello World!', 127))
print(f"calsize('i13s) :", struct.calcsize('i13s'))
print(struct.pack('i13s', 127, b'Hello World!'))
