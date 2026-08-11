class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majdict = {}
        for i in nums:
            if i in majdict:
                majdict[i] += 1
            else:
                majdict[i] = 1

        for num, count in majdict.items():
            if count > len(nums) // 2:
                return num