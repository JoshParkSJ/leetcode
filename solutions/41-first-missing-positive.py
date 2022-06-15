class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
         Basic idea:
        1. for any array whose length is n, the first missing positive must be in range [1,...,n+1], so we only have to care about those elements in this range and remove the rest. First missing positive number has to be from 1...n+1 because "worst case" is [1,2,3,4] where first missing positive number is 5. For [1,1,1,1] it's 2, and this is still in 1...n+1.
        2. we can use the array index as the hash to restore the frequency of each number within the range [1,...,n+1]
        """
        
        # we append 0 because hash function is used to check if an index 0...n-1 has been used or not. if you dont append 0, it will always return 0 as the answer
        nums.append(0)
        n = len(nums)
        
        #delete those useless elements
        for i in range(len(nums)):
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        
        # use the index as the hash to record the frequency of each number
        # 1. val % n will always return val because we took out values bigger than n
        # 2. index => num, 
        #    val => occured/not if val is divisible by n
        #    if divisible by n then this idx is some num's hash (i.e if idx 2, val 2 exists)
        # 3. we add n so that hashing/modulo is not affected/overriden by previous hashes
        #    also double wammy for dividing by 5 to see if this idx was "visied" (i.e if an index 3 is n, that means 5%5=0, 0 occurances of 3)
        for i in range(len(nums)):
            nums[nums[i]%n]+=n

        for i in range(1,len(nums)):
            # 5%5 == 0 or even simpler, if nums[i] < n
            # first number with 0 occurances is answer
            if nums[i] < n:
                return i

        return n