import sys

n, m = list(map(int, sys.stdin.readline().strip().split(' ')))

group = []
start = -1
ans = 0

for i in range(m):
    group.append(list(map(int, sys.stdin.readline().strip().split(' ')))[1:])
    if 0 in group[-1]:
        start = group.index(group[-1])

queue = group[start]
ed = []
group.remove(queue)

while queue:
    t = queue.pop()
    if t not in ed:
        ans += 1
        ed.append(t)
    else:
        continue
    for _ in range(len(group)):
        if t in group[_]:
            tmp_queue = group[_]
            group[_] = []
            for tmp in tmp_queue:
                if tmp not in queue:
                    queue.append(tmp)

print(ans)
