class Solution:
    def GetMaxStaffs(self, pos):
        pos = pos[2:-2].split('],[')
        for i in range(len(pos)):
            pos[i] = pos[i].split(',')
        h, w = len(pos), len(pos[0])
        ans = 0
        for i in range(h):
            for j in range(w):
                # print(i, j)
                if pos[i][j] == '*':
                    continue
                if pos[i][j] == '.':
                    ans += 1
                    pos[i][j] = '*'
                    pos[max(0, i - 1)][j] = '*'
                    pos[min(i + 2, h) - 1][j] = '*'
                    pos[i][max(0, j - 1)] = '*'
                    pos[i][min(j + 2, w) - 1] = '*'
                    continue
        return ans


s = Solution()
print(s.GetMaxStaffs('[[.,.,.,.,.],[.,.,.,.,.],[.,.,.,.,.]]'))
