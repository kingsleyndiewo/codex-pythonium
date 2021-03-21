# TapeEquilibrium
# Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.

from itertools import accumulate

def solution(A):
    # get the trivial case
    if len(A) == 2:
        return abs(A[0] - A[1])
    # get the sum of the array
    array_sum = sum(A)
    # get the accumulated sums
    list_of_sums = list(accumulate(A))
    # find the list of differences
    list_of_diffs = [abs(x - (array_sum - x)) for x in list_of_sums]
    # enforce 0 < P < N
    list_of_diffs.pop()
    # return the smallest
    return min(list_of_diffs)

print(solution([-10, -20, -30, -40, 100]))