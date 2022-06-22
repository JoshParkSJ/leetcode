# O(n) time | O(1) space
# greedy algorithm / implicit bfs solution

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, end, furthest = 0, 0, 0,
        
        for i in range(len(nums)-1):
            furthest = max(furthest, i+nums[i])

            # visited all the items on the current level
            if i == end:
                # increment level
                jumps += 1
                # getting the queue size (level size) for the next level you are traversing
                end = furthest
        return jumps
