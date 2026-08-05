class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        cs = {}
        ct = {}

        for ch in s:
            cs[ch] = cs.get( ch , 0 ) + 1

        for ch in t:
            ct[ch] = ct.get( ch , 0 ) + 1     
        
        return cs == ct