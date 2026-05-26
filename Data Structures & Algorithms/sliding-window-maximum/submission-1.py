class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for right in range(k-1, len(nums)):
            left = right - k + 1
            res.append(max(nums[left:right+1]) )
        return res

