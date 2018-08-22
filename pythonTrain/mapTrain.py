#!/usr/bin/env python3

def normalize(name):
    # s1 = name[:1].upper()
    # s2 = name[1:].lower()
    return name[:1].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce
def prod(L):
    def multi(x,y):
        return x*y
    return reduce(multi,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

def str2float(s):
    digits = {'0':0, '1':1, '2':2, '3': 3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    def cut(s1):
        for i, ch in enumerate(s1):
            if ch == '.':
                break
        return s1[:i],s1[:i:-1]
    def ch2num(s2):
        return digits[s2]
    def num2int(x,y):
        return x*10+y
    def num2float(x,y):
        return x/10.0+y
    return reduce(num2int,map(ch2num,cut(s)[0])) + reduce(num2float,map(ch2num,cut(s)[1]))/10.0

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

s = '123.456'
print (s.split('.'))




