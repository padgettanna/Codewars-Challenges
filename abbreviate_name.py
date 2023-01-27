def abbrev_name(name):
    initials = []
    for i in name.split():
        initials.append(i[0].upper())
    return ".".join(initials)
