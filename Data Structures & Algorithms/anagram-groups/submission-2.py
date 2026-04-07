class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        """
        [1, 0, 0 , 0..... 0]
        [0, 0, 0]

        {[sig]: ['hat']}
        
        """

        for word in strs:
            signiture = [0] * 26

            for char in word:
                signiture[ord(char) - ord('a')] += 1

            res[tuple(signiture)].append(word)
        return list(res.values())
        
