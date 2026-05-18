class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rLen = len(matrix)
        cLen = len(matrix[0])
        
        firstRow = False
        firstCol = False
        
        # 1. Fast scan for the first row and first column boundaries
        for c in range(cLen):
            if matrix[0][c] == 0:
                firstRow = True
                break  # Exit early as soon as a zero is found
                
        for r in range(rLen):
            if matrix[r][0] == 0:
                firstCol = True
                break  # Exit early
        
        # 2. Record flags in the first row and column for the inner matrix
        for r in range(1, rLen):
            for c in range(1, cLen):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
                    
        # 3. Optimized Inner Update: Eliminates redundant writes and extra checks
        for r in range(1, rLen):
            if matrix[r][0] == 0:
                # If the row flag is set, blindly fill the row with zeros
                for c in range(1, cLen):
                    matrix[r][c] = 0
            else:
                # If row flag isn't set, only write zero if the column flag is set
                for c in range(1, cLen):
                    if matrix[0][c] == 0:
                        matrix[r][c] = 0
                        
        # 4. Final step: Clean up the boundaries
        if firstRow:
            for c in range(cLen):
                matrix[0][c] = 0
                
        if firstCol:
            for r in range(rLen):
                matrix[r][0] = 0