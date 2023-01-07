""" The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence. """

def getPermutation(n, k):
    from math import factorial
    from itertools import permutations
    root_array = [i for i in range(1, n + 1)]  # applying list comprehension
    permutations_dict = {}
    amount_permutations = factorial(n)
    perm_iter = permutations(root_array,n)
    perm_list = list(perm_iter)
    for i in range(amount_permutations):
        permutations_dict[i+1] = perm_list[i]

    kth_perm = ''
    for x in permutations_dict[k]:
        kth_perm += str(x)
    return kth_perm #final of function



