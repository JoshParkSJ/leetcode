class TrieNode:
    def __init__(self):
        self.children = {}
        
    def addWord(self, word):
        for char in word:
            if char not in self.children:
                self.children[char] = TrieNode()
            self = self.children[char]
        self.children['#'] = True

# O(4*3^L) time worst case | O(n) space for trie
# 4 directions, each direction can go 3 paths since we came from one direction, and we repeat visiting 3 neighbours for L characters where L is the max length of word
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        for word in words:
            trie.addWord(word)
        
        ROWS, COLS = len(board), len(board[0])
        result, visited = set(), set()
        
        def dfs(row, col, node, word):
            if (row == ROWS or col == COLS or
                row < 0 or col < 0 or
                (row, col) in visited or
                board[row][col] not in node.children):
                return
            
            visited.add((row, col))
            word += board[row][col]
            node = node.children[board[row][col]]
            
            if '#' in node.children:
                result.add(word)
            
            dfs(row+1, col, node, word)
            dfs(row-1, col, node, word)
            dfs(row, col+1, node, word)
            dfs(row, col-1, node, word)
            
            visited.remove((row, col))
            
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, trie, '')
        
        return list(result)