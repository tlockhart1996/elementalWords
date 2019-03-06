import sys

from trie import Trie, TrieNode

ELEMENTS_FILE = 'elements.txt'
WORDS_FILE = 'dictionary.txt'

elements = {}
with open(ELEMENTS_FILE, 'r') as f:
    for line in f.readlines():
        elem = [s.strip().lower() for s in line.split('-')]
        elements[elem[1]] = elem[2]

element_abbreviations = elements.keys()

words = []
with open(WORDS_FILE, 'r') as f:
    for line in f.readlines():
        if line.isalpha:
            words.append(line.strip().lower())

trie = Trie(words)


def findLongestWord(suffix_list):
    longestWord = ''
    prefix_list = ['']
    while len(prefix_list) != 0:
        for prefix in prefix_list:
            if trie.is_word(prefix) is not None and len(prefix) > len(longestWord):
                longestWord = prefix

        new_prefix_list = []
        for prefix in prefix_list:
            pref = prefix
            for suffix in suffix_list:
                new_prefix = pref + suffix
                if trie.is_prefix(new_prefix) or trie.is_word(new_prefix):
                    new_prefix_list.append(new_prefix)

        prefix_list = new_prefix_list
    return longestWord


print(findLongestWord(element_abbreviations))
