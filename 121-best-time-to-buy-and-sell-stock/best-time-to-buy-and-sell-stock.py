class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_ = float(inf)
        max_profit=0
        for i in prices:
            min_=min(i,min_)
            profit = i-min_
            # print(profit)
            
            max_profit = max(max_profit,profit)
            # print(max_profit)

        return max_profit
        # ans=0
        # for i in range(len(prices)):
        #     pev=prices[i]
        #     max_=pev
        #     for j in range(i,len(prices)):
        #         max_ = max(max_,prices[j])

        #     profit=max_ - pev
        #     ans = max(profit,ans)

        # return ans

        