class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        flatMatrix = [j for i in matrix for j in i]
        heapq.heapify(flatMatrix)
        return heapq.nsmallest(k,flatMatrix)[-1]