class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        left = 0
        freq_t, window = Counter(t), {}
        have = 0
        need = len(freq_t)
        res, res_len = [-1, -1], float("infinity")
        for right in range(len(s)):
            ch = s[right]
            window[ch] = 1 + window.get(ch, 0)

            if ch in freq_t and window[ch] == freq_t[ch]:
                have += 1
            
            while have == need:
                if (right - left + 1 ) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                window[s[left]] -= 1
                if s[left] in freq_t and window[s[left]] < freq_t[s[left]]:
                    have -= 1
                left += 1
        left, right = res
        return s[left:right+1] if res_len != float("infinity") else ""

            


        