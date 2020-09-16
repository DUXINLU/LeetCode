class Solution:
    def RotateMatrix(self, matrix):
        length, width = len(matrix), len(matrix[0])

        ans = []

        for i in range(width):
            _ = []
            for j in range(length):
                _.append(matrix[j][i])
            ans.append(_)
        ans.reverse()
        print(ans)
        return ans


s = Solution()
s.RotateMatrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
