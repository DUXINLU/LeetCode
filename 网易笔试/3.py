import sys

t = sys.stdin.readline().strip().split()
s1 = sys.stdin.readline().strip().split()
s2 = sys.stdin.readline().strip().split()

for word in t:
    while word in s1:
        s1.remove(word)
    while word in s2:
        s2.remove(word)

ans = -1
if len(s1) == len(s2):
    ans = 0
else:
    ans = abs(len(s1) - len(s2))

for i in range(min(len(s1), len(s2))):
    if s1[i] != s2[i]:
        ans += 1
    else:
        continue

print(ans)
