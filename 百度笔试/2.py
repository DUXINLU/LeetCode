import sys

n, m, k = sys.stdin.readline().strip().split()
n, m, k = map(int, [n, m, k])

goods = []

for i in range(n):
    goods.append(list(map(int, sys.stdin.readline().strip().split())))

goods = sorted(goods, key=lambda i: i[2], reverse=True)


def f(p, w, v):
    n = len(p)
    lists, arr = [], [[0] * (v + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, v + 1):
            if w[i - 1] <= j:
                arr[i][j] = max(arr[i - 1][j], p[i - 1] + arr[i - 1][j - w[i - 1]])
            else:
                arr[i][j] = arr[i - 1][j]
    remain = v

    for i in range(n, 0, -1):
        if arr[i][remain] > arr[i - 1][remain]:
            lists.append(i - 1)
            remain -= w[i - 1]

    return arr[-1][-1], lists

