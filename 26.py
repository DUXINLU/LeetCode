class Solution:
    def removeDuplicates(self, nums):
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                for j in range(i + 1, len(nums)):
                    if nums[j] == nums[i]:
                        nums[j] = -9999
                        print(nums)
                    else:
                        print(nums)
                        break

        count = nums.count(-9999)
        print(count)
        for i in range(count):
            nums.remove(-9999)
            print(nums)
        return count


s = Solution()
s.removeDuplicates([1, 1, 2, 3, 4, 5])
