
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        validWindow = Counter(s1)
        windowSize = len(s1)

        for l in range(len(s2)):

            window = s2[l : l + windowSize]

            if Counter(window) == validWindow:
                return True

        return False