class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = set()
        repeated = 0

        for row in grid:
            for v in row:
                if v in seen:
                    repeated = v
                else:
                    seen.add(v)
        
        missing = 0
        for v in range(1, len(grid)**2+1):
            if v not in seen:
                missing = v
                break
        
        return [repeated, missing]