import sys

ELEMENTS_FILE = 'elements.txt'

elements = []
with open(ELEMENTS_FILE, 'r') as f:
    for line in f.readlines():
        elem = [s.strip() for s in line.split('-')]
        elements.append(elem[1])


def elementalSpellings(word, wordguess='', partials=elements):
    if wordguess.lower() == word.lower():
        print(wordguess)
        return
    for part in partials:
        newguess = wordguess.lower()+part.lower()
        if word.lower().startswith(newguess):
            elementalSpellings(word, wordguess + part)


elementalSpellings('nonrepresentationalisms')
