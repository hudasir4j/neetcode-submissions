class Solution:
    def romanToInt(self, s: str) -> int:
        
        hashmap = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M': 1000}
        total = 0
        l,r = 0,1

        while(l < len(s)):

            if (r < len(s) and hashmap[s[r]] > hashmap[s[l]]):
                total += (hashmap[s[r]]-hashmap[s[l]])
                l += 2
                r += 2
            else:
                total += hashmap[s[l]]
                l += 1
                r += 1
                
        return total