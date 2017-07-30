#-*- coding:utf-8 -*-

#定义一个数组
a = [[0 for i in range(3)] for j in range(3)]
#为数组赋值
for i in range(3):
    for j in range(3):
        a[i][j] = int(input('请输入值:'))

#计算数组对角线上的元素
sum = 0.0
for i in range(3):
    sum += a[i][i]
print sum