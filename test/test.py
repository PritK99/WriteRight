# Import necessary modules
import os
import pandas as pd
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from model.statistics import statistics_check
from model.syntax import syntax_check
from model.semantic import semantic_check

path = "test.csv"
essay_column = "essay"
label_column = "domain1_score"

script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, '..', 'data', path)

try:
    df = pd.read_csv(path)
    essays = df[essay_column]
    labels = df[label_column]
except FileNotFoundError:
    print(f"Error: File not found at {path}")
    exit(0)

def mean_squared_error(y, y_pred):
    return (y - y_pred)**2

prompt = "More and more people use computers, but not everyone agrees that this benefits society. Those who support advances in technology believe that computers have a positive effect on people. They teach hand-eye coordination, give people the ability to learn about faraway places and people, and even allow people to talk online with other people. Others have different ideas. Some experts are concerned that people are spending too much time on their computers and less time exercising, enjoying nature, and interacting with family and friends. Write a letter to your local newspaper in which you state your opinion on the effects computers have on people. Persuade the readers to agree with you."
accuracy = 0
iterations = 100

# Testing over 100 examples
for i in range (iterations):
    essay = essays[i]
    label = labels[i]

    # Hewlett dataset scores between 2-12
    label = (label-2)

    suggestions = []
    statistic_score = statistics_check(essay, suggestions)
    syntax_score = syntax_check(essay, suggestions)
    semantic_score = semantic_check(prompt, essay, suggestions)
    total_score = (statistic_score + 2 * syntax_score + 2 * semantic_score) / 5
    error = mean_squared_error(label, total_score)
    
    print(f"iteration: {i:.1f}", end=" ")
    print(f"Error: {error:.1f}")
    

    accuracy += error

accuracy = accuracy/iterations
print("/////////////////////////////////////")
print(f"Mean Squared Error: {accuracy:.1f}")