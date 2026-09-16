from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        odd, even = 0, float("inf")

        for cnt in freq.values():
            if cnt % 2 == 1:
                odd = max(odd, cnt)
            else:
                even = min(even, cnt)
        return odd - even

        