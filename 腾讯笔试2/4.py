import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, list(sys.stdin.readline().strip().split(' '))))

arr_sorted = sorted(arr)

l, r = arr_sorted[(n // 2) - 1], arr_sorted[n // 2]

mid = (l + r) / 2

for i in arr:
    if i < mid:
        print(r)
    else:
        print(l)
