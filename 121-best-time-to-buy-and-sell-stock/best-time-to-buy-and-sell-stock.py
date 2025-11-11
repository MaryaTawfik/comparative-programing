class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')   # Start with a very high value
        max_profit = 0             # No profit initially

        for price in prices:
            # Update minimum price if current price is lower
            if price < min_price:
                min_price = price
            # Calculate profit if selling today
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
