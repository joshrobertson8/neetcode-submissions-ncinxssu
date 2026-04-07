class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = [char.lower() for char in s if char.isalnum()]

        l, r = 0, len(cleaned) - 1

        for i in range(len(cleaned)): 

            if cleaned[l] == cleaned[r]: 
                l += 1
                r -= 1

            else:
                return False

        return True