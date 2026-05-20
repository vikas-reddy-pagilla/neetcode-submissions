class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        p1 = 0
        p2 = 0 
        n = len(s)
        max_len = 0
        chars_count = {}
        while p2 < n:
            if s[p2] in chars_count:
                chars_count[s[p2]] += 1
            else:
                chars_count[s[p2]] = 1
            
            max_freq = max(chars_count.values())

            window_size = p2 - p1 + 1

            if window_size - max_freq > k:
                chars_count[s[p1]] -= 1
                p1 += 1
            max_len = max(max_len, p2 - p1 + 1)
            p2 += 1
        return max_len            
