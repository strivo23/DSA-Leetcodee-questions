class Solution(object):
    def majorityElement(self, nums):
        majority_count = len(nums)//3
        hashmap = {}
        arr = []
        for num in nums:
            hashmap[num] = hashmap.get(num, 0)+1
            if hashmap[num] > majority_count and num not in arr:
                arr.append(num)
        return arr
        