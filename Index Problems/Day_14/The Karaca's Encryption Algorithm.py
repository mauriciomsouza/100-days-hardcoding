def Encrypt(word):
    base = {'a':0, 'e':1, 'i':2, 'o':2, 'u':3}
    word = word[::-1]
    out = ''
    for l in word:
        if l in base:
            out += str(base[l])
        else:
            out += l
    out += 'aca'
    return out


words = ['banana', 'karaca', 'burak', 'alpaca']
for word in words:
    print(word, Encrypt(word))





