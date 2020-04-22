def formatEnumeration(li):
    if len(li) <= 2:
        return " and ".join(li)
    else:
        return f"{', '.join(li[:-1])} and {li[-1]}"
