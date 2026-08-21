class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        slist = s.split()
        my_dict = {}
        reverse_dict = {}
        if len(slist) != len(pattern):
            return False
            
        for i in range(len(pattern)):
            ch = pattern[i]
            word = slist[i]

            if ch not in my_dict and word not in reverse_dict:
                my_dict[ch] = word
                reverse_dict[word] = ch
            elif my_dict.get(ch) != word or reverse_dict.get(word) != ch:
                return False

        return True