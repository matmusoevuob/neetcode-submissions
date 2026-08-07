class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fj = {}

        for i in nums:
            fj.setdefault(i, 0)
            fj[i] += 1

        st_fj = dict(sorted(fj.items(), key=lambda item: item[1], reverse=True))   

        kmost = list(st_fj.keys())[:k]

        return kmost