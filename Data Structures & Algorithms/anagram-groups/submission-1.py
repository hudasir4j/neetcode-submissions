class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq = defaultdict(list)

        for s in strs:
            code = [0] * 26
            for c in s:
                code[ord(c) - ord('a')] += 1
            
            key = tuple(code)
            freq[key].append(s)
        
        return list(freq.values())