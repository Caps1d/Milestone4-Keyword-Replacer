import string
from abbreviation_dict import abbreviation_dict


class Node:
    def __init__(self):
        self.children = {}
        self.keywords = {}


class KeywordReplacer:
    def __init__(self, abbreviations):
        self.root = Node()
        for abbreviation, phrase in abbreviations.items():
            first_letter = abbreviation[0]
            # extracts a node that represents the corresponding letter or provides an empty node
            node = self.root.children.get(first_letter, Node())
            # adds the full phrase with the matching key to the node
            node.keywords[abbreviation] = phrase
            # adds the processed node to the root
            self.root.children[first_letter] = node

    def replace_keywords(self, text):
        words = text.split()
        result = []
        for word in words:
            if len(word) == 1 or word[0] in string.punctuation:
                result.append(word)
            else:
                # in case a keyword starts with a capital letter
                wordLow = word.lower()
                node = self.root.children.get(wordLow[0])
                if node is None:
                    result.append(word)
                else:
                    phrase = node.keywords.get(wordLow)
                    if phrase is None:
                        result.append(word)
                    else:
                        result.append(phrase)
        return ' '.join(result)


# abbreviations = {"can't": "cannot", "ain't": "am not",
#                  "haven't": "have not", "w/": "with",
#                  "w/o": "without", "etc.": "and so on",
#                  "asap": "as soon as possible", "you're": "you are",
#                  "q&e": "quick and easy"}
# replacer = KeywordReplacer(abbreviations)

# corpus = "I ain't looking for a q&e answer. Since we haven't even understood the concept yet, we can't go on like that! Get to it asap or you're fired!"
# result = replacer.replace_keywords(corpus)
# print(result)
# Modified Corpus: "I am not looking for a quick and easy answer. Since we have not even understood the concept yet, we cannot go on like that! Get to it as soon as possible or you are fired!"
