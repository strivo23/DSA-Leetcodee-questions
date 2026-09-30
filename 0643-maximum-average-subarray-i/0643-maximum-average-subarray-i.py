class Solution(object):
    def findMaxAverage(self, nums, k):
        c_sum = sum(nums[:k])
        m_sum = c_sum
        for i in range(k, len(nums)):
            c_sum += nums[i] - nums[i-k]
            m_sum = max(m_sum, c_sum)

        return float(m_sum)/k