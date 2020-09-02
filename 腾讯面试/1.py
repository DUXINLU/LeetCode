def func(str):
    str = list(str)
    for i in range(len(str) - 2):
        if str[i] == str[i + 2]:
            if str[i] == str[i + 1]:
                continue
            else:
                str[i:i + 3] = list('...')

    ans = ''
    for i in str:
        ans += i
    return ans


print(func('abcxxxdfdllyx'))
