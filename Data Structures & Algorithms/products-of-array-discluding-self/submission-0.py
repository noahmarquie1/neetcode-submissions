class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # easier approach - get product of whole array, divide by current each step
        whole_product = 1
        # temp fix against zeros - zero count
        zero_count = 0 

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                whole_product *= num

        if zero_count == 0:
            return [int(whole_product / num) for num in nums]
        elif zero_count == 1:
            return [whole_product if num == 0 else 0 for num in nums]
        else:
            return [0 for _ in nums]
        