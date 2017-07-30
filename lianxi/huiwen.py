#-*- coding:utf-8 -*-
a = int(raw_input("请输入数值:"))
x = str(a)
flag = True
for i in range(len(x)/2):
    if x[i] != x[-i-1]:
        flag = False
        break
if flag:
    print "%d 是一个回文数:" % a
else:
    print "%d 不是一个回文数:" % a