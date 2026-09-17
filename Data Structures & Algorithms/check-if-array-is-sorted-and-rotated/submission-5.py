class Solution:
    def check(self, nums: List[int]) -> bool:
        i = 0
        left = nums[0]

        while i < len(nums) - 1 and nums[i] <= nums[i + 1]:
            i += 1

        if i == len(nums) - 1:
            return True

        i += 1

        while i < len(nums) - 1 and nums[i] <= nums[i + 1]:
            i += 1
        
        right = nums[i]

        return i == len(nums) - 1 and left >= right

