class Solution:
    def check(self, nums: List[int]) -> bool:
        cnt = 0
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] <= nums[(i + 1) % n]:
                cnt += 1
        
        return cnt >= n - 1