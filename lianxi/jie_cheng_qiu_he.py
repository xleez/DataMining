#-*- coding:utf-8 -*-
s = 0
l = range(1,21)
def f(x):
    r = 1
    for i in range(1,x+1):
        r *= i
    return r
s = sum(list(map(f,l)))
print('阶乘的和=%d' %s)