import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # go through the list, have a min heap of the k largest elements,
        #   pop every time the list goes higher than k
        #   return heap minimum in the end
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
            
        return heapq.heappop(heap)

        