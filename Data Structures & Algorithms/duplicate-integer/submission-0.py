class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter(nums)

        for key in cnt:
            if cnt[key] > 1:
                return True

        return False