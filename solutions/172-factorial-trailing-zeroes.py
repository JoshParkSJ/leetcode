# O(logn) time with base 5 | O(1) space
class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        i = 5
        while n/i > 0:
            result += int(n/i)
            i *= 5
        return result
    
# trailing zero comes from 10
# 10 comes from 2x5 (prime numbers, meaning we can't chop up 2,5 into smaller multiples)
# we need to consider multiples of 2 and 5 (2,4,6,8,10... 5,10,15,20,25...)


# How many trailing zeros in 23!?
# 23 ÷ 5 = 4.6 = 4 factors of 5
# 23 ÷ 2 = 11.5 = 11 factors of 2 (but is limited by 4 because there's only 4 factors of 5)
# Therefore, 23! has 4 trailing zeros
# Now we know that factors of 2 will always be limited by factors of 5
# So let's just find the possible factors of 5, and the 2's will match the 5's to make 10

# How many trailing zeros in 4617!?
# 5^1 : 4617 ÷ 5 = 923.4, so we get 923 factors of 5
# 5^2 : 4617 ÷ 25 = 184.68, so we get 184 additional factors of 5
# 5^3 : 4617 ÷ 125 = 36.936, so we get 36 additional factors of 5
# 5^4 : 4617 ÷ 625 = 7.3872, so we get 7 additional factors of 5
# 5^5 : 4617 ÷ 3125 = 1.47744, so we get 1 more factor of 5
# 5^6 : 4617 ÷ 15625 = 0.295488, which is less than 1, so stop here.
# Therefore, 4617! has 923 + 184 + 36 + 7 + 1 = 1151 trailing zeroes.
# We need to consider factors of 5 like 25 because 25 x 4 = 100 
# and we always have a surplus of 2's to make the factors of 5 into a 10

