class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = True
        text = "".join([char for char in s if char.isalnum()]).lower()

        left = 0
        right = len(text) - 1

        while(right > left):
            
            if (text[right] != text[left]):
                result = False
                break
            left += 1
            right -= 1

            
        return result

