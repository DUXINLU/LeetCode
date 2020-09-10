import sys

n, k = list(map(int, sys.stdin.readline().strip().split(' ')))
strs = []
str_count = []

for i in range(n):
    strs.append(sys.stdin.readline().strip())

while strs:
    c = strs.count(strs[0])
    str_count.append([strs[0], c])
    for i in range(c):
        strs.remove(strs[0])

str_count_max = sorted(str_count, key=lambda i: i[1], reverse=True)
max_ans = []
for i in range(k):
    _ = str_count_max.pop(0)
    try:
        flag = None
        for j in range(len(max_ans, -1, -1)):
            if _[1] == max_ans[j][1] and _[0] < max_ans[j][0]:
                flag = j
    except:
        pass
    if flag == None:
        max_ans.append(_)
    else:
        max_ans.insert(flag, _)

for i in range(k):
    print('%s %d' % (max_ans[i][0], max_ans[i][1]))

str_count_min = sorted(str_count, key=lambda i: i[1])
min_ans = []
for i in range(k):
    _ = str_count_min.pop(0)
    try:
        flag = None
        for j in range(len(min_ans, -1, -1)):
            if _[1] == min_ans[j][1] and _[0] < min_ans[j][0]:
                flag = j
    except:
        pass
    if flag == None:
        min_ans.append(_)
    else:
        min_ans.insert(flag, _)

for i in range(k):
    print('%s %d' % (min_ans[i][0], min_ans[i][1]))
