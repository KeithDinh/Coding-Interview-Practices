class Solution:
    def frequencySort(self, s: str) -> str:
    
        d = {}
        for i in s:
            d[i] = d[i]+1 if i in d.keys() else 1
        
        
        st = ''
        for k in sorted(d, key=d.__getitem__, reverse=True):
            for i in range(d[k]):
                st += k
                
        return st