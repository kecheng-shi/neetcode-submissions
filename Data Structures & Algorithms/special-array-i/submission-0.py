class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        prev = None
        for num in nums:
            if prev is None:
                prev = (num % 2 == 0)
                continue
            else:
                curr = (num % 2 == 0)
            
            if prev == curr:
                return False

            prev = curr
        return True