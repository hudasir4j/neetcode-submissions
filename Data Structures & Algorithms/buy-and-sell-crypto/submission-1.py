class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left = 0
        right = 1

        while (right < len(prices)):
            print("Current:", prices[left], prices[right])
            if (prices[left] > prices[right]):
                print("moving up!")
                left = right
                right += 1
                
                if(maxProfit <= 0):
                    maxProfit = 0
            else:
                if(prices[right] - prices[left] > maxProfit):
                    maxProfit = prices[right] - prices[left]
                    print(maxProfit, prices[right],prices[left])
                right += 1
        
        return maxProfit

        #left = 0 / prices[left] = 10
        #right = 1 / prices[right] = 1

        #left = 1 / prices[left] = 1
        #right = 2 / prices[right] = 5

