class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        sdict = {}
        for ar in arr:
            sdict[ar] = sdict.setdefault(ar, 0) + 1
        slist = [key for key, val in sdict.items() if val == 1]

        if k <= len(slist):
            return slist[k-1]
        else:
            return ""