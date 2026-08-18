class Solution:
    def maxDifference(self, s: str) -> int:
        odd = 0
        even = 101
        freq = {}

        for _ in s:
            freq[_] = freq.get(_, 0) + 1

        for i in list(freq.values()):
            if i % 2 == 0:
                even = min(even, i)
            else:
                odd = max(odd, i)

        return odd - even
        