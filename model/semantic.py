import sys
import getopt
from sentence_transformers import SentenceTransformer, util

def get_similarity(prompt, essay):
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

    # Encode prompt and essay into embeddings
    prompt_embedding = model.encode(prompt, convert_to_tensor=True)
    essay_embedding = model.encode(essay, convert_to_tensor=True)

    # Calculate cosine similarity
    similarity_score = util.pytorch_cos_sim(prompt_embedding, essay_embedding).item()

    return similarity_score

def semantic_check(prompt, essay):
    similarity_score = get_similarity(prompt, essay)
    
    if (similarity_score >= 0.7):
        return 10.0
    elif (similarity_score <= 0.0):
        return 0.0
    else:
        return (similarity_score*10.0)/0.7