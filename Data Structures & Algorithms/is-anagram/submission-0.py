class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_hash = {}
        t_hash = {}
        answer = True

        for char in s.lower():
            s_hash[char] = s_hash.get(char, 0) + 1

        for char in t.lower():
            t_hash[char] = t_hash.get(char, 0) + 1
        
        for key in s_hash:
            if(not(t_hash.get(key) == s_hash[key])):
                answer = False

        return answer
