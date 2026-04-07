class Solution:
    def scoreOfString(self, s: str) -> int:
        
        cum = 0
        for ch in range(1, len(s)):
            cum += abs(ord(s[ch]) - ord(s[ch - 1]))
        return cum