import sys

s = sys.stdin.readline()
print(len(s))
k = 0
ans = []

while k < len(s):
    tmp = s[k:k + 1024]
    for i in range(len(tmp) - 1, -1, -1):
        if tmp[i] in [',', '.', ';', '!', '\n']:
            ans.append(tmp[:i + 1])
            k = k + i + 1
            break

print()
for i in ans:
    print(i)
