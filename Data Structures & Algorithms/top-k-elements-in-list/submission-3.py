class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        arr = []
        for num, fre in freq.items():
            arr.append([fre, num])
        arr.sort()

        while len(res) < k:
            res.append(arr.pop()[1])

        return res