from textblob import TextBlob
text = "Apple is looking at buying U.K. startup for $1 billion."
blob = TextBlob(text)
entities = blob.noun_phrases
print("Named Entities:")
for entity in entities:
    print(entity)
