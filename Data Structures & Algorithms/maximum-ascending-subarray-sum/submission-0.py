class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        max_inc = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                max_sum = max(max_sum, max_inc)
                max_inc = nums[i]
            elif nums[i] > nums[i-1]:
                max_inc += nums[i]
                max_sum = max(max_sum, max_inc)
            else:
                max_sum = max(max_sum, max_inc)
                max_inc = nums[i]
             
        return max_sum