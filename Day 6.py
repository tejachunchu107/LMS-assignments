#6. Write a Python program to using NLTK and Spacy
#Convert text to lowercase.
#Remove stopwords using NLTK
text = "Hello World"
lowercase_text = text.lower()
print("Lowercase Text:", lowercase_text)
#Remove stopwords using NLTK
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
text = "NLP is a Natural language process which is very useful for sentiment analysis and it has many real time projects though itd very easy to do and it is a beautiful language and it is specificially and widely used in business purposes"
words = text.split()
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]
filtered_text = ''.join(filtered_words)
print("Filtered Text:",filtered_text)
