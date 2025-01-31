#Day 28
import spacy

!python -m spacy download en_core_web_sm

nlp = spacy.load("en_core_web_sm")

def perform_ner(text):
    doc = nlp(text)
    for ent in doc.ents:
        print(f"Entity: {ent.text}, Label: {ent.label_}")

text = "Apple is looking at buying U.K. startup for $1 billion"
perform_ner(text)
