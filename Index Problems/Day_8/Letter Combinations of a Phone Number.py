import itertools

def ArgumentPerm(list_digits): 
    base = {'1': '', '2':'abc', '3':'def', '4':'ghi', '5': 'jkl', '6':'mno', 
            '7':'pqrs', '8':'tuv', '9':'wxyz'}
    out = ''
    for item in list_digits:
        out += base[item]
    return out.strip()

def CombinationsNumber(input):
    input = list(str(input))
    r_lenght = len(input) if '1' not in input else len(input) - input.count('1')
    output = list(itertools.permutations(ArgumentPerm(input),r_lenght))
    return [''.join(output[k]) for k in range(len(output))]
    

input = 321
print(CombinationsNumber(input))
