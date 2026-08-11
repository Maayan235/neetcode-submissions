class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 3 pointers, left right and i 
        # swapping in place 
        # 2 0 1 
        # l = 2 i = 2 r = 1 
        # 1 0 2
        # l = 1 i = 1 r = 0
        # 1 0 2
        # l = 1 i = 0 r = 0


        l = 0 
        r = len(nums) - 1
        i = 0

        while i <= r:
            # swap 0
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                i += 1
                l += 1
            # swap 2
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else: 
                i += 1 
        
        


        