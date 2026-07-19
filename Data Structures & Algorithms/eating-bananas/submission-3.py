from math import ceil

class Solution:
    def hoursToEat(self, piles: List[int], k: int):
        piles = piles.copy()
        hours = 0
        while len(piles) > 0:
            hours += ceil(piles[0] / k)
            piles.pop(0)

        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # eating speed is a "monotonic search" problem, suggesting binary search
        # we have a floor and ceiling and increment them until 
        #  - floor > h 
        #  - ceil < h  
        #  - ceil = floor + 1
        #
        # if eating speed k has minEatingSpeed(k) < h, then every k above also satisfies property

        ceil = max(piles)
        floor = 1

        while ceil > floor + 1:
            # check middle value
            #  - if its under h, match ceil = middle
            #  - if its over h, match floor = middle
            mid = floor + int((ceil - floor) / 2)
            if self.hoursToEat(piles, mid) <= h:
                ceil = mid
            else:
                floor = mid

        if self.hoursToEat(piles, floor) <= h:
            return floor
        else:
            return ceil

            






        