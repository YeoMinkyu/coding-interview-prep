import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.stones = []

        for stone in stones:
            heapq.heappush(self.stones, -stone)

        while len(self.stones) >= 2:
            y = -heapq.heappop(self.stones)
            x = -heapq.heappop(self.stones)

            if x == y:
                pass
            else:
                y = y - x
                heapq.heappush(self.stones, -y)
            
        
        if not self.stones:
            return 0
        else:
            return -self.stones[0]
