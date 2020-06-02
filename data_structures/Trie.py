from collections import defaultdict


# Implement a trie with insert, search, and startsWith methods.
#
# Example:
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");
# trie.search("app");     // returns true
# Note:
#
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.

class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.terminating = False


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.create_node()

    def create_node(self):
        return TrieNode()

    def get_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        root = self.root

        for i in range(len(word)):
            root = root.children[word[i]]

        root.terminating = True

    def search(self, word, fullSearch=True):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.root
        len1 = len(word)

        for i in range(len1):
            index = self.get_index(word[i])
            if not root:
                return False
            root = root.children.get(index)
        if (fullSearch):
            return True if root and root.terminating else False
        else:
            return True if root else False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

        return self.search(prefix, False)

