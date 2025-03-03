import re

def to_camel_case(text):
    
    words = re.split("[-_]", text)
    
    for i, word in enumerate(words[1:], start=1):
        words[i] = word.capitalize()
   
    return "".join(words)
