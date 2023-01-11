def friend(x):
    y = []
    for item in x:
        if len(item) == 4:
            y.append(item)
    return y
