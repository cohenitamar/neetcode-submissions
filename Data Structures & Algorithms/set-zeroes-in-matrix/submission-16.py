class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rLen = len(matrix)
        cLen = len(matrix[0])
        zeroFlag = False
        firstRow = False
        for c in range(cLen):
            if matrix[0][c] == 0:
                firstRow = True
                break

        for r in range(1, rLen):
            for c in range(0, cLen):
                if matrix[r][c] == 0:
                    zeroFlag = True
                    matrix[0][c] = 0
            if zeroFlag:
                #matrix[r] = [0]*cLen 
                for c in range(cLen):
                    matrix[r][c] = 0       
            zeroFlag = False
        
        for c in range(cLen):
            if matrix[0][c] == 0:
                for r in range(rLen):
                    matrix[r][c] = 0

        if firstRow:
            #matrix[0] = [0]*cLen
            for c in range(cLen):
                matrix[0][c] = 0            