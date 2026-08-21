class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        slist = s.split()
        my_dict = {}
        reverse_dict = {}
        if len(slist) != len(pattern):
            return False
            
        for i in range(len(pattern)):
            character = pattern[i]
            word = slist[i]

            if character not in my_dict and word not in reverse_dict:
                my_dict[character] = word
                reverse_dict[word] = character
            elif my_dict.get(character) != word or reverse_dict.get(word) != character:
                return False

        return True