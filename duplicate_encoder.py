def duplicate_encode(word):
  word = list(word.lower())
  new_word = []
  for i in word:
      if word.count(i) <= 1:
          i = "("
          new_word.append(i)
      else:
          i = ")"
          new_word.append(i)
  new_word = "".join(new_word)
  return new_word
