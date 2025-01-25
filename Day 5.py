#5. Write a Python program to calculate the frequency of each word in a given text. Print the words and their corresponding counts
from collections import Counter

def word_frequency(text):
    # Normalize the text: remove punctuation and convert to lowercase
    text = text.lower()
    words = text.split()

    # Count word frequencies
    word_count = Counter(words)

    # Display each word and its count
    for word, count in word_count.items():
        print(f"{word}: {count}")

# Example input
text_input = input("Enter text: ")
word_frequency(text_input)
