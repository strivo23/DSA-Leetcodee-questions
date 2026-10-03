class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        total_sum = 0
        min_len = float('inf')
        for right in range(len(nums)):
            total_sum += nums[right]
            while total_sum >= target:
                min_len = min(min_len, right-left+1)
                total_sum -= nums[left]
                left += 1
        return min_len if min_len != float('inf') else 0
                