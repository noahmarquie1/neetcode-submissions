class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        for i, num in enumerate(nums):
            if target - num in seen.keys():
                compliment = seen[target - num]
                return [compliment, i]
            seen[num] = i
        
        return [] # should never occur