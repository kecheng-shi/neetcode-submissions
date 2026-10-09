class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = Counter(arr1)
        res = []
        for num in arr2:
            for _ in range(cnt[num]):
                res.append(num)
            del cnt[num]

        for num in sorted(cnt):
            for _ in range(cnt[num]):
                res.append(num)
        return res