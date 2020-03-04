class Solution:
    def printVertically(self, s: str) -> List[str]:
        ans = []
        s = s.split(" ")
        max_ = -1
        for i in s:
            if len(i) > max_:
                max_ = len(i)
        for i in range(len(s)):
            s[i] = s[i] + (max_ - len(s[i])) * ' '
        _ = ''
        for i in range(max_):
            for j in range(len(s)):
                _ += s[j][i]
            ans.append(_)
            _ = ''
        for i in range(len(ans)):
            ans[i] = ans[i].rstrip()

        return ans
