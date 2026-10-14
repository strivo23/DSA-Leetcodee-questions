class Solution(object):
    def twoSum(self, nums, target):
        left = 0
        right = len(nums)-1
        while left < right:
            summ = nums[left] + nums[right]
            if summ == target:
                return [left+1, right+1]
            elif summ < target:
                left +=1
            else:
                right -= 1
        
