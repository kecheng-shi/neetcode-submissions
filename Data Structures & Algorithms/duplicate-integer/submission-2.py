class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter(nums)

        if cnt and max(cnt.values()) > 1:
            return True
        else:
            return False