class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            mid = (left + right) // 2
            mid_sum = (1 + mid) * mid / 2
        

            if mid_sum == n:
                return mid
                
            elif mid_sum < n:
                left = mid + 1
            else:
                right = mid - 1
                
        return right
