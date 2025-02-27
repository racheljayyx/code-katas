def spin_words(sentence):
    
    words = sentence.split()
    new_words = list(map(lambda word: word[::-1] if len(word) >= 5 else word, words))
    return " ".join(new_words)
