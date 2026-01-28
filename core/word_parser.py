import re

def parse_words(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip().split(" ")
