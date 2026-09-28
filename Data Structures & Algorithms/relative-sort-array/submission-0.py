class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_count = Counter(arr1)
        arr2_count = Counter(arr2)
        res = []
        notin = []

        for num in arr2:
            for i in range(arr1_count[num]):
                res.append(num)
        
        for num in arr1:
            if num not in arr2_count:
                notin.append(num)
        
        notin.sort()
        res += notin

        return res