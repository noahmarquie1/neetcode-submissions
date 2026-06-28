class Solution:
    def area(self, l, r, heights):
        return (r-l) * min(heights[l], heights[r])


    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        best_area = self.area(l, r, heights)

        # check additional configurations
        while l < r:
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            best_area = max(best_area, self.area(l, r, heights))

        return best_area

        