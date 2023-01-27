def encode(st):
    replacement = {"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}
    for char in replacement.keys():
        st = st.replace(char, replacement[char])  
    return st
    
def decode(st):
    replacement = {"1": "a", "2": "e", "3": "i", "4": "o", "5": "u"}
    for char in replacement.keys():
        st = st.replace(char, replacement[char])  
    return st
