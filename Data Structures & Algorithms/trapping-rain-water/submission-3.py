class Solution:
    def trap(self, height: List[int]) -> int:
        lPtr = 0
        rPtr = len(height) - 1
        leftMax = height[lPtr]
        rightMax = height[rPtr]
        res = 0
        
        while lPtr < rPtr:
            if leftMax < rightMax:
                lPtr += 1
                leftMax = max(leftMax, height[lPtr])
                res += leftMax - height[lPtr]
            else:
                rPtr -= 1
                rightMax = max(rightMax, height[rPtr])
                res += rightMax - height[rPtr]
        return res