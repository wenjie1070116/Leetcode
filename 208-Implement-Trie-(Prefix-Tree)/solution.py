class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isword = None
        self.children = [None]*26

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        root = self.root
        for ch in word:
            idx = ord(ch)-ord('a')
            if not root.children[idx]:
                root.children[idx] = TrieNode()
            root = root.children[idx]
        root.isword = word
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.root
        for ch in word:
            idx = ord(ch)-ord('a')
            if not root.children[idx]:
                return False
            root = root.children[idx]
        return root.isword is not None
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.root
        for ch in prefix:
            idx = ord(ch)-ord('a')
            if not root.children[idx]:
                return False
            root = root.children[idx]
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")