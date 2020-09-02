import sys

s = sys.stdin.readline().strip()
s = list(s)

good = ['G', 'o', 'o', 'd']
k = 0

ans = 0

for i in range(len(s)):
    if s[i] == good[k]:
        for j in range(i, len(s)):
            if s[j] == good[k]:
                print(s[j], good[k])
                s[j] = '.'
                k += 1
                if k == 4:
                    ans += 1
                    k = 0
                    break

print(ans)
