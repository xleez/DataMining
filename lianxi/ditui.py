def age(n):
    if n == 1:
        i = 10
    else:
        i = age(n-1) + 2
    return i
print age(5)
