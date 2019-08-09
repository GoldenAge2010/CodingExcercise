class Solution(object):
    def maxProfit(self, prices):

        buy, sell = float('-inf'), 0

        for price in prices:
            buy = max(buy, - price)
            sell = max(sell, price + buy)
        return sell

sln = Solution()

# input
prices = [3,8,8,55,38,1,7,42,54,53]

rst = sln.maxProfit(prices)

print(rst)