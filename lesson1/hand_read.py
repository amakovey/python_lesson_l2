with open('test', 'w', encoding='utf-8') as f:
    f.write('abcdefghijklmnopабвгдаежз')

with open('test', 'rb') as f:
    text = f.read()
    for i in text[:6]:
        print(i)
        print(hex(i))
        print(bin(i))
    for i in text[15:]:
        print(i)