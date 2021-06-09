class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        d = {}
        
        for i in s:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        
        odd = False
        count = 0
        
        for k,v in d.items():
            if v != 0 and v % 2 == 0:
                count += v
            elif  v != 0:
                if not odd:
                    count += v
                    odd = True
                else:
                    count += v -1
        
        return count