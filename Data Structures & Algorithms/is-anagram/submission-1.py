class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = False
        if(len(s) != len(t)):
            result = False

        s_sorted = "".join(sorted(s))
        t_sorted = "".join(sorted(t))

        if(s_sorted == t_sorted):
            result = True
        
        return result