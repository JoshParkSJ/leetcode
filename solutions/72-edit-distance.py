# recurisve naive approach
class Solution:
    def minDistance(self, word1, word2):
        """Naive recursive solution"""
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        insert = 1 + self.minDistance(word1, word2[1:])
        delete = 1 + self.minDistance(word1[1:], word2)
        replace = 1 + self.minDistance(word1[1:], word2[1:])
        return min(insert, replace, delete)

# we only pass in unprocessed letters
# if char1 == char2:
#    move on indexes i+1, j+1
# else:
#    - insert: orse vs ello => eorse vs ello => minDistance(orse, llo) => j+1
#    - delete: orse vs ello => rse vs ello => minDistance(rse, ello) => i+1
#    - replace: orse vs ello => erse vs ello => minDistance(rse, llo) => i+1, j+1

#-------------------------------------------------------------------------------------

# bottom up solution
# O(mn) time | O(mn) space
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # 2D array where the row and col has bottom/base values
        cache = [[float("inf")] * (len(word2)+1) for i in range(len(word1)+1)]
        
        # every last row (left -> right is 4,3,2,1,0)
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
            
        # every last column (top -> bottom is 4,3,2,1,0)
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i
        
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1])
        
        return cache[0][0]


# if char1 == char2
#   my cell = right bottom cell
# else:
#    insert: try j+1
#    delete: try i+1
#    replace: try i+1, j+1
#    my cell = 1 + min(insert, delete, replace)

             j
    #    a   c   d   ""
    # a              3  <- abd vs "" needs 3 inserts
i   # b              2  <- bd vs "" needs 2 inserts
    # d      1   0   1  <- d vs "" needs 1 insert
    # "" 3   2   1   0  <- "" vs "" needs 0 inserts





