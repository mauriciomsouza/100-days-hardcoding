import itertools


def arrangements(n):
    arr = []
    for lenght in range(n, 0, -1):
        arr_aux = itertools.combinations_with_replacement([1, 2, 3], r=lenght)
        for item in arr_aux:
            if sum(item) == n:
                arr.append(item)
    return arr

def nim_game(number):
    arrs = arrangements(number)
    arr_lengths = [len(a) for a in arrs]
    min_leghts = min(arr_lengths)
    if not(min_leghts % 2 == 0):
        return True
    else: 
        return False




for k in range(1,20):
    print(k, nim_game(k))





