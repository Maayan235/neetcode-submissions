class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        prev = [0]*cols
        prev[-1] = 1 if obstacleGrid[-1][-1] == 0 else 0 

        for r in range(rows-1, -1, -1):
            curr = [0]*cols
            for c in range(cols-1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    curr[c] = 0 
                elif c == cols -1:
                    curr[c] = prev[c]
                else:
                    curr[c] = prev[c] + curr[c+1]
            prev = curr
        return prev[0]









        