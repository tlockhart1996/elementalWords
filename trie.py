'''
Trie class will be built with a list of words
It will be used for searching an autocompleting words
'''


class TrieNode:
    def __init__(self):
        # children is a dictionary from next character to the next trie node
        self.children = {}
        self.data = None

    @staticmethod
    def insert(node, word):
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.data = word

    @staticmethod
    def find(node, word):
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return None
        return node.data

    @staticmethod
    def is_prefix(node, prefix):
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return len(node.children.keys()) != 0

    @staticmethod
    def is_word(node, word):
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return node.data is not None

    @staticmethod
    def print_all_words_after_node(node):
        if node.data:
            print(node.data)
        for childNode in node.children.values():
            TrieNode.print_all_words_after_node(childNode)

    @staticmethod
    def print_all_words_after_prefix(node, prefix):
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                print("NONE EXISTS")
                return
        TrieNode.print_all_words_after_node(node)


class Trie:
    # build the trie from the words given.

    def __init__(self, words):
        self.top = TrieNode()
        for word in words:
            TrieNode.insert(self.top, word)
        print("Built Trie!")

    def find(self, word):
        return TrieNode.find(self.top, word)

    def insert(self, word):
        TrieNode.insert(self.top, word)

    def is_prefix(self, prefix):
        return TrieNode.is_prefix(self.top, prefix)

    def print_all_words_after_prefix(self, prefix):
        TrieNode.print_all_words_after_prefix(self.top, prefix)

    def is_word(self, word):
        return TrieNode.is_word(self.top, word)
