class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        iso_bool = True
        iso_dict = {}
        for i in range(len(s)):
            if s[i] in iso_dict:
                if iso_dict[s[i]] != t[i]:
                    iso_bool = False
                    break
            else:
                if t[i] in iso_dict.values():
                    iso_bool = False
                    break
                else:
                    iso_dict[s[i]] = t[i]


        return iso_bool