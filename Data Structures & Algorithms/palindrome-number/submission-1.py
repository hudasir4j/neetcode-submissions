class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        
        num_reversed = 0
        num = x

        while num != 0:
            print('num', num)
            last_num = num % 10
            print('last_num', last_num)
            num_reversed = (num_reversed * 10) + last_num
            print('num_reversed', num_reversed)
            num = num // 10

        
        return num_reversed == x