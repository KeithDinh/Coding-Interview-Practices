from collections import Counter 

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if len(A) < 2:
            return []
        
        d = dict(Counter(A[0]))
        
        for i in d.keys():
            for word in A[1:]:
                count = word.count(i)
                if count < d[i]:
                    d[i] = count
        
        result = []
        for i,j in d.items():
            if j > 0:
                result += [i] * j
        return result
            