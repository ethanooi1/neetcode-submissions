class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
        cnt = Counter(nums)
        arr = [[] for _ in range (len(nums) + 1)]
        res = []

        for key, v in cnt.items():
            arr[v].append(key)
        
        for i in range(len(arr)-1, -1, -1):
            for val in arr[i]:
                res.append(val)
                if len(res) == k:
                    return res



