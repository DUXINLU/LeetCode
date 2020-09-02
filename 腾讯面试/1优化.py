def func(str):
    str = list(str)
    flag = 0
    for i in range(len(str) - 2):
        if flag:
            flag -= 1
            continue
        if str[i] == str[i + 2]:
            if str[i] == str[i + 1]:
                flag = 1
            else:
                str[i:i + 3] = list('...')
                flag = 2

    ans = ''
    for i in str:
        ans += i
    return ans


print(func('abcxxxdfdllyx'))
