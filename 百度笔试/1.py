import sys

x, y = sys.stdin.readline().strip().split(' ')
x, y = map(int, [x, y])

ops = sys.stdin.readline().strip()

for op in ops:
    if op == 'U':
        y += 1
        continue
    if op == 'D':
        y -= 1
        continue
    if op == 'L':
        x -= 1
        continue
    if op == 'R':
        x += 1
        continue

print("%d %d" % (x, y))
