class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_c = nums1.copy()
        i = 0
        j = 0
        while i < m and j < n:
            idx = i + j
            if nums1_c[i] < nums2[j]:
                nums1[idx] = nums1_c[i]
                i += 1
            else:
                nums1[idx] = nums2[j]
                j += 1
        
        while i < m:
            idx = i + j
            nums1[idx] = nums1_c[i]
            i += 1
        
        while j < n:
            idx = i + j
            nums1[idx] = nums2[j]
            j += 1
                
            