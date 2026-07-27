import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        while len(stones) > 1:
            cand1 = stones[-1]
            cand2 = stones[-2]
            stones = stones[:-2]

            if cand1 < cand2:
                heapq.heappush(stones, cand2 - cand1)
            elif cand1 > cand2:
                heapq.heappush(stones, cand1 - cand2)

        if len(stones) == 0:
            return 0
        
        return stones[0]

        