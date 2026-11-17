class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        if self.minheap and num > self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)
        

        if len(self.maxheap) > len(self.minheap) + 1:
            val = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -val)
        if len(self.maxheap) + 1 < len(self.minheap):
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -val)




    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        
        return (self.minheap[0] - self.maxheap[0]) / 2.0
        
