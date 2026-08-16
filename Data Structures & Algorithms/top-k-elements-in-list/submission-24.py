class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        arr = [[] for _ in range(len(nums)+1)]
        res = []

        for val, freq in cnt.items():
            arr[freq].append(val)

        for i in range(len(arr)-1, -1, -1):
            for j in arr[i]:
                if len(res) == k:
                    return res
                res.append(j)
        
        return res
            
        