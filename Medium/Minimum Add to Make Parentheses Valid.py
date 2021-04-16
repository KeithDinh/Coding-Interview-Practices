class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        validCount = 0
        missCount = 0
        for i in S:
            if i == '(':
                validCount += 1
            elif validCount > 0:
                validCount -= 1
            else:
                missCount += 1
            
        return validCount + missCount