class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        cache = dict()

        def dfs(i, j):
            if i == m-1 and j == n-1:
                return 1 
                 

            if i < m-1 and (i+1, j) not in cache:
                cache[(i+1, j)] = dfs(i+1, j)
            if j < n-1 and (i, j+1) not in cache:
                cache[(i, j+1)] = dfs(i, j+1)
            
            right = cache[(i+1, j)] if (i+1, j) in cache else 0 
            down = cache[(i, j+1)] if (i, j+1) in cache else 0 
            
            return right + down 


        return dfs(0, 0) 