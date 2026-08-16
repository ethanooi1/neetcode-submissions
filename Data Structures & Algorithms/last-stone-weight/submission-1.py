class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i] * -1
        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if x > y:
                heapq.heappush(stones, (y + x * -1))

        if len(stones) == 1:
            return stones[0] * -1
        else:
            return 0