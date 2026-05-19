class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(1, len(nums)):
            p1 = i
            p2 = len(nums) -1
            target = - nums[i-1]
            if i > 1 and nums[i-1] == nums[i-2]:
                continue
            while p1 < p2:
                current_sum = nums[p1] + nums[p2]
                if current_sum == target:
                    result.append([nums[i-1], nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1
                    while p1 < p2 and nums[p1-1] == nums[p1] :
                        p1 += 1
                    while p1 < p2 and nums[p2+1] == nums[p2] :
                        p2 -= 1
                elif current_sum < target:
                    p1 += 1
                else:
                    p2 -= 1
                # p1 = 1
                # p2 = len(nums) -1
        return result
                