class Solution(object):
    def coinChange(self, coins, amount):

        coins.sort(reverse = True)
        coinNum = [0] * len(coins)

        for i, coin in enumerate(coins):
            while amount >= coin:
                amount -= coin
                coinNum[i] += 1

        return coinNum

sln = Solution()

# input
coins = [25,10,5,1]
amount = 83

rst = sln.coinChange(coins, amount)

print(rst)