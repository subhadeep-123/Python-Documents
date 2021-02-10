import struct

byteorder = {
    'default(native)': 'i13sf',
    'native(explicit)': '@i13sf',
    'little-endian': '<i13sf',
    'big-endian': '>i13sf'
}
for formatting in byteorder:
    sendBytes = struct.pack(byteorder[formatting], 127, b'Hello World', 3.14)
    print(f"{formatting} ['{byteorder[formatting]}'] ==> {sendBytes}")
