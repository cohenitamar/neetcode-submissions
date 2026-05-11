class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # 1. Count the frequency of each number
        # fMap = {number: count}
        count = Counter(nums)
        
        # 2. Create buckets where index is the frequency
        # The max frequency can't exceed len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # 3. Iterate backwards from the highest frequency bucket
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res