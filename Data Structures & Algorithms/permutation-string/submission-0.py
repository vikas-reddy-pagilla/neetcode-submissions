class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = Counter(s1)
        window_freq = Counter()
        p1 = 0
        p2 = len(s1) - 1
        window_freq = Counter(s2[p1:p2+1])
        while p2 < len(s2):
            if window_freq == freq_s1:
                return True
            else:
                p1 += 1
                p2 += 1
                window_freq = Counter(s2[p1:p2+1])
        return False
