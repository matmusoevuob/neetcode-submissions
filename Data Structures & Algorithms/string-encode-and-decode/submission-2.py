class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""

        for word in strs:
            enc = enc + "#" + str(len(word)) + "#" + word

        return enc
    
    def decode(self, s: str) -> List[str]:
        dec = []
        i = 0
        while i < len(s):
            if s[i] == "#":
                i += 1
                j = i
                while s[j] != "#":
                    j += 1
                length = int(s[i:j])
                dec.append(s[j + 1:j + 1 + length])
                i = j + 1 + length
            else:
                i += 1
        
        return dec