class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        while len(nums) > 0:
            if nums[0] in seen:
                return True
            seen.add(nums[0])
            nums.pop(0)

        return False
        