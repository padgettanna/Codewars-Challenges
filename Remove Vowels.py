def disemvowel(string_):
    for char in "aeiouAEIOU":
        string_ = string_.replace(char, "")
    return string_
