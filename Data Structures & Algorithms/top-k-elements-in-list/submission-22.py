class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        ls = [[] for _ in range (len(nums) + 1)]
        res = []

        for i, n in cnt.items():
            ls[n].append(i)

        for i in range(len(nums), 0, -1):
            for val in ls[i]:
                res.append(val)
                if len(res) == k:
                    return res