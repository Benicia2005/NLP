import random
text = "this is a simple example this is another example"
tokens = text.split()
bigrams = {tokens[i]: tokens[i+1] for i in range(len(tokens)-1)}
word = "this"
for _ in range(5): word = bigrams.get(word, "this"); print(word, end=" ")
