def qs(num):
    if len(num) < 2:
        return num
    key = num[len(num) // 2]
    num.remove(key)

    left, right = [], []
    for i in num:
        if i < key:
            left.append(i)
        else:
            right.append(i)
    return qs(left) + [key] + qs(right)


print(qs([4, 7, 2, 5, 9, 1, 10]))
