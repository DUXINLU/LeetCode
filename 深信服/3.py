def min_send(self, nums, m):
    n = len(nums)
    res = []

    def dfs(i, s, k, max_):
        if s > max_:
            max_ = s
        if i == n:
            if k == m - 1:
                res.append(max_)
        else:
            dfs(i + 1, nums[i], k + 1)
            dfs(i + 1, s + nums[i], k)

    dfs(1, nums[0], 0)
    return min(res)

min_send('',[4,3,5,10,12],2)