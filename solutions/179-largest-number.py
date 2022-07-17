# O(nlogn) time | O(nlogn) space for recursion stack
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums = self.mergeSort(nums, 0, len(nums)-1)
        return str(int("".join(nums)))
    
    # split arrays into length 1 array
    def mergeSort(self, nums, l, r):
        if l > r:
            return 
        if l == r:
            return [nums[l]]
        mid = (l+r) // 2
        left = self.mergeSort(nums, l, mid)
        right = self.mergeSort(nums, mid+1, r)
        return self.merge(left, right)

    # merge arrays by comparing them with str(n1) + str(n2) > str(n2) + str(n1)
    def merge(self, l1, l2):
        res, i, j = [], 0, 0
        while i < len(l1) and j < len(l2):
            if self.compare(l1[i], l2[j]):
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1
        res.extend(l1[i:] or l2[j:])
        return res

    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)
