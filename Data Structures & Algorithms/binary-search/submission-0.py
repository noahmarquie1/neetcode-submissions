class Solution:
    def split(self, nums):
        split_idx = int(len(nums) / 2)
        return nums[:split_idx], nums[split_idx:], split_idx


    def search(self, nums: List[int], target: int) -> int:
        if ((len(nums) == 0) 
            or (len(nums) == 1 and nums[0] != target) 
            or (nums[0] > target)):
            return -1
        elif nums[0] == target:
            return 0
        else:
            l, r, split_idx = self.split(nums)
            r_search = self.search(r, target)
            if r_search != -1:
                return split_idx + r_search
            return self.search(l, target)

        