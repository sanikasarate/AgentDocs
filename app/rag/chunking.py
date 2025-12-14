def chunk_text(text):
    return [text[i:i+100] for i in range(0, len(text), 100)]
