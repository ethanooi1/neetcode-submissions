class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
            res = []
            cor = []
            for i in range(len(grid)):
                for j in range(len(grid)):
                    res.append(grid[i][j])
            for x in range(len(grid)**2):
                cor.append(x+1)
            for y in range(len(res)):
                if cor[y] in res:
                    res.remove(cor[y])
                else:
                    res.append(cor[y])
            return res
                