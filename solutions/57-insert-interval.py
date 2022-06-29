# O(n) time | O(n) space

# sometimes, instead of considering every case ever
# we can abstract these cases into ideas

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for idx in range(len(intervals)):
            if newInterval[0] > intervals[idx][1]:
                # newInterval is after this interval
                result.append(intervals[idx])
            elif newInterval[1] < intervals[idx][0]:
                # newInterval is before this interval
                result.append(newInterval)
                return result + intervals[idx:]
            else:
                # if case is anything else (all the cases below)
                # force newInterval to be before next interval (or nxt nxt)
                newInterval[0] = min(newInterval[0], intervals[idx][0])
                newInterval[1] = max(newInterval[1], intervals[idx][1])
        result.append(newInterval)
        return result
        
# intervals: [[1,3], [6,9]]
# new:       [0,  4]

# intervals: [[1,3], [6,9], [10,11]]
# new:              [4,8]

# intervals: [[1,3], [6,9], [12,14]]
# new:                 [7,10]

# intervals: [[1,3], [6,9]]
# new:          [2,    7]

# intervals: [[1,3], [6,9], [7,11]]
# new:          [2,           10]

# intervals: [[1,3], [6,9]]
# new:              [4,   11]


