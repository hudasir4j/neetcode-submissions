class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            curr = nums[i]
            compliment = target - curr

            if(compliment in nums and nums.index(compliment) != i):
                result.append(i)
                result.append(nums.index(compliment))
                break
            
        result.sort()
            
        return result
