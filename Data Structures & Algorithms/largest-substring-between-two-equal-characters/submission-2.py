class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        chToidx = defaultdict(int)
        res = 0

        for idx, ch in enumerate(s):
            
            if ch in chToidx:
                res = max(res, idx - chToidx[ch])
            else:
                chToidx[ch] = idx

        return res - 1
