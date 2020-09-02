def f(s):
    l = len(s)
    if len(s) < 2:
        return l

    _ = []
    max_len = -1
    for i in range(l):
        if s[i] not in _:
            _.append(s[i])
        else:
            _ = _[_.index(s[i]) + 1:]
            _.append(s[i])
        if len(_) > max_len:
            max_len = len(_)

    return max_len


print(f('bbbbb'))
