class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        sorted_prices = sorted(prices)
        all_money = money
        count = 2
        for price in sorted_prices:
            all_money -= price
            if count > 0 and all_money < 0:
                return money
            count -= 1
            if count == 0:
                return all_money