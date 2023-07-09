"""the tokenizer will tokenize the text into
it's words, and it will separate the names from
symbols used in the text."""
import synreco.constants as constants


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


def generalformat(tokenized_statement: list):

    statement = ""
    is_space = True

    for element in tokenized_statement:

        if element in constants.SYMBOLS_:
            statement += element
            is_space = True

        elif element == " " and is_space:
            statement += "S"
            is_space = False

        elif element != " ":
            statement += "N"
            is_space = True
    return statement


def generalformataddspace(tokenized_statement):

    statement = "S"

    for element in tokenized_statement:

        if element in constants.SYMBOLS_:
            statement += element+"S"

        elif element != " ":
            statement += "NS"

    return statement












