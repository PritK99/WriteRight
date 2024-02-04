import nltk
import math
from nltk import word_tokenize
import enchant
from enchant.checker import SpellChecker

def spelling_error(essay):
    """
    Calculates the ratio of misspelled words in the essay and provides suggestions for corrections.

    Args:
    - essay (str): The input essay.
    - suggestions (list): A list to store suggestions for misspelled words.

    Returns:
    - float: The ratio of misspelled words to total words.
    """
    suggestions = []
    words = word_tokenize(essay)
    spell_checker = SpellChecker("en_US")
    sdict = enchant.Dict("en_US")
    spell_checker.set_text(" ".join(words))
    total_misspelled_words = len([error.word for error in spell_checker])
    
    # Iterate over misspelled words and collect suggestions
    for err in spell_checker:
        print("Hiiiiii")
        suggestion = spell_checker.suggest(err.word)[0]
        print(suggestion)
        suggestions.append(f"Did you mean {suggestion} instead of {err.word}?")

    return total_misspelled_words/len(words), suggestions

def syntax_check(essay, suggestions):
    """
    Performs syntax analysis by calculating a syntax score based on the ratio of misspelled words.

    Args:
    - essay (str): The input essay.

    Returns:
    - float: The syntax score ranging from 0.0 to 10.0.
    """
    alpha = 1.15     # Penalty Factor
    syntax_ratio, spelling_errors = spelling_error(essay)
    syntax_penalty = alpha*syntax_ratio*10
    syntax_score = 10 - syntax_penalty

    if (syntax_penalty > 4.5):
        for error in spelling_errors:
            suggestions.append(error)

    return max(syntax_score, 0)