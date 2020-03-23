class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        ans = [1 for i in range(n)]
        ans[0:2] = [0, 0]
        for i in range(2, int(n ** 0.5) + 1):
            if ans[i] == 1:
                ans[i * i::i] = [0] * len(ans[i * i::i])
        print(ans)
        return sum(ans)


s = Solution()
s.countPrimes(12)
