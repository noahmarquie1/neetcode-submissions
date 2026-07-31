class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # handle trivial cases first
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 0 if nums[0] == target else -1

        split = int(len(nums) / 2)

        first_half_res = self.search(nums[:split], target)
        if first_half_res != -1:
            return first_half_res
        else:
            second_half_res = self.search(nums[split:], target)
            return -1 if second_half_res == -1 else split + second_half_res
        

        
        