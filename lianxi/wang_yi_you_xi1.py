def strcount(str1):
    result = []
    item = str1[0]
    count = 1
    for i in str1[1:]:
        if i == item:
            count += 1
        else:
            result.append(item + str(count))
            item = i
            count = 1
    result.append(item + str(count))
    return result


print(strcount('AAAABCCDAA'))