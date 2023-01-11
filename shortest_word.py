def find_short(s):
    list = s.split()
    return len(min(list, key=len))
