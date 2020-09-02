def commonChars(self, chars):
    ans = ''

    for i in range(len(chars)):
        chars[i] = list(chars[i])

    for i in chars[0]:
        flag = 1
        for j in chars[1:]:
            if i not in j:
                flag = 0
            else:
                continue
        if flag:
            for j in range(len(chars[1:])):
                chars[j].remove(i)
            # print(i)
            ans = ans + i

    ans = list(ans)
    ans.sort()
    ans = ''.join(ans)
    return ans


print(commonChars('', ["abcc", "abcd", "abcr"]))
