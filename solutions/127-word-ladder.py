# O(nm^2) time | O(nm^2) space
# M is the length of each word and N is the total number of words in the input word list.
# idea: create adj list for patterns and do a BFS to find the shortest path
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # initialize a dictionary, if key dne, make the value an empty list
        neighbours = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                # { *ot: [hot, dot, bot] }
                pattern = word[:j] + "*" + word[j+1:]
                neighbours[pattern].append(word)
        
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in neighbours[pattern]:
                        if neiWord not in visited:
                            visited.add(neiWord)    
                            q.append(neiWord) 
            res += 1
        return 0


# -----------------------------------------------------------

# this soln TLE because we have to optimize for n since length of m is much shorter than n
# O(lmn^2) time | O(n) space
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        sequences = []
        self.findSequence(beginWord, endWord, wordList, 1, sequences)
        return 0 if len(sequences) == 0 else min(sequences)
        
    # O(n) time | O(n) space
    def findSequence(self, currWord, endWord, wordList, currSeqLen, sequences):
        if self.differsByOneLetter(currWord, endWord):
            sequences.append(currSeqLen+1)
            return
        
        # O(m) time
        for idx,word in enumerate(wordList):
            # O(l) time
            if self.differsByOneLetter(currWord, word):
                # O(n) time
                self.findSequence(word, endWord, wordList[idx+1:] + wordList[:idx], currSeqLen+1, sequences)
        
    def differsByOneLetter(self, word1, word2):
        differenceCount = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                differenceCount += 1
        return differenceCount == 1







