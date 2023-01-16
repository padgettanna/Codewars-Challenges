def consonant_count(s):
    count = 0
    for i in s.lower():
        if i in "bcdfghjklmnpqrstvwxyz":
            count += 1
    return count
