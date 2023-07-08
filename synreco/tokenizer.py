"""the tokenizer will tokenize the text into
it's words, and it will separate the names from
symbols used in the text."""


def tokenize(statement: str):
    tokenized_text = []

    for word in statement:

