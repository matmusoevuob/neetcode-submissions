class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fj = {}
        for i in nums:
            fj.setdefault(i, 0)
            fj[i] += 1
        sorted_fj_desc = dict(sorted(fj.items(), key=lambda item: item[1], reverse=True))   
        
        kmost = list(sorted_fj_desc.keys())[:k]

        return kmost