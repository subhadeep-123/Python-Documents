import struct

struct1 = struct.Struct('@i13sf')
print(f"Format - {struct1.format}")
print(f'Size : ', struct1.size)
