class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen_chars = set()
        p2 = 0
        p1 = 0
        max_chars = 0
        while p2 < n:
            if s[p2] in seen_chars:
                seen_chars.remove(s[p1])
                p1 += 1
            else:
                seen_chars.add(s[p2])
                max_chars = max(max_chars, p2 - p1 + 1)
                p2 += 1
        return max_chars

