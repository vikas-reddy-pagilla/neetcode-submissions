class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        p1 = 0
        p2 = n-1
        left_max , right_max = height[0], height[n-1]
        total = 0
        while p1 < p2:
            if height[p1] <= height[p2]:
                p1 += 1
                left_max = max(left_max, height[p1])
                total += left_max - height[p1]
            else:
                p2 -= 1
                right_max = max(right_max, height[p2])
                total += right_max - height[p2]
        return total
        