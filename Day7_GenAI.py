# We use Hugging Face library because Google Gemini SDK
# does NOT provide a direct tokenizer API

from transformers import AutoTokenizer

# Load a pretrained tokenizer
# "google/flan-t5-small" is a lightweight model good for learning
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")

# Sample text (this is what we want to tokenize)
text = "Hello, how are you doing today?"

# ---------------- TOKENIZATION ----------------
# Convert text into tokens (words/subwords)
tokens = tokenizer.tokenize(text)

# Convert tokens into numerical IDs (models understand numbers, not text)
token_ids = tokenizer.encode(text)

# Print results
print("Original Text:", text)
print("Tokens:", tokens)
print("Token IDs:", token_ids)

# ---------------- DETOKENIZATION ----------------
# Convert token IDs back into readable text
decoded_text = tokenizer.decode(token_ids)

print("Decoded Text:", decoded_text)
