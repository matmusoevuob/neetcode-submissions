from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky = Counter(arr)
        ls = []
        for key, value in lucky.items():
            if key == value:
                ls.append(key)
        if ls:
            return max(ls)
        return -1

