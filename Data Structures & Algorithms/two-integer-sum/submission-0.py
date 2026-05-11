class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        count = 0
        for x in nums:
            diff = target - x
            if diff in map:
                return [map[diff], count]
            map[x] = count       
            count += 1