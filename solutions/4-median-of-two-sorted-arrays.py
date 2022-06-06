# O(log(m) + log(n)) time | O(1) space
# O(log(m) + log(n)) ≤ O(log(m⋅n)) = log(m) + log(n) ≤ 2⋅log(m+n)

# should revisit with a simpler solution
class Solution:
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.   
    
    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2 , len(b) // 2
        ma, mb = a[ia], b[ib]
    
        # when k is bigger than the sum of a and b's median indices 
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)
    
"""
answer = 5
combined = [1,2,3,/5/,6,7,8]

A1: [1,5,6,7], A2: [2,3,8]
k = 3
ia = 2, ib = 1
ma = 6, mb = 3

A1: [1,5], A2: [2,3,8]
k = 3
ia = 1, ib = 1
ma = 5, mb = 3

A1: [1,5], A2: [8]
k = 1
ia = 1, ib = 0
ma = 5, mb = 8

A1: [1,5], A2: []
k = 1

A1[1] = 5 = answer
"""
