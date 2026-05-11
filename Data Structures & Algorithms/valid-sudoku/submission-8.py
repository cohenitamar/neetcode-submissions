class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squareSize = int(len(board)**0.5)
        for i in range(len(board)):
            hSet = Counter(board[i])
            for j in range(1, len(board[i]) + 1):
                if str(j) in hSet:
                    if hSet[str(j)] != 1:
                        return False
                
        for i in range(len(board)):
            hSet = defaultdict(int)
            for j in range(len(board[i])):
                if board[j][i] == '.':
                    continue
                hSet[board[j][i]] = hSet[board[j][i]] + 1
                if hSet[board[j][i]] > 1:
                    return False


        for i in range(0, len(board), squareSize):
            for j in range(0, len(board), squareSize):
                squareSet = defaultdict(int)
                for r in range(i, i + squareSize):
                    for c in range(j, j + squareSize):
                        if board[r][c] == '.':
                            continue
                        squareSet[board[r][c]] += 1
                        if squareSet[board[r][c]] > 1:
                            return False            
        
        return True