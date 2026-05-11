
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = len(board)
        base = int(N**0.5) # עבור לוח 9 זה יהיה 3
        
        # אנחנו יוצרים רשימות של קבוצות (Sets)
        # כל אינדקס ברשימה מייצג שורה/עמודה/ריבוע ספציפי
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        squares = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                
                # תאים ריקים לא מעניינים אותנו
                if val == ".":
                    continue
                
                # חישוב אינדקס הריבוע:
                # הנוסחה מחלקת את הלוח לבלוקים של base x base
                s_idx = (r // base) * base + (c // base)
                
                # הבדיקה הקריטית: האם הערך כבר קיים באחד המבנים?
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in squares[s_idx]):
                    return False
                
                # אם לא קיים, נוסיף אותו לכולם ונמשיך
                rows[r].add(val)
                cols[c].add(val)
                squares[s_idx].add(val)
                
        return True