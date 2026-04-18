from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        
        res = ""
        
        for s in strs:
            res += "~" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        curr = ""

        if not s:
            return []

        for i in range(1, len(s)):

            if s[i] == "~":
                res.append(curr)
                curr = ""
            else:
                curr += s[i]
        res.append(curr)
        
        return res