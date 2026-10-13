class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnt = Counter(nums)

        for num in cnt:
            if cnt[num] % 2 != 0:
                return False

        return True