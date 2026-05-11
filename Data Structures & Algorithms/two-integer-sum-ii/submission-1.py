class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lPtr = 0
        rPtr = len(numbers) - 1
        while lPtr < rPtr:
            sumOfPtr = numbers[lPtr] + numbers[rPtr]
            if sumOfPtr > target:
                rPtr -= 1
            elif sumOfPtr < target:
                lPtr += 1
            else:
                return [lPtr + 1, rPtr + 1]    
        return False
        