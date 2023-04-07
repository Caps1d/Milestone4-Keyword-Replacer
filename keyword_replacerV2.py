import string
from abbreviation_dict import abbreviation_dict


def keyword_replacerV2(corpus, abbreviation_dict):
    words = corpus.split()
    modified_words = []

    for i, word in enumerate(words):
        clean_word = word.strip(string.punctuation)
        precast_word = clean_word
        clean_word = clean_word.lower() if clean_word.lower(
        ) in abbreviation_dict else clean_word
        modified_word = abbreviation_dict.get(clean_word, clean_word)
        # Check for a full stop before the word and capitalize it if found
        if i > 0 and words[i-1][-1] == ".":
            modified_word = modified_word.capitalize()

        # Preserve punctuation marks from the original word
        prefix = word[:word.index(precast_word)
                      ] if precast_word in word else ""
        suffix = word[word.index(
            precast_word) + len(precast_word):] if precast_word in word else word

        modified_words.append(prefix + modified_word + suffix)

    modified_corpus = " ".join(modified_words)
    return modified_corpus
