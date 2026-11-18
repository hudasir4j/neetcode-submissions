class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if (nums == []):
            return 0

        nums.sort()
        print(nums)

        max_ct = 1
        ctr = 1

        for i in range(len(nums) - 1):
            next_val = nums[i + 1]

            if (next_val == nums[i] + 1):
                ctr += 1
                max_ct = max(max_ct, ctr)
            elif next_val == nums[i]:
                continue
            else:
                ctr = 1
        
        return max_ct

        