class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = s.count("a")

        for i in range(1, n + 1):
            curr = dp[i - 1]
            if s[i - 1] == "a":
                curr -= 1
            else:
                curr += 1
            dp[i] = curr
        
        return min(dp)