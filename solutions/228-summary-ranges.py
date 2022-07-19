# O(n) time | O(1) space
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        prev = nums[0]
        curr = [prev, None]
        ranges = [curr]
        for idx in range(1, len(nums)):
            num = nums[idx]
            if prev + 1 == num:
                prev = num
                curr[1] = num
                continue
            curr = [num, None]
            ranges.append(curr)
            prev = num
        
        result = []
        for summaryRange in ranges:
            if summaryRange[1]:
                result.append(str(summaryRange[0]) + "->" + str(summaryRange[1]))
            else:
                result.append(str(summaryRange[0]))
            
        return result