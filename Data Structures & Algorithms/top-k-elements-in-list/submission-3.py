class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntMap = {}
        res = []
        for i in nums:
            cntMap[i] = cntMap.get(i, 0) + 1
        for _ in range(k):
            res.append(max(cntMap, key=cntMap.get))
            cntMap.pop(max(cntMap, key=cntMap.get))
        return res