class Solution:
    def maxScore(self, s: str) -> int:
        hightest = 0
        for i in range(1, len(s)):
            curr = 0
            for j in range(0, i):
                if s[j] == "0":
                    curr += 1
                    
            for k in range(i, len(s)):
                if s[k] == "1":
                    curr += 1

            hightest = max(curr, hightest)

        return hightest