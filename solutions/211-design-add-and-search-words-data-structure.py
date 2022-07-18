class WordDictionary:

    def __init__(self):
        self.trie = {}

    # O(word) time | O(word) space
    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            node = node.setdefault(char, {})
        node['#'] = True

    def search(self, word: str) -> bool:
        return self.searchTrie(self.trie, word)
    
    # P(w*26^w) time for 26 alphabets | O(w) space
    def searchTrie(self, node, word) -> bool:
        for idx, char in enumerate(word):
            if char == '.':
                for wildChar in node:
                    if wildChar != '#' and self.searchTrie(node[wildChar], word[idx+1:]):
                        return True
            if char not in node:
                return False
            node = node[char]
        return '#' in node
