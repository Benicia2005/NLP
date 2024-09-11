from sklearn.feature_extraction.text import TfidfVectorizer
docs = ["The cat sat on the mat.", "The dog sat on the log.", "Cats and dogs are pets."]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(docs)
print(tfidf_matrix.toarray())
