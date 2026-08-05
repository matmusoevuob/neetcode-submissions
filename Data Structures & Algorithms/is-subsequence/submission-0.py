class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        is_sub = True
        s_index = 0
        t_index = 0
        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1
        
        if s_index != len(s):
            is_sub = False
            
        return is_sub