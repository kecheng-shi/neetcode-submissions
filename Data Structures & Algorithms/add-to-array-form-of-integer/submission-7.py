class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        val = 0
        digit = 1

        while num:
            val += digit * num.pop()
            digit *= 10

        val += k

        res = []
        while val:
            res.append(val % 10)
            val //= 10

        return res[::-1]