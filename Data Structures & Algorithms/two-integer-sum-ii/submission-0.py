class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {} # dict of number: index (1 indexed)
        for i in range(len(numbers)):
            adjusted_i = i + 1
            diff = target - numbers[i]
            if diff in seen.keys():
                return [seen[diff], adjusted_i]
            
            seen[numbers[i]] = adjusted_i
        