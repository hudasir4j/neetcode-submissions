class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []

        for i in range(len(nums)):
            looking_for = target - nums[i]

            if (looking_for in nums and nums.index(looking_for) != i):
                res.append(i)
                res.append(nums.index(looking_for))
                break
        
        res.sort()
        return res
            
