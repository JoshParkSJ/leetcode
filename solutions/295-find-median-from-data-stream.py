class MedianFinder:

    # O(n) space
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = [] # store high nums, pop smallest big number
        self.maxHeap = [] # store low nums, pop biggest small number

    # O(logn) time
    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        minOfMaxHeap = -heapq.heappop(self.maxHeap)
        heapq.heappush(self.minHeap, minOfMaxHeap)
        if len(self.minHeap) > len(self.maxHeap):
            maxOfSmallNums = heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -maxOfSmallNums)
    # O(1) time
    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        return (-self.maxHeap[0] + self.minHeap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()