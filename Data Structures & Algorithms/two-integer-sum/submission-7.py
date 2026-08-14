class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if (complement in nums and nums.index(complement) != i):
                result.append(i)
                result.append(nums.index(complement))
                break
        result.sort()
        return result