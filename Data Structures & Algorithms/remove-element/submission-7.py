class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)

        for i in range(k):
            if val not in nums:
                return k
            else:
                nums.remove(val)
                k -= 1
        return k