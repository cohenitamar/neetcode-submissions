class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        mul = 1
        res.append(1)
        for i in range(1, len(nums)):
            res.append(nums[i - 1] * mul)
            mul = res[i]
        print(res)
        mul = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * mul
            mul = mul * nums[i] 
  
        return res