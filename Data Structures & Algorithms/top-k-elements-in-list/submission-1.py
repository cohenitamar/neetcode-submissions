class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Get the k most frequent, then extract just the number (x[0])
        return [x[0] for x in Counter(nums).most_common(k)]