def inverte(s):
    if len(s) == 1:
        return s[0]
    else:
        return inverte(s[1:]) + s[0]