def alphabet_position(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    text = list(text.lower())
    positions = []
    for letter in text:
      if letter in alphabet:
          positions.append(alphabet.index(letter) + 1)
    positions = " ".join(str(i) for i in positions)

    return positions
