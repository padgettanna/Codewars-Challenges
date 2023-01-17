def reverse_words(text):
    t = text.split(" ")
    list = []
    for i in t:
      i = i[::-1]
      list.append(i)
    return " ".join(list)
