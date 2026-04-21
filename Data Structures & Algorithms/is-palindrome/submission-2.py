class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(c for c in s if c.isalnum()).lower()

        l, r = 0, len(cleaned) - 1

        while l < r:
            if cleaned[l] != cleaned[r]:
                return False
            
            r -= 1
            l += 1
        return True