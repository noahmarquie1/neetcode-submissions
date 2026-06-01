class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets: List[List[int]] = [[num] for num in nums]
        subsets.append([])
        l = 2

        last_subsets: List[List[int]] = subsets
        while l <= len(nums):
            next_subsets: List[List[int]] = []
            for num in nums:
                for subset in last_subsets:
                    subset_cand = sorted(subset + [num])
                    if (not subset_cand in subsets) and (not num in subset):
                        next_subsets.append(subset_cand)
                        subsets.append(subset_cand)

            last_subsets = next_subsets
            l += 1

        return subsets



        