#!/usr/bin/env python3

def is_palindrome(n):
    s = str(n)
    if s == s[::-1]:
        return True
    return False
#或者
#is_palindrome = lambda n : str(n) == str(n)[::-1]

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')


def __odd_num():
    n = 3
    while True:
        yield n
        n = n + 2

def __not_divisable(n):
    return lambda x: x % n > 0 #筛选函数的定义非常重要！lambda表达与filter和map reduce

def prime():
    yield 2
    prime_ge = __odd_num()
    while True:
        now = next(prime_ge)
        yield now
        prime_ge = filter(__not_divisable(now),prime_ge)

for i in prime():
    if (i>100):
        break
    else:
        print(i)
