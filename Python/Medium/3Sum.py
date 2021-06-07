class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        
        result = list()
        for k in range(len(nums)-2):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i = k + 1
            j = len(nums)-1
            remain = 0 - nums[k]
            while (i < j):
                if nums[i] + nums[j] == remain:
                    result.append([nums[k], nums[i],nums[j]])
                    while i < j and nums[i] == nums[i+1]:
                        i += 1
                    while i < j and nums[j] == nums[j-1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] < remain:
                    i += 1
                else:
                    j -= 1
            
        return result