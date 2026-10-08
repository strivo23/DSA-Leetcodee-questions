class Solution(object):
    def maxSubArray(self, nums):
        curr_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(curr_sum, max_sum)
        return max_sum