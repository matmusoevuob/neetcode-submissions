class Solution:
    def maxDifference(self, s: str) -> int:
        max_odd = 0
        min_even = 101
        freq = {}

        for _ in s:
            freq[_] = freq.setdefault(_, 0) + 1

        for i in list(freq.values()):
            if i % 2 == 0:
                min_even = min(min_even, i)
            else:
                max_odd = max(max_odd, i)

        return max_odd - min_even
        