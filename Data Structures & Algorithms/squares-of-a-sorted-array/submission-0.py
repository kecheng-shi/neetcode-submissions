import numpy as np
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        array = np.asarray(nums)
        return sorted(array**2)