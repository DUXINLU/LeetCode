max_ = -1


def f(num):
    global max_
    if len(num) == 1:
        if num[0] > max_:
            max_ = num[0]
        return
    if len(num) == 0:
        return

    min_ = min(num)
    min_index = num.index(min_)
    _ = min_ * len(num)
    if _ > max_:
        max_ = _
    f(num[:min_index])
    f(num[min_index + 1:])


f([2, 1, 5, 6, 2, 3])
print(max_)
