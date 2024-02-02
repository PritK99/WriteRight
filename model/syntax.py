import nltk
import math
from nltk import word_tokenize
from enchant.checker import SpellChecker

def spelling_error(essay):
    words = word_tokenize(essay)
    spell_checker = SpellChecker("en_US")
    spell_checker.set_text(" ".join(words))
    total_misspelled_words = len([error.word for error in spell_checker])
    print("Syntax errors identified: ")
    for error in spell_checker:
        print(error.word, error.suggestions)

    return total_misspelled_words/math.sqrt(len(words))

def syntax_check(essay):
    syntax_ratio = spelling_error(essay)
    syntax_penalty = syntax_ratio*10
    syntax_score = 10 - syntax_penalty

    return max(syntax_score, 0)