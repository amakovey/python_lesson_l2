f = open('latindata', 'w', encoding='latin-1')
f.write('A\xc4B\xe8C')
f.close()

f = open('utf8data', 'w', encoding='utf-8')
f.write('A\xc4B\xe8C')
f.close()

f = open('latindata', 'rb')
print(f.read())
f.close()

f = open('utf8data', 'rb')
print(f.read())
f.close()

f = open('latindata', 'r', encoding='latin-1')
print(f.read())
f.close()

f = open('utf8data', 'r', encoding='utf-8')
print(f.read())
f.close()

f = open('utf8data', 'r', encoding='latin-1')
print(f.read())
f.close()