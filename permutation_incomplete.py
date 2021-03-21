# PermMissingElem
# Find the missing element in a given permutation.

def solution(A):
    # handle the trivial cases
    if len(A) == 0:
        return 1
    # get the full array as a set
    full_array = range(len(A) + 1)
    set_full = set([x + 1 for x in full_array])
    set_a = set(A)
    # get difference
    diff = list(set_full - set_a)
    return diff[0]
