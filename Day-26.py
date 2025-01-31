#Day 26

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def cosine_sim(text1, text2):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    return similarity

string1 = "This is the first document."
string2 = "This document is the second document."
similarity_score = cosine_sim(string1, string2)
print(f"Cosine Similarity between strings: {similarity_score}")
