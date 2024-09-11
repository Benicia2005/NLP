from transformers import pipeline
translator = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")
translation = translator("Hello, how are you?", clean_up_tokenization_spaces=False)
# Translate the text
def translate(text):
    result = translator(text)[0]['translation_text']
    return result

# Example usage
english_text = "Hello, how are you?"
french_translation = translate(english_text)
print(french_translation)
