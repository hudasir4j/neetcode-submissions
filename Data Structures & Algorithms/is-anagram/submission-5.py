class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        t_arr = []
        s_arr = []

        for c in t:
            t_arr.append(c)
        
        for c in s:
            s_arr.append(c)
        
        t_arr.sort()
        s_arr.sort()

        return t_arr == s_arr