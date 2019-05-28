# Solution submitted by learner 'Justin Amarin'
from itertools import product

def NumberToPattern(index, k):
    lst = ["".join(i) for i in product("ACGT", repeat=k)]
    return lst[index]