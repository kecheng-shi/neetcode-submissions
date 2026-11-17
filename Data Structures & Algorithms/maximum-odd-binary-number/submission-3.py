class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt = Counter(s)
        res = ''
        for i in range(cnt['1'] - 1):
            res += '1'
        
        for i in range(cnt['0']):
            res += '0'

        res += '1'

        return res