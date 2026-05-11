class Solution:
    def twoSum(self, start: int, numbers: List[int], target: int) -> List[List[int]]:
        pairs = []
        lPtr = start
        rPtr = len(numbers) - 1
        while lPtr < rPtr:
            sumOfPtr = numbers[lPtr] + numbers[rPtr]
            if sumOfPtr > target:
                rPtr -= 1
            elif sumOfPtr < target:
                lPtr += 1
            else:
                pairs.append([lPtr, rPtr]) 
                lPtr += 1
                rPtr -= 1
                while lPtr < rPtr and numbers[lPtr] == numbers[lPtr - 1]:
                    lPtr += 1
        return pairs
            
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            r = self.twoSum(i + 1, nums, -1*nums[i])
            if len(r) == 0:
                continue
            for j in range(len(r)):
                if i == r[j][0] or i == r[j][1]:
                    continue
                r[j][0] = nums[r[j][0]]    
                r[j][1] = nums[r[j][1]]    
                r[j].append(nums[i])
                res.append(r[j])
        return res        
        
    