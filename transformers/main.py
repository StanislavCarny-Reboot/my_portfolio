import pandas as pd
from tokenizer import SimpleWordTokenizer

africa_galore = pd.read_json(
    "https://storage.googleapis.com/dm-educational/assets/ai_foundations/africa_galore.json"
)
dataset = africa_galore["description"].values
print("Loaded dataset with", dataset.shape[0], "paragraphs.")

# Initialize the tokenizer. This will build the tokenizer's vocabulary with
# all the tokens that appear in the dataset.
tokenizer = SimpleWordTokenizer(dataset)

# # Translate all tokens to their corresponding IDs.
# encoded_tokens = []
# for text in dataset:
#     # Split text into tokens and translate the tokens to token IDs.
#     token_ids = tokenizer.encode(text)
#     encoded_tokens.append(token_ids)

corpus = "Hello how are you doing !"
tokenizer = SimpleWordTokenizer(corpus)
token_ids = tokenizer.encode("Hello There")
