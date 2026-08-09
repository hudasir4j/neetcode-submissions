class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #one approach: store non0 in an array, then add 0s to end
        #other approach: compare left to right. if left = 0 and right 

        l, r = 0, 1

        while(r < len(nums)):
            if (nums[l] == 0 and nums[r] != 0):
                nums[l] = nums[r]
                nums[r] = 0
            elif (nums[l] == 0 and nums[r] == 0):
                r += 1
            else:
                l += 1
                r += 1
        