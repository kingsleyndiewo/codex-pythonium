# FrogJmp
# Count minimal number of jumps from position X to Y.

def solution(X, Y, D):
    # check for trivial cases
    if X == Y:
        return 0
    elif D == (Y - X):
        return 1
    # compute distance to cover
    gap = Y - X
    # compute jumps; round up
    jumps = ceil(gap / D)
    return jumps
