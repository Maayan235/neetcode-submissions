class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        masum = nums[0]
        currsum = 0

        for n in nums:
            if currsum < 0:
                currsum = 0

            currsum += n
            masum = max(masum, currsum)

        return masum 

        