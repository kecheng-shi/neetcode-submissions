class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_count = -1
        l, r = 0, 0

        while l < len(s):
            if r == len(s):
                l += 1
                r = l
                continue

            if s[r] == s[l] and r != l:
                max_count = max(max_count, r - l - 1)

            r += 1
        return max_count