def format_words(words):
    return ", ".join(w for w in words if w)[::-1].replace(",", "dna ", 1)[::-1] if words else ""
