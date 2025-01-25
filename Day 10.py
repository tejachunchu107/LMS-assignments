#10
import re
from collections import Counter

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

# Example usage
if __name__ == "__main__":
    text = input("Enter a text: ")
    word_frequency(text)
    emails = extract_emails(text)
    print("Extracted emails:", emails)