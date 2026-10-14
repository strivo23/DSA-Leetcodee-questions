class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        mx_area = 0
        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            area = min_height * width
            mx_area = max(area, mx_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return mx_area        