class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp = sorted(heights)
        n = 0
        for i in range(len(heights)):
            if exp[i] != heights[i]:
                n += 1
        return n