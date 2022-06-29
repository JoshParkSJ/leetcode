class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        # key with no s, lambda x: x[0]
        sortedIntervals = sorted(intervals, key = lambda x: x[0])
        prevInterval = sortedIntervals[0]
        # important to initialize first because we skip this in the forloop
        # we start with an array in result, so we can extend it when we see an opportunity
        result = [prevInterval]
        
        for idx in range(1, len(sortedIntervals)):
            currInterval = sortedIntervals[idx]
            
            if prevInterval[1] >= currInterval[0]:
                # important to consider edge case: use max of both end times
                prevInterval[1] = max(currInterval[1], prevInterval[1])
            else:
                prevInterval = currInterval
                result.append(currInterval)
        
        return result