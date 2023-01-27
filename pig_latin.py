def pig_it(text):
  list = []
  punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
  for i in text.split():
    if i in punc:
      list.append(i)
    else:
      list.append(i[1:] + i[0] + "ay")
  return " ".join(list)
