class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker = {}

        for i in nums:
            if (i in tracker):
                tracker[i] += 1
            else:
                tracker[i] = 1
        
        for num in tracker:
            if tracker.get(num) > 1:
                return True
        
        return False