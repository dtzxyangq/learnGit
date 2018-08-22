#!/usr/bin/env python3
def findMinAndMax(L):
    if L == []:
        return (None,None)
    a = L[0]
    b = L[0]
    for x in L:
        if (a > x):
            a = x
        if (b < x):
            b = x
    return (a , b)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

L = (1, 2, 3, [1,2,3])
from collections import Iterable
if isinstance(L,Iterable):
    print ('yes')

L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s,str)])
