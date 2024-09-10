import random
import re
from collections import defaultdict
def generate_bigrams(text):
    words = re.findall(r'\b\w+\b', text.lower())  
    bigrams = [(words[i], words[i + 1]) for i in range(len(words) - 1)]
def build_bigram_model(bigrams):
    bigram_model = defaultdict(list)
    for word1, word2 in bigrams:
        bigram_model[word1].append(word2)  
    return bigram_model
def generate_text(bigram_model, start_word, length=10):
    current_word = start_word.lower()
    result = [current_word]
    for _ in range(length - 1):
        if current_word in bigram_model:
            next_word = random.choice(bigram_model[current_word])
            result.append(next_word)
            current_word = next_word
        else:
            break 
    return ' '.join(result)
random.seed(0)
input_text = "roses are red violets are blue sugar is sweet and so are you"
bigrams = generate_bigrams(input_text)
bigram_model = build_bigram_model(bigrams)
start_word = "roses"
generated_text = generate_text(bigram_model, start_word)
print("Generated Text:", generated_text)
