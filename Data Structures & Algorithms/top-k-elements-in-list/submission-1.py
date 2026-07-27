class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            mp[nums[i]] = mp.get(nums[i], 0) + 1
        res = sorted(mp, key=lambda x: mp[x])
        return res[-k:]