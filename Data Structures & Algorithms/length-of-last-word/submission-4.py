class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        first = True
        i = 0

        while i < len(s) and first:
            if s[-1 - i] != ' ':
                i += 1
                cnt += 1
            elif s[-1 - i] == ' ' and cnt > 0:
                first = False
            else:
                i += 1
        
        return cnt