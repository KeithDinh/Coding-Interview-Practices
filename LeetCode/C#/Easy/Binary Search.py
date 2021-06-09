class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        return self.bsearch(nums, 0, len(nums)-1,target)
            
        
        
    def bsearch(self, nums, l, r, target):
        if r >= l:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                return self.bsearch(nums, mid+1, r, target)
            else:
                return self.bsearch(nums, l, mid-1, target)
        else:
            return -1