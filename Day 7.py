#Write a Python script that:
#7. Use Genism to preprocess data from a sample text file, follow basic procedures like tokenization, stemming, lemmatization etc.
import nltk
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download necessary resources for NLTK
nltk.download('wordnet')
nltk.download('omw-1.4')

# Function for text preprocessing
def preprocess_text(text):
    # Tokenization using Gensim's simple_preprocess
    tokens = simple_preprocess(text, deacc=True)  # deacc removes punctuations

    # Remove stopwords
    tokens = [word for word in tokens if word not in STOPWORDS]

    # Stemming using NLTK
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in tokens]

    # Lemmatization using NLTK
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in stemmed_tokens]

    return lemmatized_tokens

# Example input sentence
text_data = "The quick brown fox jumps over the lazy dog. This is a test document for text preprocessing."

# Preprocess the text
preprocessed_data = preprocess_text(text_data)

# Display the results
print("Preprocessed Text Tokens:")
print(preprocessed_data)
