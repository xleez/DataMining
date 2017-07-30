#-*- coding:utf-8 -*-
#原先规律的数组
a = [1,3,4,6,9,23,56,98,0]
# for i in range(len(a)):
#     print(a[i])
#键盘获取要得到的数值
number = raw_input('请输入要插入的数值:')
#判断是否大于最后一个数
end = a[len(a)-1]
print('###############')
print(end)
print('#############')



if  number > end:
    a[7] = number
else:
    for i in range(len(a)):
        if(number > a[i]):
            temp1 = a[i]
            a[i] = number
            for j in range(i+1,len(a)):
                temp2 = a[j]
                a[j] = temp1
                temp1 = temp2
            break


for i in  range(len(a)):
    print (a[i])