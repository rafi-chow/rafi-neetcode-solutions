class Solution:
#at all times, the already processed string holds string, and its length
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
#after i iterations, result should have only the content of the original string
        i = 0
        decoded = []
        while i < len(s):

            j = i
            #two pointer to get length
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            #get word
            word = s[j+1:j+1+length]
            #move i
            decoded.append(word)
            i = j + 1 + length
        return decoded