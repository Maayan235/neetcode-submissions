class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # use indees and the current array
        nums = [0 if x < 0 else x for x in nums]

        for val in nums:
            if 0 < abs(val) <= len(nums):
                if nums[abs(val) - 1] == 0:
                    nums[abs(val) - 1] = -1 * (len(nums)+1)
                else:
                    nums[abs(val)-1] = -1 * abs(nums[abs(val)-1])

        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1

        return len(nums) + 1