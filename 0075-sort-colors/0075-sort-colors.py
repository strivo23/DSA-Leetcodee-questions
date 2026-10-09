class Solution(object):
    def sortColors(self, nums):
        count0 = count1 = count2 = 0
        for num in nums:
            if num == 0:
                count0 +=1
            if num == 1:
                count1 += 1
            if num == 2:
                count2 += 1
        i = 0
        for _ in range(count0):
            nums[i] = 0
            i += 1
        for _ in range(count1):
            nums[i] = 1
            i += 1
        for _ in range(count2):
            nums[i] = 2
            i += 1
        return nums