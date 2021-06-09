class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if(length < 2):
            return nums
        
        pivot = nums.pop()
        low = []
        high = []
        for i in nums:
            if i < pivot:
                low.append(i)
            else:
                high.append(i)
        
        return self.sortArray(low) + [pivot] + self.sortArray(high)