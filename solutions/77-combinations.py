# O(kn^k) time
#   - O(n^k) for every digit of k, we have n branches
#   - O(kn^k) bc we create a new array of worst case size k every iteration
# O(n^k) space

# tight bound is O(k * n!/(n-k)!k!) because n!/(n-k)!k! is the formula for possible combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        possibleNums = [i for i in range(1,n+1)]
        combination = []
        self.recursion(possibleNums, combination, result, k)
        return result

    def recursion(self, unprocessedNums, combination, result, k):
        if len(combination) == k:
            result.append(combination)
            return
        
        for idx in range(len(unprocessedNums)):
            self.recursion(unprocessedNums[idx+1:], combination + [unprocessedNums[idx]], result, k)