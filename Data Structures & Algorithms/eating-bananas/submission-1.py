class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def fits(k):
            total_hours = 0
            for pile in piles:
                hours = (pile + k - 1) // k
                total_hours += hours
            if total_hours <= h:
                return True
            else:
                return False

        l = 1
        r = max(piles)

        while l < r:
            mid = (r + l) // 2
            if fits(mid):
                r = mid
            else:
                l = mid + 1
        return l
        


            
