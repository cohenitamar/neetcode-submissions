class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            encodedStr += str(len(s)) + "#" + s
        return encodedStr


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            amountOfLetters = ""
            while s[i] != '#':
                amountOfLetters += s[i]
                i += 1
            i += 1    
            print(str(amountOfLetters))    
            #for j in range(i, i + int(amountOfLetters)):
            res.append(s[i:i + int(amountOfLetters)])
            i += int(amountOfLetters)

        return res    


        