class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        set_c = set()
        max_length = 0
        for R in range(len(s)):
            while L < len(s) and s[R] in set_c:
                set_c.remove(s[L])
                L += 1


            set_c.add(s[R])
            max_length = max(max_length, len(set_c))
        
        return max_length