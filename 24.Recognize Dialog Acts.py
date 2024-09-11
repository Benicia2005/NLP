import nltk
from nltk import word_tokenize
def classify_dialog(text):
    words = set(word_tokenize(text.lower()))
    if "hello" in words:
        return "Greeting"
    elif "how" in words:
        return "Question"
    return "Statement"
print(classify_dialog("Hello, how are you?"))
