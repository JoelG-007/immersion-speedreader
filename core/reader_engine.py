def get_delay(word, wpm):
    base = 60 / wpm
    if word.endswith((".", "?", "!")):
        return base * 1.8
    if word.endswith(","):
        return base * 1.3
    if len(word) > 8:
        return base * 1.2
    return base
