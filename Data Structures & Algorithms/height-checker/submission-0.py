class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        n = 0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                n += 1
        return n