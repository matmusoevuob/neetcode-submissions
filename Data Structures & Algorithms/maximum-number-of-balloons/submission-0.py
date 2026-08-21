class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        my_dict = {
            "b" : 0,
            "a" : 0,
            "l" : 0,
            "o" : 0,
            "n" : 0
        }
        for i in text:
            if i in my_dict.keys():
                my_dict[i] += 1
        
        my_dict["l"] //= 2

        my_dict["o"] //= 2

        return min(my_dict.values())
