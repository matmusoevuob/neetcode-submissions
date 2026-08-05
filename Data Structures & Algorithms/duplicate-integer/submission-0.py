class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dn = set()
        for i in nums:
            if i in dn:
                return True
            dn.add(i)
        return False