class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = r = 0
        n = len(nums)
        cnt = 0
        curr = 0
        ways = 0

        while r < n:
            if nums[r] % 2 == 1:
                curr += 1
                ways = 0
            
            while curr == k:
                ways += 1
                curr -= nums[l] % 2
                l += 1

            cnt += ways
            r += 1
        return cnt
