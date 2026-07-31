class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # handle trivial cases first
        if len(nums) == 1:
            return (nums[0] == target) - 1 # Easy way to say 0: true, -1: false

        split = int(len(nums) / 2)

        if nums[0] <= target < nums[split]:
            return self.search(nums[:split], target)
        elif nums[split] <= target <= nums[-1]:
            second_half_res = self.search(nums[split:], target)
            return -1 if second_half_res == -1 else split + second_half_res

        first_half_res = self.search(nums[:split], target)
        if first_half_res != -1:
            return first_half_res
        else:
            second_half_res = self.search(nums[split:], target)
            return -1 if second_half_res == -1 else split + second_half_res
        

        
        