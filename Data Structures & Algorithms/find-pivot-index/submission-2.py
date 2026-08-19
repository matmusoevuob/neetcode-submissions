class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sr = sum(nums)
        sl = 0
        for i in range(len(nums)):
            if i != 0:
                sl += nums[i-1]
            sr -= nums[i]
            if sl == sr :
                return i
            
        return -1