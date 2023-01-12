def spin_words(sentence):
    list = sentence.split()
    reverse = []
    for word in list:
        if len(word) < 5:
            reverse.append(word)    
        elif len(word) >= 5:
            reverse.append(word[::-1])   
    return " ".join(reverse)
