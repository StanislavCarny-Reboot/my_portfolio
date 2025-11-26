import re


class SimpleWordTokenizer:
    """A simple word tokenizer.

    The tokenizer splits the text sequence based on whitespace, using the
    `encode` method to convert the text into a sequence of indices and the
    `decode` method to convert indices back into text.

    The simple word tokenizer that can be initialized with a corpus or using a
    provided vocabulary list

    Typical usage example:

        corpus = "Hello there!"
        tokenizer = SimpleWordTokenizer(text)
        print(tokenizer.encode('Hello'))

    """

    # Define constants.
    UNKNOWN_TOKEN = "<UNK>"
    PAD_TOKEN = "<PAD>"

    def __init__(self, corpus: list[str], vocabulary: list[str] | None = None):
        """Initializes the tokenizer with texts in corpus or with a vocabulary.

        Args:
          corpus: Input text dataset.
          vocabulary: A pre-defined vocabulary. If None,
              the vocabulary is automatically inferred from the texts.
        """

        if vocabulary is None:
            # Build the vocabulary from scratch.
            if isinstance(corpus, str):
                corpus = [corpus]

            # Convert text sequence to tokens.
            tokens = []
            for text in corpus:
                for token in self.space_tokenize(text):
                    tokens.append(token)

            # Create a vocabulary comprising of unique tokens.
            vocabulary = self.build_vocabulary(tokens)

            # Add special unknown and pad tokens to the vocabulary list.
            self.vocabulary = [self.PAD_TOKEN] + vocabulary + [self.UNKNOWN_TOKEN]

        else:
            self.vocabulary = vocabulary

        # Size of vocabulary.
        self.vocabulary_size = len(self.vocabulary)

        # Create token-to-index and index-to-token mappings.
        self.token_to_index = {}
        self.index_to_token = {}
        # Loop through all tokens in the vocabulary. enumerate automatically
        # assigns a unique index to each token.
        for index, token in enumerate(self.vocabulary):
            self.token_to_index[token] = index
            self.index_to_token[index] = token

        # Map the special tokens to their IDs.
        self.pad_token_id = self.token_to_index[self.PAD_TOKEN]
        self.unknown_token_id = self.token_to_index[self.UNKNOWN_TOKEN]

    def space_tokenize(self, text: str) -> list[str]:
        """Splits a given text on whitespace into tokens.

        Args:
            text: Text to split on whitespace.

        Returns:
            List of tokens after splitting `text`.
        """

        # Use re.split such that multiple spaces are treated as a single
        # separator.
        return re.split(" +", text)

    def join_text(self, text_list: list[str]) -> str:
        """Combines a list of tokens into a single string.

        The combined tokens, as a single string, are separated by spaces in the
        string.

        Args:
            text_list: List of tokens to be joined.

        Returns:
            String with all tokens joined with a whitespace.

        """
        return " ".join(text_list)

    def build_vocabulary(self, tokens: list[str]) -> list[str]:
        """Create a vocabulary list from the list of tokens.

        Args:
            tokens: The list of tokens in the dataset.

        Returns:
            List of unique tokens (vocabulary) in the dataset.
        """
        return sorted(list(set(tokens)))

    def encode(self, text: str) -> list[int]:
        """Encodes a text sequence into a list of indices.

        Args:
            text: The input text to be encoded.

        Returns:
            A list of indices corresponding to the tokens in the input text.
        """

        # Convert tokens into indices.
        indices = []
        unk_index = self.token_to_index[self.UNKNOWN_TOKEN]
        for token in self.space_tokenize(text):
            token_index = self.token_to_index.get(token, unk_index)
            indices.append(token_index)

        return indices

    def decode(self, indices: int | list[int]) -> str:
        """Decodes a list (or single index) of integers back into tokens.

        Args:
            indices: A single index or a list of indices to be
                decoded into tokens.

        Returns:
            A string of decoded tokens corresponding to the input indices.
        """

        # If a single integer is passed, convert it into a list.
        if isinstance(indices, int):
            indices = [indices]

        # Map indices to tokens.
        tokens = []
        for index in indices:
            token = self.index_to_token.get(index, self.unknown_token_id)
            tokens.append(token)

        # Join the decoded tokens into a single string.
        return self.join_text(tokens)
