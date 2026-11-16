class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result = []

        for i in range(len(nums)):
            looking_for = target - nums[i]
            if (looking_for in nums and nums.index(looking_for) != i):
                result = [nums.index(looking_for), i]
        
        return result
        