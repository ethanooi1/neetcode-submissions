class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        res = []

        for point in points:
            dist = point[0]**2 + point[1]**2
            h.append([dist, point[0], point[1]])

        heapq.heapify(h)

        for i in range(k):
            res.append(heapq.heappop(h)[1:])

        return res
        