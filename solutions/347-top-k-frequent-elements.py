# O(nlogn) | O(n) space
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurances = {}
        for num in nums:
            occurances[num] = occurances.get(num, 0) + 1
        
        heap = []
        for key, val in occurances.items():
            heapq.heappush(heap, (-val, key))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res


# ------------------------
# bucket sort
# no frequencies can be more than n (since question says: k is in the range [1, num of unique elements in array])
# O(n) time | O(n) space
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        occurances = {}
        for num in nums:
            occurances[num] = occurances.get(num, 0) + 1
        
        for num, freq in occurances.items(): 
            bucket[freq].append(num)
        
        flatList = []
        for sublist in bucket:
            for item in sublist:
                flatList.append(item)

        return flatList[::-1][:k]
