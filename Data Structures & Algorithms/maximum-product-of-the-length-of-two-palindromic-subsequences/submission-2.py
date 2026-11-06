class Solution:
    def maxProduct(self, s: str) -> int:
        def dfs(i, a, b):
            if i == len(s):
                if a == a[::-1] and b == b[::-1]:
                    return len(a) * len(b)
                return 0

            return max(
                dfs(i + 1, a + s[i], b),
                dfs(i + 1, a , b + s[i]),
                dfs(i + 1, a , b),
            )

        return dfs(0, '', '')