def is_pangram(s):
    pangram = list("abcdefghijklmnopqrstuvwxyz")
    s = sorted(list(s.lower()))
    new_list = []
    for i in s:
        if i.isalpha():
            new_list.append(i)
            new_list = sorted(list(set(new_list)))
    return pangram == new_list
