class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        mp = defaultdict(list)
        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            mp[dist].append(point)

        h = list(mp.keys())
        heapq.heapify(h)
        print(mp)
        
        while len(res) < k:
            for n in mp[h[0]]:
                res.append(n)
            heapq.heappop(h)
        
        return res

        
                
        
        

        