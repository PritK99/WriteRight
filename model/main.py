# Import necessary modules
import sys
import shutil
from statistics import statistics_check
from syntax import syntax_check
from semantic import semantic_check

# Get the width of the terminal for formatting
window_width = shutil.get_terminal_size().columns

# Prompt the user for the topic sentence
prompt = input("Enter the topic sentence: ")

# Initialize an empty string to store the essay
essay = ""

# Prompt the user to enter the essay, press enter twice to exit
print("Enter the essay below. Press enter key twice to exit.")
print('/' * window_width)
while True:
    user_input = input()

    if user_input == '':
        break
    else:
        essay += user_input
print('/' * window_width)

# Initialize a list to store suggestions
suggestions = []

# Perform statistical analysis and get the statistics score
statistic_score = statistics_check(essay, suggestions)

# Perform syntax analysis and get the syntax score
syntax_score = syntax_check(essay, suggestions)

# Perform semantic analysis and get the semantic score
semantic_score = semantic_check(prompt, essay, suggestions)

# Calculate the total score based on weights for each analysis
total_score = (statistic_score + 2 * syntax_score + 2 * semantic_score) / 5

# Display the results and suggestions
print('////////////' + "Results" + '////////////')
print(f"Statistics score: {statistic_score:.1f}/10.0")
print(f"Syntax score: {syntax_score:.1f}/10.0")
print(f"Semantic score: {semantic_score:.1f}/10.0")
print(f"Total score: {total_score:.1f}/10.0")

print(('/////////' + "Suggestions" + '/////////'))
for suggestion in suggestions:
    print(suggestion)
print("///////////////////////////////")