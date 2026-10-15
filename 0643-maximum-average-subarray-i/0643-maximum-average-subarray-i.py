class Solution(object):
    def findMaxAverage(self, nums, k):
        csum = sum(nums[:k])
        max_sum = csum
        n = len(nums)
        for i in range(k, n):
            csum += nums[i]-nums[i-k]
            max_sum = max(csum, max_sum)
        return max_sum / float(k)
