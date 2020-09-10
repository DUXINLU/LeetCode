import sys

n = int(sys.stdin.readline().strip())
color = sys.stdin.readline().strip()
number = list(map(int, list(sys.stdin.readline().strip().split(' '))))

ans = 0

# 第一遍先来黑的
for i in range(2 * n):
    if color[i] == 'R':
        continue
    flag = 0
    for j in range(2 * n - i - 1):
        for k in range(j, 2 * n - i - 1):
            if color[j] == 'R':
                flag += 1
                continue
