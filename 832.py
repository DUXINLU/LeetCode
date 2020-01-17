class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        l=len(A)
        for i in range(l):
            A[i].reverse()
            for j in range(l):
                A[i][j]=1-A[i][j]
        return A