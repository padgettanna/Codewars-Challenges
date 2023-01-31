def find_needle(haystack):
    for item in haystack:
        if item == "needle":
            return f"found the needle at position {haystack.index(item)}"
