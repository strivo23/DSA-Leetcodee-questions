class Solution(object):
    def majorityElement(self, nums):
        hashmap = {}
        majority_count = len(nums)//2
        for num in nums:
            hashmap[num] = hashmap.get(num, 0)+1
            if hashmap[num] > majority_count:
                return num