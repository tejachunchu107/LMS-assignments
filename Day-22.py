#Day 22
import re

def clean_text(text):
    
    text = text.lower()
    
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text


input_text = 'Hello, World! Welcome to NLP 101.'
cleaned_text = clean_text(input_text)
print(cleaned_text)
