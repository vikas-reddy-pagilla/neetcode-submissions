class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stack_index, stack_temp = stack.pop()
                result[stack_index] = index - stack_index
            stack.append([index, temp])
        return result
