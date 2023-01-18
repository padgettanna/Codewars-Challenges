import math
def get_average(marks):
    total = 0
    for i in range(0, len(marks)):
        total += marks[i]
    return math.floor(total / len(marks))
