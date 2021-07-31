def example(express, result=None):
    if result == None:
        result = eval(express)
    print(express, ' ==> ', result)


print('字符串转字节串:')
print('字符串编码为字节码', end=": ");
example(r"'12abc'.encode('ascii')")
print('数字或字符数组', end=": ");
example(r"bytes([1,2, ord('1'),ord('2')])")
print('16进制字符串', end=': ');
example(r"bytes().fromhex('010210')")
print('16进制字符串', end=': ');
example(r"bytes(map(ord, '\x01\x02\x31\x32'))")
print('16进制数组', end=': ');
example(r'bytes([0x01,0x02,0x31,0x32])')
