class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Go through and make a frequency dictionary
        # After, create a for loop of range k and append to output

        result = []
        freq_dict = {}

        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        
        sorted_nums = sorted(
            freq_dict,
            key = freq_dict.get,
            reverse = True
        )

        return sorted_nums[:k]
