#-*- coding:utf-8 -*-
if __name__ == "__main__":
    n = int(input("请输入你的数组个数:"))

    a = []
    for i in range(n):
      a.append(int(raw_input("请输入数组的值:")))
#排序
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
             if a[min] > a[j]:   min = j
        a[i],a[min] = a[min],a[i]
    print "after sorted"
    for i in range(n):
        print a[i]


# if __name__ == "__main__":
#     N = 10
#     print 'please input ten num:\n'
#     l = []
#     for i in range(N):
#         l.append(int(raw_input('input a number:\n')))
#     print
#     for i in range(N):
#         print l[i]
#     print
#
#     # sort ten num
#     for i in range(N - 1):
#         min = i
#         for j in range(i + 1, N):
#             if l[min] > l[j]: min = j
#         l[i], l[min] = l[min], l[i]
#     print 'after sorted'
#     for i in range(N):
#         print l[i]