class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 1 and len(nums) == 1:
            return nums

        result = []
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        count_array = [[] for _ in range(len(nums))]
        for key, value in freq.items():
            count_array[value-1].append(key)
        print(f"{freq} {count_array}")
        for i in range(len(nums) -1, -1, -1):
            for num in count_array[i]:
                result.append(num)
            if len(result) == k:
                return result