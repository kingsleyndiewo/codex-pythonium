# OddOccurrencesInArray
# Find value that occurs in odd number of elements. 

from collections import Counter

def solution(A):
	# get the trivial case
	if len(A) == 1:
		return A[0]
	# get Counter of A
	frequencies = Counter(A)
	# find the value that has an odd frequency
	black_sheep = [x[0] for x in frequencies.items() if x[1] % 2 > 0][0]
	return black_sheep
