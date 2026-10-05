class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(i):
            if i <= 2:
                return n

            dp = [1, 1]
            j = 2
            while j <= i:
                tmp = dp[1]
                dp[1] = dp[0]+dp[1]
                dp[0] = tmp
                j+=1

            return dp[1]

        return dp(n)

        

                







        