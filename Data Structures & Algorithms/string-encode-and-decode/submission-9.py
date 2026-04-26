class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        
        for word in strs:
            res += "~" + word
        
        return res

    def decode(self, s: str) -> List[str]:
        
        res = []

        curWord = ""

        if not s:
            return [] 
        
        for i in range(1, len(s)):
            if s[i] != "~":
                curWord += s[i]
            else:
                res.append(curWord)
                curWord = ""

        res.append(curWord)
        return res