class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nlist = []
        for i in range(1, len(nums)+1):
            if i not in nums:
                nlist.append(i)

        return nlist


