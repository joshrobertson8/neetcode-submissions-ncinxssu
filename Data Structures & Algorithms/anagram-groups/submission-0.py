class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}  # Use a regular dictionary
        for s in strs:
            sortedS = ''.join(sorted(s))  # Sort the string to use as the key
            if sortedS not in res:
                res[sortedS] = []
            res[sortedS].append(s)
               

        return list(res.values())
