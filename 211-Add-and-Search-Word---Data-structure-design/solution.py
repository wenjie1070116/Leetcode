class TrieNode(object):
    def __init__(self):
        self.isword = None
        self.children = [None]*26
        
class WordDictionary(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        root = self.root
        for ch in word:
            idx = ord(ch)-ord('a')
            if not root.children[idx]:
                root.children[idx] = TrieNode
            root = root.children[idx]
        root.isword = word
    
    def searchnode(self, node, word, pos):
        if pos == len(word):
            if node.isword:
                return True
            return False
        if word[pos] != '.':
            idx = ord(word[pos])-ord('a')
            if node.children[idx] and self.search(node.children[idx], word, pos+1):
                return True
        else:
            for i in xrange(26):
                if node.children[i] and self.search(node.children[i], word, pos+1):
                    return True
        return False

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        root = self.root
        return self.searchnode(root, word, 0)
        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")