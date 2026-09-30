class Solution(object):
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        while left  < right:
            mid = (left+right)//2
            total_hours = 0
            for p in piles:
                total_hours += math.ceil(p/float(mid))
            if total_hours <= h:
                right = mid
            else:
                left = mid+1
        return left