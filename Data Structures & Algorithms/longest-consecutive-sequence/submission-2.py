class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        mCount = 0
        for i in range(len(nums)):
            if (nums[i] - 1) in s:
                continue
            lCount = 1
            currentNumber = nums[i] + 1
            while currentNumber in s:
                lCount += 1
                currentNumber += 1
            if mCount < lCount:
                mCount = lCount
            # another possibilty is to do mCount = max(mCount, lCount)    
        return mCount        