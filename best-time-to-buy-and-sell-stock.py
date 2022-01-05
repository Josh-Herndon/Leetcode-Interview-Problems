class Solution:
    def maxProfit(self, prices):

        maximum = 0
        minimum = float('inf')

        for price in prices:

            if price < minimum:
                minimum = price
            
            profit = price - minimum

            if profit > maximum:
                maximum = profit

        return maximum