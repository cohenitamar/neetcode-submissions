class Solution:
    def isPalindrome(self, s: str) -> bool:
        lPtr = 0
        rPtr = len(s) - 1
        while lPtr < rPtr:
            while not s[lPtr].isalnum() and lPtr < rPtr:
                lPtr += 1
            while not s[rPtr].isalnum() and lPtr < rPtr:
                rPtr -= 1    
            if s[lPtr].lower() != s[rPtr].lower():
                return False
            lPtr += 1
            rPtr -= 1
        return True            