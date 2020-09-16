import sys

s = sys.stdin.readline().strip()

ans = 0

for i in range(len(s)):
    try:
        j = 1
        if s[i] == s[i + 1]:
            #print(1, s[i], s[i + 1], i)
            ans += 1
            while s[i + j + 1] == s[i - j]:
                if i - j < 0:
                    break
                #print(2, s[i + j + 1], s[i - j], i, j)
                ans += 1
                j += 1

        else:
            while s[i + j] == s[i - j]:
                if i - j < 0:
                    break
                #print(3, s[i + j], s[i - j], i, j)
                ans += 1
                j += 1
    except:
        continue

print(ans)
