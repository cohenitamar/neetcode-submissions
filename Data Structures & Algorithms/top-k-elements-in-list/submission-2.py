class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = Counter(nums).most_common(k)
        l = []
        for r in res:
            l.append(r[0])
        return l     