import sys
import getopt
from sentence_transformers import SentenceTransformer, util

def get_similarity(prompt, essay):
    """
    Calculates the cosine similarity between a prompt and an essay using a pre-trained sentence transformer model.

    Args:
    - prompt (str): The prompt text.
    - essay (str): The essay text.

    Returns:
    - float: The cosine similarity score.
    """

    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

    prompt_embedding = model.encode(prompt, convert_to_tensor=True)
    essay_embedding = model.encode(essay, convert_to_tensor=True)

    similarity_score = util.pytorch_cos_sim(prompt_embedding, essay_embedding).item()

    return similarity_score

def semantic_check(prompt, essay, suggestions):
    """
    Performs semantic analysis by calculating the similarity score between a prompt and an essay.

    Args:
    - prompt (str): The prompt text.
    - essay (str): The essay text.

    Returns:
    - float: The semantic score ranging from 0.0 to 10.0.
    """
    similarity_score = get_similarity(prompt, essay)

    if (similarity_score < 0.5):
        suggestions.append("Try to rephrase the essay to make it more relevant to the given topic.")

    # All scores greater than 0.7 are considered to be perfect match with the prompt
    if (similarity_score >= 0.7):
        return 10.0
    elif (similarity_score <= 0.0):
        return 0.0
    else:
        return (similarity_score*10.0)/0.7