class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nlist = [i for i in range(1, len(nums)+1) if i not in nums]

        return nlist


