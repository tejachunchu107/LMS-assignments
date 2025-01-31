#Day 24

import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import re

nltk.download('punkt')

def most_common_words(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return

    tokens = word_tokenize(text)
    cleaned_tokens = [re.sub(r'[^a-zA-Z0-9]', '', token).lower() for token in tokens]
    cleaned_tokens = [token for token in cleaned_tokens if token]
    fdist = FreqDist(cleaned_tokens)

    print("10 Most Common Words:")
    for word, frequency in fdist.most_common(10):
        print(f"{word}: {frequency}")

most_common_words('your_file.txt')
