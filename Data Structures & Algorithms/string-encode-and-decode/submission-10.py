class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs != []:
            res = "#LOL".join(strs)
        else:
            res = "#BRO"
        return res

    def decode(self, s: str) -> List[str]:
        
        if ('#BRO' == s):
            print('HI')
            return []

        res = s.split("#LOL")
        return res
