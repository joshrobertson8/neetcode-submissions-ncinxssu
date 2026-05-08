class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        writeIdx = 0

        numCopy = s[:]
        
        for i in range(len(s) - 1, -1, -1):

            s[i] = numCopy[writeIdx]
            writeIdx += 1
        
        return s
