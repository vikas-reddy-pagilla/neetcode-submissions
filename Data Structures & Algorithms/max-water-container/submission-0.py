class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        p1 = 0
        p2 = n - 1
        max_water = 0
        while p1 < p2:
            width = p2 - p1
            current_height = min(heights[p2], heights[p1])
            current_area = width * current_height
            max_water = max(max_water, current_area)

            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        return max_water

