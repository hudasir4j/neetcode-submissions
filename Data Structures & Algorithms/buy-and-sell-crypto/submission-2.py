class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Consider the smallest number on the left of i
        maxProfit = 0
        left = 0
        right = 1

        while (right < len(prices)):
            if (prices[left] > prices[right]):
                left, right = right, right + 1
                if (maxProfit < 0):
                    maxProfit = 0
            else:
                maxProfit = max(maxProfit, prices[right] - prices[left])
                right += 1
            
        return maxProfit


            
