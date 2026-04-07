class Solution:
    def isPalindrome(self, s: str) -> bool:
        parced_s = [char.lower() for char in s if char.isalnum()]
        l = 0 
        r = len(parced_s) - 1 

        while l < r: 

            if parced_s[l] == parced_s[r]:
                l += 1
                r -= 1
            else:
                return False

        return True