class Solution(object):
    def maxSubArray(self, nums):
        c_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            c_sum = max(nums[i], c_sum + nums[i])
            max_sum = max(c_sum, max_sum)
        return max_sum