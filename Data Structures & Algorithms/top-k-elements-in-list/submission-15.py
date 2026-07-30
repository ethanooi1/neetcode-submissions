class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = [[] for _ in range(len(nums) + 1)]
        res = []
        for num, freq in count.items():
            arr[freq].append(num)
        for i in range(len(nums), 0, -1):
            for val in arr[i]:
                res.append(val)
                if len(res) == k:
                    return res