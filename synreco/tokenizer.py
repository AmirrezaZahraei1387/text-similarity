"""the tokenizer will tokenize the text into
it's words, and it will separate the names from
symbols used in the text."""
import constants


def tokenize(statement: str):
    tokenized_text = []
    maked_name = ""

    for word in statement:

        if word in constants.SYMBOLS:
            if maked_name != "":
                tokenized_text.append(maked_name)
                maked_name = ""
            tokenized_text.append(word)

        else:
            maked_name += word
    return tokenized_text
