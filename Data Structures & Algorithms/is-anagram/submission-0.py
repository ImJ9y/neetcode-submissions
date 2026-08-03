class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        

        word_bank1 = [0] * 26
        for i in range(len(s)):
            word_bank1[ord(s[i]) - ord('a')] += 1

        word_bank2 = [0] * 26
        for i in range(len(t)):
            word_bank2[ord(t[i]) - ord('a')] += 1

        return tuple(word_bank1) == tuple(word_bank2)