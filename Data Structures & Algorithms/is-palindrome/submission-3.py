class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = True
        clean = "".join([char for char in s if char.isalnum()]).lower()

        l, r = 0, len(clean) - 1

        while (r > l):
            if (clean[l] != clean[r]):
                result = False
            l += 1
            r -= 1
        return result