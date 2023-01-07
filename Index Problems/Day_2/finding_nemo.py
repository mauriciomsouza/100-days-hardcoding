def FindNemo(s):
    if 'Nemo' in s:
        return (s.split().index('Nemo')) +1
    else:
        return "I can't find Nemo!"


s = "I am finding Emo !"
print(FindNemo(s))
