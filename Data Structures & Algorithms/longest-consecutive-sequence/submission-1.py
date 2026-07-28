from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # to track sequences being made, we need to know the max of each seq
        # we can use hashing to easily search, but only one-way
        # To do O(n), we cannot sort the array, which would be O(nlogn)
        
        # store a map of (max, len)
        nums_set = set(nums)
        seq_starts = defaultdict(int)

        for num in nums:
            if num - 1 not in nums_set:
                seq_starts[num] = 0

        for start in seq_starts:
            curr = start
            while curr in nums_set:
                seq_starts[start] += 1
                curr += 1

        return 0 if len(seq_starts.keys()) == 0 else max(seq_starts.values())