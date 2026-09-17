class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat[0])
        count = 0
        for i in range(n):
            for j in range(n):
                if i == j or i == n - j - 1:
                    count += mat[i][j]
        
        return count