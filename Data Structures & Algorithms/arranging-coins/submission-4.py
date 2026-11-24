class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            if n > (1 + mid) * mid / 2:
                left = mid + 1
            elif n < (1 + mid) * mid / 2:
                right = mid - 1
            else:
                return mid
        return right