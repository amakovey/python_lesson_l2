import sys

s = 'ÄèÄèÄèÄè'
print(s.encode())
t = s.encode('cp500')
print(t)
# print(s.encode('cp866'))
# print(s.encode('latin-1'))
print(t.decode('cp500'))
print(t.decode())

print(sys.getdefaultencoding())
