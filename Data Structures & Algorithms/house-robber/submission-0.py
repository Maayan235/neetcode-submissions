class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        cache = {}

        def dp(i):
            if i >= n:
                return 0
            if i in cache:
                return cache[i]

            cache[i] = max(nums[i]+dp(i+2), dp(i+1))
            return cache[i]

        return dp(0)

        

                



        