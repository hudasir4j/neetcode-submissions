class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = False
        frequency = {}

        for i in range(len(nums)):
            frequency[nums[i]] = frequency.get(nums[i], 0) + 1
            if(frequency.get(nums[i]) > 1):
                result = True
                break
        
        return result
        