class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_arr = []
        t_arr = []

        for c in s:
            s_arr.append(c)
        
        for c in t:
            t_arr.append(c)
        
        t_arr.sort(key=str.casefold)
        s_arr.sort(key=str.casefold)


        return t_arr == s_arr
