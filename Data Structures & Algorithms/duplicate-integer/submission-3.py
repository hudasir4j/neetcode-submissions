class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = False
        store = {}

        for i in range(len(nums)):
            store[nums[i]] = store.get(nums[i], 0) + 1
            if(store[nums[i]] > 1):
                result = True
        
        return result
        
