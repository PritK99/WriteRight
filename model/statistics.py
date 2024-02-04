import pandas as pd
import nltk
import math
import os
from nltk import word_tokenize, sent_tokenize

# Download nltk data and model for POS Tagging
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def get_statistics(path, desired_column):
    """
    Extracts statistical features from a dataset column.

    Args:
    - path (str): Path to the CSV file.
    - desired_column (str): Name of the column containing essays.

    Returns:
    - Tuple: Tuple containing normalized values for word count, sentence count, words per sentence, and POS tags frequency.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_dir, '..', 'data', path)

    try:
        df = pd.read_csv(path)
        essays = df[desired_column]
    except FileNotFoundError:
        print(f"Error: File not found at {path}")
        return

    num_sentences = 0
    num_words = 0
    norm_pos_freq = {}

    for essay in essays:
        sentences = sent_tokenize(essay)
        num_sentences += len(sentences)

        words = word_tokenize(essay)
        tags = nltk.pos_tag(words)

        num_words += len(words)

        for tag in tags:
            if tag[1] in norm_pos_freq:
                norm_pos_freq[tag[1]] += 1
            else:
                norm_pos_freq[tag[1]] = 1

    norm_num_words = (int)(num_words / len(essays))
    norm_num_sentences = (int)(num_sentences / len(essays))
    norm_num_words_in_sentences = (int)(norm_num_words / norm_num_sentences)
    for tag in norm_pos_freq.keys():
            norm_pos_freq[tag] = max((int)(norm_pos_freq[tag] / len(essays)),1)

    return norm_num_words, norm_num_sentences, norm_num_words_in_sentences, norm_pos_freq


def statistics_check(essay, suggestions):
    """
    Evaluates an essay based on statistical features and provides suggestions.

    Args:
    - essay (str): The essay text to be evaluated.
    - suggestions (list): A list to store suggestions based on the evaluation.

    Returns:
    - float: The final statistics score.
    """
    train_dataset_name = "train.csv"
    desired_column = "full_text"

    norm_num_words, norm_num_sentences, norm_num_words_in_sentences, norm_pos_freq = get_statistics(train_dataset_name, desired_column)

    num_sentences = 0
    num_words = 0
    pos_freq = {}

    sentences = sent_tokenize(essay)
    num_sentences += len(sentences)

    words = word_tokenize(essay)
    tags = nltk.pos_tag(words)

    num_words += len(words)

    for tag in tags:
        if tag[1] in pos_freq:
            pos_freq[tag[1]] += 1
        else:
            pos_freq[tag[1]] = 1
    
    tag_penalty = {}
    tag_count = 0
    pos_penalty = 0.0
    major_tags = [
    "NN",  # Noun, singular or mass
    "VB",  # Verb, base form
    "JJ",  # Adjective
    "PR",  # Pronoun (unspecific type)
    "WH",  # Wh-pronoun
    "MD",  # Modal verb
    "IN",  # Preposition or subordinating conjunction
    "RB",  # Adverb
    "DT",  # Determiner
    "CC"   # Coordinating conjunction
    ]

    for tag in norm_pos_freq.keys():
        tag_count+=1
        tag_penalty = math.fabs(norm_pos_freq[tag] - pos_freq.get(tag, 0))/norm_pos_freq[tag]
        if tag in major_tags:
            pos_penalty += tag_penalty*2
        else:
            pos_penalty += tag_penalty
    
    num_words_in_sentences = (int)(num_words / num_sentences)

    num_words_in_sentences_penalty = math.fabs(norm_num_words_in_sentences - num_words_in_sentences)/norm_num_words_in_sentences
    num_sentences_penalty = math.fabs(norm_num_sentences - num_sentences)/norm_num_sentences
    num_words_penalty = math.fabs(norm_num_words - num_words)/norm_num_words
    pos_penalty = pos_penalty/(tag_count+len(major_tags))

    if (num_words_in_sentences_penalty > 0.5):
        suggestion = "The number of words in sentences is too high or too low. The number of words in sentences should be around " + str(norm_num_words_in_sentences) + "."
        suggestions.append(suggestion)
    if (num_sentences_penalty > 0.5):
        suggestion = "The number of sentences is too high or too low. The number of sentences should be around " + str(norm_num_sentences) + "."
        suggestions.append(suggestion)
    if (num_words_penalty > 0.5):
        suggestion = "The number of words is too high or too low. The number of words should be around " + str(norm_num_words) + "."
        suggestions.append(suggestion)
    if (pos_penalty > 0.7):
        suggestion = "The part of speech distribution is too high or too low. Try to use a different distribution of parts of speech."
        suggestions.append(suggestion)

    penalty_ratio = (num_words_penalty + num_sentences_penalty + 2*num_words_in_sentences_penalty + pos_penalty)/5

    penalty_score = (penalty_ratio*10.0)

    statistics_score = max(10.0 - penalty_score, 0)

    # print all ratios
    # print(f"num_words_penalty: {num_words_penalty:.1f}")
    # print(f"num_sentences_penalty: {num_sentences_penalty:.1f}")
    # print(f"num_words_in_sentences_penalty: {num_words_in_sentences_penalty:.1f}")
    # print(f"pos_penalty: {pos_penalty:.1f}")

    return statistics_score