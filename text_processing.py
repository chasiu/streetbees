def tokenise(text: str) -> list:
    """
    Takes a string and tokenises it on a space character
    """
    return text.split(" ")


def drop_stop(text: str, stop_words: list, ignore_case=True) -> str:
    """
    Remove stopwords from a string.
    """
    if ignore_case:
        text = text.lower()
        stop_words = [word.lower() for word in stop_words]
    split_text = tokenise(text)
    new_text = [word for word in split_text if word not in stop_words]

    return " ".join(word for word in new_text)


def drop_chars(text: str) -> str:
    """
    Remove specific characters and replace them with a space. Uses Regex.
    """
    import string

    return "".join((char for char in text if char not in string.punctuation))


def drop_whitespace(text: str) -> str:
    """
    Replace whitespace (multiple spaces, tabs, newlines etc) with a single space
    """
    import re

    return re.sub("\s+", " ", text)