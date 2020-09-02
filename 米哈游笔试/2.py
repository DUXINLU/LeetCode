import sys

m, n = sys.stdin.readline().strip().split()
m, n = int(m), int(n)

if m < n:
    print('NO')

matrix = []
for i in range(m):
    matrix.append(list(map(int, sys.stdin.readline().strip().split())))

ans_matrix = [None for i in range(n)]
for i in range(m):
    if matrix[i].count(1) != 1:
        continue
    else:
        ans_matrix[matrix[i].index(1)] = matrix[i]


def isDJZ(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] != 1:
            return False
    return True


if isDJZ(ans_matrix):
    print('YES')
else:
    print('NO')
