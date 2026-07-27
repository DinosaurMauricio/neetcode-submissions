class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checkEating(k):
            tot = 0 
            for pile in piles:
                tot += (pile+k-1)//k

                if tot > h:
                    return False
            return True 

        piles.sort()
        res = piles[-1]
        L, R = 1, piles[-1]
        while L <= R:
            #mid is our k
            mid = L + (R - L)//2

            is_valid = checkEating(mid)

            if is_valid:
                res = min(res, mid)
                R = mid - 1
                
            else:
                L = mid + 1

        return res