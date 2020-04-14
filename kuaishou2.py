def f():
    R, N = 25, 5

    ans = []

    x = 0

    while N ** x < R:
        x += 1

    while R > 0:
        while R >= N ** x:
            print(R, N, x, N ** x)
            R = R - N ** x
            if x in ans:
                return []
            ans.append(x)
        x -= 1

    ans.sort()
    return ans


print(f())
