from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        seq_starts = defaultdict(int)

        for num in nums:
            if num - 1 not in nums_set:
                seq_starts[num] = 0

        max_seq = 0
        for start in seq_starts:
            curr = start
            while curr in nums_set:
                seq_starts[start] += 1
                curr += 1

            max_seq = max(max_seq, seq_starts[start])

        return max_seq