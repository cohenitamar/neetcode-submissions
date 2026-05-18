class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        cSet = set()
        rLen = len(matrix)
        cLen = len(matrix[0])
        zeroFlag = False
        for r in range(rLen):
            for c in range(cLen):
                if matrix[r][c] == 0:
                    zeroFlag = True
                    cSet.add(c)
            if zeroFlag:
                matrix[r] = [0]*cLen        
            zeroFlag = False
        
        
        for r in range(rLen):
            for c in cSet:
                matrix[r][c] = 0
