from transformers import pipeline
generator = pipeline("text-generation", model="gpt2")
def generate_text(prompt):
    result = generator(prompt, max_length=10000, num_return_sequences=1)
    return result[0]["generated_text"]
prompt = input("Enter the question: ")
response=generate_text(prompt)
print(response)
