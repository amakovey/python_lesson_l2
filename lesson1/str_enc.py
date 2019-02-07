print(chr(0xc4))

print(ord('Ä'))
print(chr(196))
print(hex(196))

print(chr(0xe8))

s = '\xc4\xe8'
print(s)

print(int('0xc4', 16))

s = '\u00c4\u00e8'
print(s)

print(len(s))

# print(s.encode('ascii'))
print(s.encode('latin-1'))
print(s.encode('utf-8'))

print(len(s.encode('latin-1')))
print(len(s.encode('utf-8')))