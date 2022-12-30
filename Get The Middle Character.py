def get_middle(s):
    if len(s) % 2 != 0:
        middle = int(len(s) // 2)
        return(s[middle])
    else:
        middle1 = int(len(s) - 1)// 2
        middle2 = int(len(s) + 2) // 2
        return(s[middle1:middle2])
