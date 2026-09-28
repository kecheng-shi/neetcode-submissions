class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        odd = False
        
        for value in cnt.values():
            if not value & 1:
                ans += value
            else:
                if not odd:
                    ans += value
                    odd = True
                else:
                    ans += value - 1
        
        return ans