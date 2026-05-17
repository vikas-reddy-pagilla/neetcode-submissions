class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = [1,2,3,4,5(4),5(5)]
        result = []
        count = {}
        for i in range(len(nums)):
            if target - nums[i] in count:
                result.append(count[target - nums[i]])
                result.append(i)
                break
            count[nums[i]] = i
        return result
        
        