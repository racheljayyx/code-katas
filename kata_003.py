def accum(st):
    letters = list(st.lower())
    for i, ch in enumerate(letters):
        letters[i] = (ch*(i+1)).capitalize()
    return "-".join(letters)
