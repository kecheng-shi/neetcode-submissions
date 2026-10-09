class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hash_set = set(range(1, n + 1))

        for num in nums:
            if num in hash_set:
                hash_set.remove(num)
        
        res = []
        for num in hash_set:
            res.append(num)
        return  res
