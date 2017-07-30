#-*- coding:utf-8 -*-
import math
def jiecheng():
       n = input("please input n:")
       a = [0 for i in xrange(40000)]
       s = 0
       for k in range(2,n):
            global m
            s += math.log10(k)
            m = int(s)+1
            for k in range(1,m):
                a[k] = 0
       a[1]=1
       g = 0
       for k in range(2,n):
           for j in range(1,m):
               t = a[j]*k+g
               a[j]  = t%10
               g = t/10
       print("%d!=",n)
       for i in range(m,1,-1):
           print(a[i])
       print("共%d位",m)



jiecheng()

