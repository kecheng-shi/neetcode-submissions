class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        for _ in range(k):
            minIdx = 0
            for i in range(n):
                if nums[i] < nums[minIdx]:
                    minIdx = i
            nums[minIdx] = nums[minIdx] * multiplier
                    
        
        return nums