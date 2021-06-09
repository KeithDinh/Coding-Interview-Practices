class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify(stones)
        k = 1
        while len(stones) > 1:
            twoHeaviest = heapq.nlargest(2, stones)

            if twoHeaviest[0] != twoHeaviest[1]:
                stones.append(abs(twoHeaviest[0] - twoHeaviest[1]))
                
            stones.remove(twoHeaviest[0])
            stones.remove(twoHeaviest[1])
            heapq.heapify(stones)
        
        if stones:
            return stones[-1]
        return 0
            