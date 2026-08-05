class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        answer = False
        empty = set()
        for i in range(len(nums)):
            if nums[i] in empty:
                answer = True;
            empty.add(nums[i])
            
        return answer