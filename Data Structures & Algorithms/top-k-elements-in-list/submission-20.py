class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = [[] for _ in range(len(nums) + 1)]
        ans = []
        for num, cnt in count.items():
            res[cnt].append(num)
        
        for i in range(len(nums), 0, -1):
            for val in res[i]:
                ans.append(val)
                if len(ans) == k:
                    return ans