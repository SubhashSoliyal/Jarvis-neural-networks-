from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load the tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Load the model
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Encode the prompt
prompt = "Today is a beautiful day and "
encoded_prompt = tokenizer.encode(prompt, return_tensors="pt")

# Generate text
generated_text = model.generate(encoded_prompt, max_length=100, top_p=0.95, top_k=50)

# Decode the generated text
decoded_text = tokenizer.decode(generated_text[0], skip_special_tokens=True)

# Print the generated text
print(decoded_text)
