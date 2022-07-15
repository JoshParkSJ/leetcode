# don't focus on the actual number, focus on the states 2 <-> 2b <-> 2c

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seenOnce = seenTwice = 0
        
        for num in nums:            
            #                change     if seenTwice is unchanged
            seenOnce = (seenOnce ^ num) & ~seenTwice
            #                change     if seenOnce is unchanged
            seenTwice = (seenTwice ^ num) & ~seenOnce
            # ^seenTwice so we can cancel/turn back seenTwice (meaning n & ~n) (2nd occur)
            # ^seenOnce  so we can cancel/turn back seenTwice (meaning n & ~n) (3rd occur)
            
        return seenOnce

# ------------------------
# memorize
# n ^ 0 = n       (XOR)
# n & -1 = n      (AND)
# n & ~n = 0      (AND)
# ------------------------
# optional
# n & -n = 1      (AND)
# ~0 = -1         (NOT)
# ------------------------

# current state:
# seenOnce = 0
# seenTwice = 0

# first appearance: 
# seenOnce = num
# seenTwice = no change

# second appearance: 
# seenOnce = turn back
# seenTwice = num

# third appearance: 
# seenOnce = no change
# seenTwice = turn back

# hence, 3 appearances will cancel out the number and turn back
# whatever is in seenOnce is answer (since it turned once, and never turned back)