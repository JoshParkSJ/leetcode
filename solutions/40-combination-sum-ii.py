# O(2^n) where n is the size of candidates | O(n) space
# 2^n bc result has unique candidates -> include or not include candidate 2^n
# if we decide not to use a candidate, make sure all duplicates are also not considered
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()                      
        result = []
        self.combine_sum_2(candidates, 0, [], result, target)
        return result

    def combine_sum_2(self, nums, start, path, result, target):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(nums)):
            # example below
            if i > start and nums[i] == nums[i - 1]:
                continue
            # just for efficiency
            if nums[i] > target:
                break

            self.combine_sum_2(nums, i+1, path + [nums[i]], result, target - nums[i])
                       
            # candidates = [1,1,7]
            # target = 8
            
            #--- i=0
            # 1x,1,7
            # start = 0
            # path = [1]

                    #--- i=1
                    # 1,1x,7
                    # start = 1
                    # path = [1,1] -> 3rd recursion will never lead to 8 so I'll skip

                    #--- i=2
                    # 1,1,7x
                    # start = 2
                    # path = [1,7] -> add to result
            
            #--- i=1
            # 1,1x,7
            # start = 0
            # path = [] skip bc i > start and nums[i] == nums[i - 1]
            
            #--- i=2
            # 1,1,7x
            # start = 0
            # path = [7]

                    #--- i=3
                    # 1,1,7,x (out of bound)
                    # start = 3
                    # path = [7]   