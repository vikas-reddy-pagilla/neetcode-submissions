class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        longest, current = 1, 1
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                continue
            if nums[i-1] == nums[i] -1:
                current += 1
            else:
                current = 1
            longest = max(current, longest)
        return longest
