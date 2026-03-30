class Solution:

    def encode(self, strs: List[str]) -> str:
        #5#Hello,5#WORLD
        encoded_string = ""
        for s in strs:
            encoded_string += str((len(s))) + "#" + s
            #  5#hello5#world
        return encoded_string
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])


            strs.append(s[j + 1 : j+1+length])
            i = j + 1 + length

        return strs