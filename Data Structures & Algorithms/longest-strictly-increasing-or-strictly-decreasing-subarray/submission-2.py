class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_sub = 1
        max_inc = 1
        max_dec = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                max_sub = max(max_sub, max_dec, max_inc)
                max_dec = 1
                max_inc = 1
            elif nums[i] > nums[i-1]:
                max_inc += 1
                max_sub = max(max_sub, max_dec, max_inc)
                max_dec = 1
            else:
                max_dec += 1
                max_sub = max(max_sub, max_dec, max_inc)
                max_inc = 1
             


        return max_sub