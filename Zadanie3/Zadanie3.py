import numpy as np
import pandas as pd

# Wprowadzenie danych
df = pd.read_csv('dictionary', sep="\n", header=None)
df.columns = ["word"]

# Czyszczenie danych
bad_chars = ['/Z', '/V']
def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = []
for d in df['word']:
    date = strip_characters(d)
    stripped_test_data.append(date)

dictionary = pd.DataFrame(stripped_test_data, columns = ['word'])

def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]
    return (matrix[size_x - 1, size_y - 1])

# Wprowadzenie danych
print('proszę wpisać słowo (z małej litery)')
word = input()
print('prosze wpisać ilość podobnych słów do wypisania ')
return_words = input()

distance_list = []
for w in dictionary['word']:
    distance = levenshtein(w, word)
    distance_list.append(distance)
dictionary['distance'] = pd.Series(distance_list)

# Sortowanie po 'distance' i wyświetlenie wynikow
dictionary = dictionary.sort_values(by=['distance'], ascending=True)
print(dictionary['word'].iloc[0:int(return_words)])
