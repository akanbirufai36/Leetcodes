class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return (seen[complement], i)
            seen[num] = i
        return None  # no valid pair found


nums = [2, 7, 11, 15]
target = 9

sum = Solution()
print(sum.twoSum(nums, target))
