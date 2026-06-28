from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        sol = []
        for i in range(len(nums)):
            # Perform two sum on the remaining list, totalling n^2 time complexity
            target_2sum = -nums[i]
            seen = {}
            for j in range(i+1,len(nums)):
                diff = target_2sum - nums[j]
                if diff in seen.keys():
                    cand = [nums[i], diff, nums[j]]
                    if not cand in sol:
                        sol.append(cand)
                
                seen[nums[j]] = j

        return sol



        