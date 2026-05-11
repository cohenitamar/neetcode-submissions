
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fMap = Counter(nums)
        iMap = defaultdict(list)
        res = []
        
        # Mapping frequency -> list of numbers
        for num, freq in fMap.items():
            iMap[freq].append(num)
        
        # Iterate backwards from max possible frequency (len(nums)) down to 1
        for i in range(len(nums), 0, -1):
            if i in iMap:
                for num in iMap[i]:
                    res.append(num)
                    # Stop as soon as we hit k elements
                    if len(res) == k:
                        return res

        return res