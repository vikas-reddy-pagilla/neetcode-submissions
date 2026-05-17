class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = [1,2,3,4,5,5,6]
        result = []
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in count:
                if count[target - nums[i]] != i:
                    result.append(i)
                    result.append(count[target - nums[i]])
                    break

        return result
        
        