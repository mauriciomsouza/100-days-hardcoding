import random
import string

def pairs(s):
    return sum([s.count(element)//2 for element in set(s)])
    


#Bloco para testes
for i in range(20):
    n = random.randint(6,24)
    s = ''.join(random.choices(list('ABCDE'), k = n))
    print(s, pairs(s))
