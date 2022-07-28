# min heap
# O(klogk) time | O(k) space
class Solution: 
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        minHeap = []
        for r in range(min(k, m)):
            heappush(minHeap, (matrix[r][0], r, 0)) # val, row, col

        ans = -1
        for i in range(k):
            val, row, col = heappop(minHeap)
            ans = val
            if col+1 < n: 
                heappush(minHeap, (matrix[row][col + 1], row, col + 1))
        return ans


# --------------------------------
# simpler binary search
# key point: binary search on ranges, not index
# O(nm * log(max-min)) time | O(1) space
class Solution:
    def kthSmallest(self, matrix, k):
        m, n = len(matrix), len(matrix[0])

        def countK(mid):
            count = 0
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] <= mid: # count includes mid. why? ex) 1,4,4,4,5 & k=2 & mid = 4
                        count += 1          # if there's duplicate nums for kth val, the count will surpass k, and right = mid, so we won't overlook mid's num). i,e mid could be our answer too
                    else:                   # ex) 1,2,3 & k=2 & mid = 2
                        break               # our count will be 2 which is equal to k, hence right = mid, inclusive 
            return count

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2

            if countK(mid) < k:
                left = mid+1
            else:
                right = mid
                
        return left

# ----------------------------
# binary search
# key point: binary search on ranges, not index
# O(nm * log(max-min)) time | O(1) space
class Solution:
    def kthSmallest(self, matrix, k):
        m, n = len(matrix), len(matrix[0])

        def countLessOrEqual(x):
            cnt = 0
            c = n - 1  # start with the rightmost column
            for r in range(m):
                while c >= 0 and matrix[r][c] > x: c -= 1  # decrease column until matrix[r][c] <= x
                cnt += (c + 1)
            return cnt

        left, right = matrix[0][0], matrix[-1][-1]
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if countLessOrEqual(mid) >= k:
                ans = mid
                right = mid - 1  # try to looking for a smaller value in the left side
            else:
                left = mid + 1  # try to looking for a bigger value in the right side

        return ans