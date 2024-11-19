import nltk
import math
import re
import spacy
import string
import language_tool_python
from nltk import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
import enchant
from enchant.checker import SpellChecker

lemmatizer = WordNetLemmatizer()
tool = language_tool_python.LanguageTool('en-US')
nlp = spacy.load('en_core_web_sm')
spell_checker = SpellChecker("en_US")
spell_dict = enchant.Dict("en_US")

# Grammar rules dictionary
rule_dic = {
    'i': ['am', 'could', 'should', 'have', 'did', 'had', 'will', 'was', 'can', 'shall', 'may', 'might', 'must', 'would'],
    'he': ['is', 'could', 'should', 'did', 'has', 'will', 'had', 'was', 'can', 'shall', 'may', 'might', 'must', 'would'],
    'you': ['are', 'had', 'could', 'should', 'did', 'have', 'will', 'were', 'can', 'shall', 'may', 'might', 'must', 'would']
}

def spelling_check(essay):
    """
    Checks spelling in the essay and returns error ratio and suggestions.

    Args:
    - essay (str): The input essay text.

    Returns:
    - tuple: (error_ratio, suggestions)
        - error_ratio (float): Ratio of misspelled words
        - suggestions (list): List of spelling suggestions
    """
    suggestions = []
    words = word_tokenize(essay)
    spell_checker.set_text(" ".join(words))
    total_misspelled_words = len([error.word for error in spell_checker])
    
    for err in spell_checker:
        if spell_checker.suggest(err.word):
            suggestion = spell_checker.suggest(err.word)[0]
            suggestions.append(f"Spelling: Did you mean '{suggestion}' instead of '{err.word}'?")
    
    return total_misspelled_words/len(words), suggestions

def clean_sentence(sentence):
    """
    Cleans and normalizes sentence for grammar checking.

    Args:
    - sentence (str): Input sentence.

    Returns:
    - str: Cleaned sentence
    """
    sen_split = sentence.split()
    temp_list = []
    [temp_list.append(i.lower()) if not i.islower() else temp_list.append(i) for i in sen_split]
    
    if 'customer' in temp_list or 'she' in temp_list or 'it' in temp_list:
        sentence = ' '.join('He' if x in ['Customer', 'She', 'It'] else 'he' if x in ['customer', 'she', 'it'] else x for x in sen_split)
    if 'they' in temp_list or 'we' in temp_list:
        sentence = ' '.join('you' if x in ['they', 'we'] else 'You' if x in ['They', 'We'] else x for x in sen_split)
    return sentence

def check_grammar_rules(sentence):
    """
    Checks grammar rules for a sentence.

    Args:
    - sentence (str): Input sentence.

    Returns:
    - list: Grammar errors found
    """
    error_list = []
    
    matches = tool.check(sentence)
    for match in matches:
        if str(match.message) not in [
            'Possible typo: you repeated a whitespace',
            'Add a space between sentences',
            'Possible spelling mistake found'
        ]:
            suggestions = match.replacements 
            suggestion_text = f" Suggestions: {', '.join(suggestions)}" if suggestions else ""
            error_list.append(f"Grammar: {match.message}{suggestion_text}")
    
    cleaned_sentence = clean_sentence(sentence)
    
    if not re.search(r'[\.?!]$', cleaned_sentence.strip()):
        error_list.append("Grammar: Sentence should end with proper punctuation (., ?, !).")
    
    sen_split = cleaned_sentence.split()
    for word in sen_split:
        word = word.translate(str.maketrans('', '', string.punctuation))
        if word and nlp(word)[0].tag_ in ['NNP', 'NNPS']:
            if word[0] != word[0].upper():
                error_list.append(f"Grammar: The noun '{word}' should be capitalized.")
    
    error_list.extend(check_pronoun_verb_agreement(cleaned_sentence))
    
    return error_list

def check_pronoun_verb_agreement(sentence):
    """
    Checks pronoun-verb agreement rules.

    Args:
    - sentence (str): Input sentence.

    Returns:
    - list: Agreement errors found
    """
    errors = []
    words = sentence.lower().split()
    
    for i, word in enumerate(words):
        if word == 'i' and i + 1 < len(words):
            if words[i + 1] not in rule_dic['i']:
                errors.append(f"Grammar: Incorrect verb form after 'I'. Use appropriate helping verb.")
        
        if word == 'he' and i + 1 < len(words):
            if words[i + 1] not in rule_dic['he']:
                errors.append(f"Grammar: Incorrect verb form after 'he'. Use appropriate helping verb.")
                
        if word == 'you' and i + 1 < len(words):
            if words[i + 1] not in rule_dic['you']:
                errors.append(f"Grammar: Incorrect verb form after 'you'. Use appropriate helping verb.")
    
    return errors

def grammar_check(essay, suggestions):
    """
    Performs grammar analysis and calculates grammar score.

    Args:
    - essay (str): The input essay text.
    - suggestions (list): List to store grammar suggestions.

    Returns:
    - float: Grammar score from 0.0 to 10.0
    """
    grammar_errors = []
    sentences = sent_tokenize(essay)
    
    for sentence in sentences:
        grammar_errors.extend(check_grammar_rules(sentence))
    
    grammar_penalty = len(grammar_errors) * 0.5
    grammar_score = max(10 - grammar_penalty, 0)
    
    suggestions.extend(grammar_errors)
    return grammar_score

def syntax_check(essay):
    """
    Calculates final essay score based on spelling and grammar.

    Args:
    - essay (str): The input essay text.

    Returns:
    - dict: Dictionary containing scores and feedback
    """
    spelling_ratio, spelling_suggestions = spelling_check(essay)
    
    alpha = 1.15
    spelling_penalty = alpha * spelling_ratio * 10
    spelling_score = max(10 - spelling_penalty, 0)
    
    grammar_errors = []
    grammar_score = grammar_check(essay, grammar_errors)
    
    final_score = (spelling_score + grammar_score) / 2
    
    feedback = {
        "final_score": round(final_score, 2),
        "spelling_score": round(spelling_score, 2),
        "grammar_score": round(grammar_score, 2),
        "spelling_errors": spelling_suggestions,
        "grammar_errors": grammar_errors,
        "total_errors": len(spelling_suggestions) + len(grammar_errors)
    }
    
    return feedback