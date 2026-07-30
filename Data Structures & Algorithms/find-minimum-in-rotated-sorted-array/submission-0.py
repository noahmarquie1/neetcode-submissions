class Solution:
    def findMin(self, nums: List[int]) -> int:
        # do recursion, cutting the list by half each time
        # cases are:
        #  1. end of list greater than start of list: return start of list
        #  2. end of list less than start of list: return min of recursion 
        #     for first and second halves
        if nums[-1] >= nums[0]: # covers case (1), and len(nums) == 1 situation
            return nums[0]
        
        split = int(len(nums) / 2)
        return min(self.findMin(nums[:split]), self.findMin(nums[split:]))
        