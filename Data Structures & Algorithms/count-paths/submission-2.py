class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0] * n
        rows = m
        cols = n 

        for r in range(rows-1, -1, -1):
            curr = [0] * cols
            curr[-1] = 1
            for c in range(cols-2, -1, -1):
                curr[c] = prev[c] + curr[c+1]
            prev = curr
        return prev[0]

