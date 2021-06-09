class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        
        return [i for i in d.keys() if d[i] == 1]