#-*- coding:utf-8 -*-
#计算题为2+22+222+2222的题目
s = 0
l = []
n = int(raw_input('n = :\n'))
a = int(raw_input('a = :\n'))
for count in range(n):
    s = s +a
    a = a * 10
    l.append(s)
    print(l)

l = reduce(lambda  x,y : x+y,l)
print l