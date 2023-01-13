def IsValid(s,t):
    if len(s) != len(s):
        return False
    s = list(s)
    t = list(t)
    aux = s.copy()
    for item in t:
        if item in s:
            aux.remove(item)
    return not bool(aux)    



