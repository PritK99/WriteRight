# Driver code
import sys
import shutil
from statistics import statistics_check
from syntax import syntax_check
from semantic import semantic_check

window_width = shutil.get_terminal_size().columns

prompt = input("Enter the topic sentence: ")

essay = ""
print("Enter the essay below. Press enter key twice to exit.")
print('/' * window_width)
while True:
    user_input = input()

    if user_input == '':
        break
    else:
        essay+=user_input
print('/' * window_width)

statistic_score = statistics_check(essay)
syntax_score = syntax_check(prompt, essay)
semantic_score = semantic_check(prompt, essay)

total_score = (statistic_score + 2*syntax_score + 2*semantic_score)/5

print('////////////' + "Results" + '////////////')
print(f"Statistics score: {statistic_score:.1f}/10.0")
print(f"Syntax score: {syntax_score:.1f}/10.0")
print(f"Semantic score: {semantic_score:.1f}/10.0")
print(f"Total score: {total_score:.1f}/10.0")
print("///////////////////////////////")