def generate_hashtag(s):
    hashtag = "#" + s.title().replace(" ", "")
    if int(len(hashtag)) > 140:
        return False
    if s == "":
        return False
    return hashtag
