def descending_order(num):
    list = sorted([int(x) for x in str(num)])
    num = "".join(str(x) for x in(list[::-1]))
    return int(num)
