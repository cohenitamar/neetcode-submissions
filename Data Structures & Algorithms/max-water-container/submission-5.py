class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lPtr = 0
        rPtr = len(heights) - 1
        maxAmount = 0
        while lPtr < rPtr:
            currentArea = min(heights[lPtr], heights[rPtr]) * (rPtr - lPtr)
            maxAmount = max(maxAmount, currentArea)
            if heights[lPtr] < heights[rPtr]:
                lPtr += 1
            elif  heights[lPtr] > heights[rPtr]:
                rPtr -= 1
            else:
                lPtr += 1
                rPtr -= 1
        return maxAmount        

  