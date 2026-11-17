class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        res = 0
        ctr = 0


        for i in range(len(nums)):
            next_idx = i + 1
            if (nums[i] == 1):
                ctr = 1
                while (next_idx < len(nums) and nums[next_idx] == 1):
                    ctr += 1
                    next_idx += 1
                res = max(res, ctr)
            else:
                next_idx += 1

        return res
                


        