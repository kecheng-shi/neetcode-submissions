class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for num in nums:
            res *= num

        return self.signFunc(res)
    

    def signFunc(self, x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0