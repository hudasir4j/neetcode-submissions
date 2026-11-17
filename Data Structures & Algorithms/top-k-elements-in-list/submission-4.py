class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        arr = []
        for num, cnt in freq.items():
            arr.append([cnt, num])
        
        arr.sort()
        
        res = []
        for i in range(k):
            res.append(arr.pop()[1])

        return res