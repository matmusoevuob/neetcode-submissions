class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nlist = []
        for i in range(1, n+1):
            if i not in nums:
                nlist.append(i)

        return nlist


