class Solution:
    def isValid(self, s: str) -> bool:
        cMap = {"}":"{", ")":"(", "]":"["}
        stck = []
        for c in s:
            if c in "[({":
                stck.append(c)
            elif c in "])}":
                if len(stck) == 0:
                    return False
                sPop = stck.pop()
                if cMap[c] != sPop:
                    return False
        if len(stck) != 0:
            return False            
        return True        
                
        