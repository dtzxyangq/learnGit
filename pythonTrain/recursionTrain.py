#!/usr/bin/env python3

def move(n,a,b,c):
    if n == 1 :
        print(a, '-->', c)
    else:#lif n%2 == 0:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
    #else:

    return 0

#move(2,'A','B','C')
move(3,'A','B','C')
