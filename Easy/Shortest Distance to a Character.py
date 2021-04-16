class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        result = [0] * n
        
        # set lastOccur to n so the first pass creates out-index values to the position that are not valid
        lastOccur = n      
        for i in range(n):
            if s[i] == c:
                lastOccur = i
            result[i] = abs(i - lastOccur)
        
        # set lastOccur to n so the first pass creates out-index values to the position that are not valid
        lastOccur = -1
        for i in range(n-1,-1,-1):
            if s[i] == c:
                lastOccur = i
            result[i] = min(result[i],abs(i - lastOccur))
        
        return result