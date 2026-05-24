class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = defaultdict(int)
        for i, num in enumerate(nums):
            if num in remaining.keys():
                other = remaining[num]
                return [other, i]
            remaining[(target - num)] = i
        
        return [] # should never occur