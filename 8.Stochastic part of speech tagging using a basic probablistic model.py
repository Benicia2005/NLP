import nltk
nltk.download('brown'); nltk.download('universal_tagset')
tagger = nltk.UnigramTagger(nltk.corpus.brown.tagged_sents(tagset='universal'))
tokens = nltk.word_tokenize("This is simple.")
print(tagger.tag(tokens))
