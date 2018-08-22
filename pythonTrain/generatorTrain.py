#!/usr/bin/env python3
def triangles():
    L = [1]
    while True:
        yield L
        print(results)
        length, i = len(L), len(L)-1
        #L = [1] + [L[i]+L[i-1] for i in range(1,length)]
        L = L[:]#巨坑！浅拷贝与直接操作修改赋值的区别！
        while i > 0:
            L[i] = L[i] + L[i-1]
            i = i - 1
        L = L + [1]

    return 'Done'



n = 0
results = []
for t in triangles():
    print(t)

    results.append(t)
    print(results,"\n")

    n = n + 1
    if n == 10:
        break

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')



