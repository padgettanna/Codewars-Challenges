def solution(s):
    new_list = []
    s = list(s)
    if len(s) % 2 != 0:
       s.append("_")
    for i in range(0, len(s), 2):
        new_list.append(s[i] + s[i + 1])
    return new_list
