# 8.
import re
import requests
from bs4 import BeautifulSoup
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Ensure necessary NLTK resources are available
nltk.download('punkt')

def word_frequency(text):
    # Convert text to lowercase and split into words
    words = text.lower().split()
    
    # Count frequency of each word
    word_counts = Counter(words)
    
    # Print words and their frequencies
    for word, count in word_counts.items():
        print(f"{word}: {count}")

def extract_emails(text):
    # Regular expression pattern for email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_pattern, text)

def tokenize_text(text):
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    return words, sentences

def fetch_webpage_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string if soup.title else "No title found"

def clean_text(text):
    # Remove special characters and convert to lowercase
    cleaned_text = re.sub(r'[^A-Za-z0-9 ]+', '', text).lower()
    return cleaned_text

# Example usage
if __name__ == "__main__":
    text = input("Enter a text: ")
    print("Cleaned text:", clean_text(text))
    word_frequency(text)
    emails = extract_emails(text)
    print("Extracted emails:", emails)
    words, sentences = tokenize_text(text)
    print("Tokenized words:", words)
    print("Tokenized sentences:", sentences)
    
    url = "https://example.com"
    print("Webpage title:", fetch_webpage_title(url))
