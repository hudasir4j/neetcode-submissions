class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}

        for str in strs:
            sorteda = list(str)
            sorteda.sort()
            sorteds = "".join(sorteda)

            if sorteds not in freq:
                freq[sorteds] = [str]
            else:
                freq[sorteds].append(str)
                
        return list(freq.values())
        