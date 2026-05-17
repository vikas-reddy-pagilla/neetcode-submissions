class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        sotred_keys = sorted(freq.keys(), key = freq.get, reverse = True)
        for values in sotred_keys[:k]:
            result.append(values)
        return result