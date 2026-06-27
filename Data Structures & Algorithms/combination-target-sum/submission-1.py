class Solution:
    def __init__(self):
        self.sols = []


    def dfs_search(self, state, nums, target):
        if len(nums) == 0:
            return

        first = nums[0]
        
        # return if target is attained
        if sum(state) == target and state not in self.sols:
            self.sols.append(state)
            return
        elif sum(state) > target:
            return


        # branch 1 - include first - keep front
        self.dfs_search(state + [first], nums, target)

        # branch 2 - include first, pop list
        self.dfs_search(state + [first], nums[1:], target)

        # branch 3 - do not include first - pop list
        self.dfs_search(state, nums[1:], target)


    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.dfs_search(state=[], nums=nums, target=target)
        return self.sols

        