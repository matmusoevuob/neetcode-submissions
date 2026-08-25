class Solution:
    def isValid(self, s: str) -> bool:
        stc = []
        for i in s:
            if i in ")]}" and stc == []:
                return False
            elif i in "([{":
                stc.append(i)
                continue
            elif i == ")" and stc.pop() != "(":
                return False
            elif i == "]" and stc.pop() != "[":
                return False
            elif i == "}" and stc.pop() != "{":
                return False
        return stc == []
